{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 70,
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import collections\n",
    "from scipy.spatial import distance"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['in comparison to dogs, cats have not undergone major changes during the domestication process.', 'as cat simply catenates streams of bytes, it can be also used to concatenate binary files, where it will just concatenate sequence of bytes.', 'a common interactive use of cat for a single file is to output the content of a file to standard output.', 'cats can hear sounds too faint or too high in frequency for human ears, such as those made by mice and other small animals.', 'in one, people deliberately tamed cats in a process of artificial selection, as they were useful predators of vermin.', 'the domesticated cat and its closest wild ancestor are both diploid organisms that possess 38 chromosomes and roughly 20,000 genes.', 'domestic cats are similar in size to the other members of the genus felis, typically weighing between 4 and 5 kg (8.8 and 11.0 lb).', 'however, if the output is piped or redirected, cat is unnecessary.', 'cat with one named file is safer where human error is a concern - one wrong use of the default redirection symbol \">\" instead of \"<\" (often adjacent on keyboards) may permanently delete the file you were just needing to read.', 'in terms of legibility, a sequence of commands starting with cat and connected by pipes has a clear left-to-right flow of information.', 'cat command is one of the basic commands that you learned when you started in the unix / linux world.', 'using cat command, the lines received from stdin can be redirected to a new file using redirection symbols.', 'when you type simply cat command without any arguments, it just receives the stdin content and displays it in the stdout.', 'leopard was released on october 26, 2007 as the successor of tiger (version 10.4), and is available in two editions.', 'according to apple, leopard contains over 300 changes and enhancements over its predecessor, mac os x tiger.', 'as of mid 2010, some apple computers have firmware factory installed which will no longer allow installation of mac os x leopard.', 'since apple moved to using intel processors in their computers, the osx86 community has developed and now also allows mac os x tiger and later releases to be installed on non-apple x86-based computers.', \"os x mountain lion was released on july 25, 2012 for purchase and download through apple's mac app store, as part of a switch to releasing os x versions online and every year.\", 'apple has released a small patch for the three most recent versions of safari running on os x yosemite, mavericks, and mountain lion.', 'the mountain lion release marks the second time apple has offered an incremental upgrade, rather than releasing a new cat entirely.', \"mac os x mountain lion installs in place, so you won't need to create a separate disk or run the installation off an external drive.\", \"the fifth major update to mac os x, leopard, contains such a mountain of features - more than 300 by apple's count.\"]\n"
     ]
    }
   ],
   "source": [
    "texts = []\n",
    "with open ('./_3a8d746cf4d86fba2f31586f239d11fd_sentences.txt') as file:\n",
    "    for line in file:\n",
    "        texts.append(line.lower())\n",
    "texts = [text.rstrip() for text in texts]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[['in', 'comparison', 'to', 'dogs', 'cats', 'have', 'not', 'undergone', 'major', 'changes', 'during', 'the', 'domestication', 'process'], ['as', 'cat', 'simply', 'catenates', 'streams', 'of', 'bytes', 'it', 'can', 'be', 'also', 'used', 'to', 'concatenate', 'binary', 'files', 'where', 'it', 'will', 'just', 'concatenate', 'sequence', 'of', 'bytes'], ['a', 'common', 'interactive', 'use', 'of', 'cat', 'for', 'a', 'single', 'file', 'is', 'to', 'output', 'the', 'content', 'of', 'a', 'file', 'to', 'standard', 'output'], ['cats', 'can', 'hear', 'sounds', 'too', 'faint', 'or', 'too', 'high', 'in', 'frequency', 'for', 'human', 'ears', 'such', 'as', 'those', 'made', 'by', 'mice', 'and', 'other', 'small', 'animals'], ['in', 'one', 'people', 'deliberately', 'tamed', 'cats', 'in', 'a', 'process', 'of', 'artificial', 'selection', 'as', 'they', 'were', 'useful', 'predators', 'of', 'vermin'], ['the', 'domesticated', 'cat', 'and', 'its', 'closest', 'wild', 'ancestor', 'are', 'both', 'diploid', 'organisms', 'that', 'possess', 'chromosomes', 'and', 'roughly', 'genes'], ['domestic', 'cats', 'are', 'similar', 'in', 'size', 'to', 'the', 'other', 'members', 'of', 'the', 'genus', 'felis', 'typically', 'weighing', 'between', 'and', 'kg', 'and', 'lb'], ['however', 'if', 'the', 'output', 'is', 'piped', 'or', 'redirected', 'cat', 'is', 'unnecessary'], ['cat', 'with', 'one', 'named', 'file', 'is', 'safer', 'where', 'human', 'error', 'is', 'a', 'concern', 'one', 'wrong', 'use', 'of', 'the', 'default', 'redirection', 'symbol', 'instead', 'of', 'often', 'adjacent', 'on', 'keyboards', 'may', 'permanently', 'delete', 'the', 'file', 'you', 'were', 'just', 'needing', 'to', 'read'], ['in', 'terms', 'of', 'legibility', 'a', 'sequence', 'of', 'commands', 'starting', 'with', 'cat', 'and', 'connected', 'by', 'pipes', 'has', 'a', 'clear', 'left', 'to', 'right', 'flow', 'of', 'information'], ['cat', 'command', 'is', 'one', 'of', 'the', 'basic', 'commands', 'that', 'you', 'learned', 'when', 'you', 'started', 'in', 'the', 'unix', 'linux', 'world'], ['using', 'cat', 'command', 'the', 'lines', 'received', 'from', 'stdin', 'can', 'be', 'redirected', 'to', 'a', 'new', 'file', 'using', 'redirection', 'symbols'], ['when', 'you', 'type', 'simply', 'cat', 'command', 'without', 'any', 'arguments', 'it', 'just', 'receives', 'the', 'stdin', 'content', 'and', 'displays', 'it', 'in', 'the', 'stdout'], ['leopard', 'was', 'released', 'on', 'october', 'as', 'the', 'successor', 'of', 'tiger', 'version', 'and', 'is', 'available', 'in', 'two', 'editions'], ['according', 'to', 'apple', 'leopard', 'contains', 'over', 'changes', 'and', 'enhancements', 'over', 'its', 'predecessor', 'mac', 'os', 'x', 'tiger'], ['as', 'of', 'mid', 'some', 'apple', 'computers', 'have', 'firmware', 'factory', 'installed', 'which', 'will', 'no', 'longer', 'allow', 'installation', 'of', 'mac', 'os', 'x', 'leopard'], ['since', 'apple', 'moved', 'to', 'using', 'intel', 'processors', 'in', 'their', 'computers', 'the', 'osx', 'community', 'has', 'developed', 'and', 'now', 'also', 'allows', 'mac', 'os', 'x', 'tiger', 'and', 'later', 'releases', 'to', 'be', 'installed', 'on', 'non', 'apple', 'x', 'based', 'computers'], ['os', 'x', 'mountain', 'lion', 'was', 'released', 'on', 'july', 'for', 'purchase', 'and', 'download', 'through', 'apple', 's', 'mac', 'app', 'store', 'as', 'part', 'of', 'a', 'switch', 'to', 'releasing', 'os', 'x', 'versions', 'online', 'and', 'every', 'year'], ['apple', 'has', 'released', 'a', 'small', 'patch', 'for', 'the', 'three', 'most', 'recent', 'versions', 'of', 'safari', 'running', 'on', 'os', 'x', 'yosemite', 'mavericks', 'and', 'mountain', 'lion'], ['the', 'mountain', 'lion', 'release', 'marks', 'the', 'second', 'time', 'apple', 'has', 'offered', 'an', 'incremental', 'upgrade', 'rather', 'than', 'releasing', 'a', 'new', 'cat', 'entirely'], ['mac', 'os', 'x', 'mountain', 'lion', 'installs', 'in', 'place', 'so', 'you', 'won', 't', 'need', 'to', 'create', 'a', 'separate', 'disk', 'or', 'run', 'the', 'installation', 'off', 'an', 'external', 'drive'], ['the', 'fifth', 'major', 'update', 'to', 'mac', 'os', 'x', 'leopard', 'contains', 'such', 'a', 'mountain', 'of', 'features', 'more', 'than', 'by', 'apple', 's', 'count']]\n"
     ]
    }
   ],
   "source": [
    "token_texts = []\n",
    "for i in texts:\n",
    "    t = re.split('[^a-z]', i)\n",
    "    t = [x for x in t if x]\n",
    "    token_texts.append(t)\n",
    "print(token_texts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "['in', 'comparison', 'to', 'dogs', 'cats', 'have', 'not', 'undergone', 'major', 'changes', 'during', 'the', 'domestication', 'process', 'as', 'cat', 'simply', 'catenates', 'streams', 'of', 'bytes', 'it', 'can', 'be', 'also', 'used', 'to', 'concatenate', 'binary', 'files', 'where', 'it', 'will', 'just', 'concatenate', 'sequence', 'of', 'bytes', 'a', 'common', 'interactive', 'use', 'of', 'cat', 'for', 'a', 'single', 'file', 'is', 'to', 'output', 'the', 'content', 'of', 'a', 'file', 'to', 'standard', 'output', 'cats', 'can', 'hear', 'sounds', 'too', 'faint', 'or', 'too', 'high', 'in', 'frequency', 'for', 'human', 'ears', 'such', 'as', 'those', 'made', 'by', 'mice', 'and', 'other', 'small', 'animals', 'in', 'one', 'people', 'deliberately', 'tamed', 'cats', 'in', 'a', 'process', 'of', 'artificial', 'selection', 'as', 'they', 'were', 'useful', 'predators', 'of', 'vermin', 'the', 'domesticated', 'cat', 'and', 'its', 'closest', 'wild', 'ancestor', 'are', 'both', 'diploid', 'organisms', 'that', 'possess', 'chromosomes', 'and', 'roughly', 'genes', 'domestic', 'cats', 'are', 'similar', 'in', 'size', 'to', 'the', 'other', 'members', 'of', 'the', 'genus', 'felis', 'typically', 'weighing', 'between', 'and', 'kg', 'and', 'lb', 'however', 'if', 'the', 'output', 'is', 'piped', 'or', 'redirected', 'cat', 'is', 'unnecessary', 'cat', 'with', 'one', 'named', 'file', 'is', 'safer', 'where', 'human', 'error', 'is', 'a', 'concern', 'one', 'wrong', 'use', 'of', 'the', 'default', 'redirection', 'symbol', 'instead', 'of', 'often', 'adjacent', 'on', 'keyboards', 'may', 'permanently', 'delete', 'the', 'file', 'you', 'were', 'just', 'needing', 'to', 'read', 'in', 'terms', 'of', 'legibility', 'a', 'sequence', 'of', 'commands', 'starting', 'with', 'cat', 'and', 'connected', 'by', 'pipes', 'has', 'a', 'clear', 'left', 'to', 'right', 'flow', 'of', 'information', 'cat', 'command', 'is', 'one', 'of', 'the', 'basic', 'commands', 'that', 'you', 'learned', 'when', 'you', 'started', 'in', 'the', 'unix', 'linux', 'world', 'using', 'cat', 'command', 'the', 'lines', 'received', 'from', 'stdin', 'can', 'be', 'redirected', 'to', 'a', 'new', 'file', 'using', 'redirection', 'symbols', 'when', 'you', 'type', 'simply', 'cat', 'command', 'without', 'any', 'arguments', 'it', 'just', 'receives', 'the', 'stdin', 'content', 'and', 'displays', 'it', 'in', 'the', 'stdout', 'leopard', 'was', 'released', 'on', 'october', 'as', 'the', 'successor', 'of', 'tiger', 'version', 'and', 'is', 'available', 'in', 'two', 'editions', 'according', 'to', 'apple', 'leopard', 'contains', 'over', 'changes', 'and', 'enhancements', 'over', 'its', 'predecessor', 'mac', 'os', 'x', 'tiger', 'as', 'of', 'mid', 'some', 'apple', 'computers', 'have', 'firmware', 'factory', 'installed', 'which', 'will', 'no', 'longer', 'allow', 'installation', 'of', 'mac', 'os', 'x', 'leopard', 'since', 'apple', 'moved', 'to', 'using', 'intel', 'processors', 'in', 'their', 'computers', 'the', 'osx', 'community', 'has', 'developed', 'and', 'now', 'also', 'allows', 'mac', 'os', 'x', 'tiger', 'and', 'later', 'releases', 'to', 'be', 'installed', 'on', 'non', 'apple', 'x', 'based', 'computers', 'os', 'x', 'mountain', 'lion', 'was', 'released', 'on', 'july', 'for', 'purchase', 'and', 'download', 'through', 'apple', 's', 'mac', 'app', 'store', 'as', 'part', 'of', 'a', 'switch', 'to', 'releasing', 'os', 'x', 'versions', 'online', 'and', 'every', 'year', 'apple', 'has', 'released', 'a', 'small', 'patch', 'for', 'the', 'three', 'most', 'recent', 'versions', 'of', 'safari', 'running', 'on', 'os', 'x', 'yosemite', 'mavericks', 'and', 'mountain', 'lion', 'the', 'mountain', 'lion', 'release', 'marks', 'the', 'second', 'time', 'apple', 'has', 'offered', 'an', 'incremental', 'upgrade', 'rather', 'than', 'releasing', 'a', 'new', 'cat', 'entirely', 'mac', 'os', 'x', 'mountain', 'lion', 'installs', 'in', 'place', 'so', 'you', 'won', 't', 'need', 'to', 'create', 'a', 'separate', 'disk', 'or', 'run', 'the', 'installation', 'off', 'an', 'external', 'drive', 'the', 'fifth', 'major', 'update', 'to', 'mac', 'os', 'x', 'leopard', 'contains', 'such', 'a', 'mountain', 'of', 'features', 'more', 'than', 'by', 'apple', 's', 'count']\n",
      "484\n"
     ]
    }
   ],
   "source": [
    "full = []\n",
    "for i in token_texts:\n",
    "    full += i\n",
    "print(full)\n",
    "print(len(full))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {
    "collapsed": true
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Counter({'the': 20, 'of': 19, 'to': 14, 'and': 14, 'a': 13, 'in': 11, 'cat': 10, 'x': 9, 'apple': 8, 'os': 8, 'is': 7, 'as': 6, 'mac': 6, 'file': 5, 'on': 5, 'you': 5, 'mountain': 5, 'cats': 4, 'it': 4, 'for': 4, 'one': 4, 'has': 4, 'leopard': 4, 'lion': 4, 'can': 3, 'be': 3, 'just': 3, 'output': 3, 'or': 3, 'by': 3, 'command': 3, 'using': 3, 'released': 3, 'tiger': 3, 'computers': 3, 'have': 2, 'major': 2, 'changes': 2, 'process': 2, 'simply': 2, 'bytes': 2, 'also': 2, 'concatenate': 2, 'where': 2, 'will': 2, 'sequence': 2, 'use': 2, 'content': 2, 'too': 2, 'human': 2, 'such': 2, 'other': 2, 'small': 2, 'were': 2, 'its': 2, 'are': 2, 'that': 2, 'redirected': 2, 'with': 2, 'redirection': 2, 'commands': 2, 'when': 2, 'stdin': 2, 'new': 2, 'was': 2, 'contains': 2, 'over': 2, 'installed': 2, 'installation': 2, 's': 2, 'releasing': 2, 'versions': 2, 'an': 2, 'than': 2, 'comparison': 1, 'dogs': 1, 'not': 1, 'undergone': 1, 'during': 1, 'domestication': 1, 'catenates': 1, 'streams': 1, 'used': 1, 'binary': 1, 'files': 1, 'common': 1, 'interactive': 1, 'single': 1, 'standard': 1, 'hear': 1, 'sounds': 1, 'faint': 1, 'high': 1, 'frequency': 1, 'ears': 1, 'those': 1, 'made': 1, 'mice': 1, 'animals': 1, 'people': 1, 'deliberately': 1, 'tamed': 1, 'artificial': 1, 'selection': 1, 'they': 1, 'useful': 1, 'predators': 1, 'vermin': 1, 'domesticated': 1, 'closest': 1, 'wild': 1, 'ancestor': 1, 'both': 1, 'diploid': 1, 'organisms': 1, 'possess': 1, 'chromosomes': 1, 'roughly': 1, 'genes': 1, 'domestic': 1, 'similar': 1, 'size': 1, 'members': 1, 'genus': 1, 'felis': 1, 'typically': 1, 'weighing': 1, 'between': 1, 'kg': 1, 'lb': 1, 'however': 1, 'if': 1, 'piped': 1, 'unnecessary': 1, 'named': 1, 'safer': 1, 'error': 1, 'concern': 1, 'wrong': 1, 'default': 1, 'symbol': 1, 'instead': 1, 'often': 1, 'adjacent': 1, 'keyboards': 1, 'may': 1, 'permanently': 1, 'delete': 1, 'needing': 1, 'read': 1, 'terms': 1, 'legibility': 1, 'starting': 1, 'connected': 1, 'pipes': 1, 'clear': 1, 'left': 1, 'right': 1, 'flow': 1, 'information': 1, 'basic': 1, 'learned': 1, 'started': 1, 'unix': 1, 'linux': 1, 'world': 1, 'lines': 1, 'received': 1, 'from': 1, 'symbols': 1, 'type': 1, 'without': 1, 'any': 1, 'arguments': 1, 'receives': 1, 'displays': 1, 'stdout': 1, 'october': 1, 'successor': 1, 'version': 1, 'available': 1, 'two': 1, 'editions': 1, 'according': 1, 'enhancements': 1, 'predecessor': 1, 'mid': 1, 'some': 1, 'firmware': 1, 'factory': 1, 'which': 1, 'no': 1, 'longer': 1, 'allow': 1, 'since': 1, 'moved': 1, 'intel': 1, 'processors': 1, 'their': 1, 'osx': 1, 'community': 1, 'developed': 1, 'now': 1, 'allows': 1, 'later': 1, 'releases': 1, 'non': 1, 'based': 1, 'july': 1, 'purchase': 1, 'download': 1, 'through': 1, 'app': 1, 'store': 1, 'part': 1, 'switch': 1, 'online': 1, 'every': 1, 'year': 1, 'patch': 1, 'three': 1, 'most': 1, 'recent': 1, 'safari': 1, 'running': 1, 'yosemite': 1, 'mavericks': 1, 'release': 1, 'marks': 1, 'second': 1, 'time': 1, 'offered': 1, 'incremental': 1, 'upgrade': 1, 'rather': 1, 'entirely': 1, 'installs': 1, 'place': 1, 'so': 1, 'won': 1, 't': 1, 'need': 1, 'create': 1, 'separate': 1, 'disk': 1, 'run': 1, 'off': 1, 'external': 1, 'drive': 1, 'fifth': 1, 'update': 1, 'features': 1, 'more': 1, 'count': 1})\n",
      "254\n"
     ]
    }
   ],
   "source": [
    "counter = collections.Counter(full)\n",
    "print(counter)\n",
    "print(len(counter))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 63,
   "metadata": {},
   "outputs": [],
   "source": [
    "dictionary = list(dict(counter).keys())\n",
    "A = np.zeros((len(token_texts), len(dictionary)))\n",
    "for i in range(len(token_texts)):\n",
    "    count = collections.Counter(token_texts[i])\n",
    "    for j in range(len(dictionary)):\n",
    "        A[i,j] = count[dictionary[j]]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 100,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "6 4\n"
     ]
    }
   ],
   "source": [
    "dist = [[] for i in range(len(token_texts)-1)]\n",
    "for i in range(1, len(token_texts)):\n",
    "    dist[i-1].append(distance.cosine(A[0], A[i]))\n",
    "    dist[i-1].append(i)\n",
    "    \n",
    "k = sorted(dist)[:2]\n",
    "l = str(k[0][1]) + ' ' + str(k[1][1])\n",
    "print(l)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 101,
   "metadata": {},
   "outputs": [],
   "source": [
    "with open('file.txt', 'w') as file:\n",
    "    file.write(l)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Задание 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 331,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[ 4.12454868 -0.87233182]\n",
      "[ 3.57839130e+00 -3.29714150e-01  3.53971617e-03]\n",
      "[ 4.36264154 -1.29552587  0.19333685 -0.00823565]\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "<function matplotlib.pyplot.show(*args, **kw)>"
      ]
     },
     "execution_count": 331,
     "metadata": {},
     "output_type": "execute_result"
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "import math\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "from scipy import linalg\n",
    "\n",
    "\n",
    "def f(x):\n",
    "    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)\n",
    "A = np.array([[1,1], [1,4]])\n",
    "b = [f(1),f(15)]\n",
    "z = np.linalg.solve(A, b)\n",
    "print (z)\n",
    "\n",
    "\n",
    "\n",
    "def f1(x):\n",
    "    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)\n",
    "A = np.array([[1,1,1], [1,4,16], [1,10,100]])\n",
    "b = [f(1),f(8),f(15)]\n",
    "z1 = np.linalg.solve(A, b)\n",
    "print (z1)\n",
    "\n",
    "\n",
    "\n",
    "def f2(x):\n",
    "    return np.sin(x/5.) * np.exp(x/10.) + 5. * np.exp(-x/2.)\n",
    "A = np.array([[1, 1, 1, 1], [1, 4, 16, 64], [1, 10, 100, 1000], [1, 15, 225, 3375]])\n",
    "b = [f(1),f(4),f(10),f(15)]\n",
    "z2 = np.linalg.solve(A, b)\n",
    "print (z2)\n",
    "\n",
    "%matplotlib inline\n",
    "from matplotlib import pylab as plt\n",
    "x = np.arange(1, 15, 0.1)\n",
    "y = f2(x)\n",
    "plt.plot (x, y)\n",
    "plt.show"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
