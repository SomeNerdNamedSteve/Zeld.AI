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
    Actor Functions
    '''
    def create_actor(self):

        #create Neural Network Layers for Actor
        actor_input = Input(shape=self.observation_space_shape)
        layer_1 = Dense(240, activation='relu')(actor_input)
        layer_2 = Dense(480, activation='relu')(layer_1)
        layer_3 = Dense(240, activation='relu')(layer_2)
        output = Dense(self.action_space.shape[0], activation='relu')(layer_3)

        # Put them altogether in a model
        model = Model(input=actor_input, output=output)
        adam = Adam(lr=self.learning_rate)
        model.compile(loss='mse', optimizer=adam)

        # return the model and Input
        return actor_input, model

    def _train_actor(self, samples):
        pass

    def _update_actor(self):
        pass

    '''
    Critic Functions
    '''
    def create_actor(self):
        pass

    def _train_critic(self, samples):
        pass

    def _update_critic(self):
        pass


    '''
    Helper Functions
    '''
    def update(self):
        self._update_actor()
        self._update_critic()

    def train(self):
        pass

    def remember(self, curr_state, action, reward, new_state):
        self.memory.append([curr_state, action, reward, new_state])

    def act(self, curr_state):
        pass
