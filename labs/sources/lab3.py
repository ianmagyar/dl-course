# -*- coding: utf-8 -*-
import random
import gym
import numpy as np
from collections import deque
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

EPISODES = 50


class DQNAgent:
    def __init__(self, state_size, action_size):
        # number of parameters describing the state
        self.state_size = state_size
        # number of possible actions for the agent
        self.action_size = action_size

        # memory of experiences
        self.memory = deque(maxlen=2000)

        # discount rate:
        # 0 - consider only current rewards
        # 1 - go for long-term high reward
        self.gamma = 0.95

        # learning rate:
        # 0 - do not learn anything new
        # 1 - forget all old information
        self.learning_rate = 0.001

        # probability of random action selection
        self.epsilon = 1.0
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995

        self.model = self._build_model()

    def _build_model(self):
        # Neural Net for Deep-Q learning Model
        model = Sequential()
        # TODO: add layers

        return model

    def remember(self, state, action, reward, next_state, done):
        # TODO: remember experience
        pass

    def act(self, state):
        # random action selection with probability self.epsilon
        # TODO:

        # otherwise select the action with the highest Q value
        act_values = self.model.predict(state)
        return np.argmax(act_values[0])

    def replay(self, batch_size):
        # select random samples from memory
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            # compute new target value to be the output of the network
            target = reward
            if not done:
                target = (reward + self.gamma *
                          np.amax(self.model.predict(next_state)[0]))
            # get current output value and update the value for the action
            target_f = self.model.predict(state)
            target_f[0][action] = target
            # train the model
            self.model.fit(state, target_f, epochs=1, verbose=0)
        # update epsilon to minimize exploration on the long term
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

    def load(self, name):
        self.model.load_weights(name)

    def save(self, name):
        self.model.save_weights(name)


if __name__ == "__main__":
    # load training environment and get parameters
    env = gym.make('CartPole-v1')
    state_size = env.observation_space.shape[0]
    action_size = env.action_space.n

    agent = DQNAgent(state_size, action_size)
    # agent.load("./save/cartpole-dqn.h5")
    done = False
    batch_size = 32

    for e in range(EPISODES):
        # at each episode, reset environment to starting position
        state = env.reset()
        state = np.reshape(state, [1, state_size])
        for time in range(500):
            # show game graphics
            env.render()

            # select action, observe environment, calculate reward
            action = agent.act(state)
            next_state, reward, done, _ = env.step(action)
            reward = reward if not done else -10
            next_state = np.reshape(next_state, [1, state_size])

            # save experience and update current state
            agent.remember(state, action, reward, next_state, done)
            state = next_state
            if done:
                # if game ended, finish episode
                print("episode: {}/{}, score: {}, e: {:.2}"
                      .format(e, EPISODES, time, agent.epsilon))
                break
            if len(agent.memory) > batch_size:
                # if enough experience is available, replay
                agent.replay(batch_size)

    # agent.save("./save/cartpole-dqn.h5")
