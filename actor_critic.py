import numpy as np
from keras.models import Sequential, Model
from keras.layers import Dense, Dropout, Input
from keras.layers.merge import Add, Multiply
from keras.optimizers import Adam

import tensorflow as tf

import random
from collections import deque

class ActorCritic:
    def __init__(self, session, action_space, observation_space_shape):

        # Hyperparameters
        self.learning_rate = 0.001
        self.epsilon = 1.0
        self.epsilon_decay = 0.99
        self.gamma = 0.95
        self.tau = 0.125

        self.session = session # Current session
        self.action_space = action_space
        self.observation_space_shape = observation_space_shape
        self.memory = deque(maxlen=100000) # memory of the AC model

        '''
        Actor portion of constructor
        '''

        self.actor_state_input, self.actor_model = self.create_actor()
        _, self.target_actor_model = self.create_actor()

        self.actor_critic_gradient = tf.placeholder(tf.float32,[None, self.action_space.shape[0]])

        actor_weights = self.actor_model.trainable_weights
        self.actor_gradients = tf.gradients(self.actor_model.output,
                                            actor_weights,
                                            -self.actor_critic_gradient)
        gradients = zip(self.actor_gradients,
                        actor_weights)

        self.optimize = tf.train.AdamOptimizer(self.learning_rate).apply_gradients(gradients)

        '''
        Critic portion of constructor
        '''

        self.cs_input, self.ca_input, self.critic_model = self.create_critic()
        _,_,self.target_critic_model = self.create_critic

        self.critic_gradients = tf.gradients(self.critic_model.output,
                                             self.ca_input)
        self.session.run(tf.initialize_all_variables())

    '''
    Actor Functions
    '''
    def create_actor(self):

        #create Neural Network Layers for Actor
        actor_input = Input(shape=self.observation_space_shape)
        actor_l1 = Dense(240, activation='relu')(actor_input)
        actor_l2 = Dense(480, activation='relu')(actor_l1)
        actor_l3 = Dense(240, activation='relu')(actor_l2)
        actor_output = Dense(self.action_space.shape[0], activation='relu')(actor_l3)

        # Put them altogether in a model
        model = Model(input=actor_input, output=actor_output)
        adam = Adam(lr=self.learning_rate)
        model.compile(loss='mse', optimizer=adam)

        # return the model and Input
        return actor_input, model

    def _train_actor(self, samples):
        for sample in samples:
            curr_state, action, reward, new_state = sample
            predicted_action = self.actor_model.predict(curr_state)
            gradients = self.session.run(self.critic_gradients,
                                         feed_dict={
                                            self.cs_input: curr_state,
                                            self.ca_input: predicted_action
                                         })[0]
            self.session.run(self.optimize,
                             feed_dict={
                                self.actor_state_input: curr_state,
                                self.actor_critic_gradient: predicted_action
                             })


    def _update_target_actor(self):
        actor_model_weights  = self.actor_model.get_weights()
        actor_target_weights = self.target_critic_model.get_weights()

        for i in range(len(actor_target_weights)):
            actor_target_weights[i] = actor_model_weights[i]

        self.target_critic_model.set_weights(actor_target_weights)

    '''
    Critic Functions
    '''
    def create_critic(self):
        critic_state_input = Input(shape=self.observation_space_shape)
        critic_state_l1 = Dense(240, activation='relu')(critic_input)
        critic_state_l2 = Dense(480)(critic_l1)

        critic_action_input = Input(shape=self.action_space.shape)
        critic_action_l1 = Dense(480)(critic_action_input)

        merged_input = Add()([critic_state_l2, critic_state_l1])
        merged_l1 = Dense(240, activation='relu')(merged_input)
        merged_output = Dense(1, activation='relu')(merged_l1)

        model = Model(input=[critic_state_input, critic_action_input],
                      output=merged_output)
        adam = Adam(lr=self.learning_rate)
        model.compile(loss='mse',
                      optimizer=adam)

        return critic_state_input, critic_action_input, model


    def _train_critic(self, samples):
        for sample in samples:
            curr_state, action, reward, new_state, done = sample

            target_action = self.target_actor_model.predict(new_state)
            future_reward = self.target_critic_model.predict([new_state, target_action])[0][0]
            reward += self.gamma * future_reward
            self.critic_model.fit(curr_state, reward, verbose=0)

    def _update_target_critic(self):
        critic_model_weights  = self.critic_model.get_weights()
        critic_target_weights = self.critic_target_model.get_weights()

        for i in range(len(critic_target_weights)):
            critic_target_weights[i] = critic_model_weights[i]

        self.critic_target_model.set_weights(critic_target_weights)



    '''
    Helper Functions
    '''
    def update(self):
        self._update_actor()
        self._update_critic()

    def train(self):
        batch_size = 32
        if len(self.memory) < batch_size: return

        rewards = []
        samples = random.sample(self.memory, batch_size)
        self._train_critic(samples)
        self._train_actor(samples)

    def remember(self, curr_state, action, reward, new_state):
        self.memory.append([curr_state, action, reward, new_state])

    def act(self, curr_state):
        self.epsilon *= self.epsilon_decay
        if np.random.random() < self.epsilon:
            return self.env.action_space.sample()
        return self.actor_model.predict(curr_state)
