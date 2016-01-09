#
#   containers.py
#   SwiftSTL
# 
#   The MIT License (MIT)
# 
#   Copyright (c) 2016 Greg Omelaenko
# 
#   Permission is hereby granted, free of charge, to any person obtaining a copy
#   of this software and associated documentation files (the "Software"), to deal
#   in the Software without restriction, including without limitation the rights
#   to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
#   copies of the Software, and to permit persons to whom the Software is
#   furnished to do so, subject to the following conditions:
# 
#   The above copyright notice and this permission notice shall be included in all
#   copies or substantial portions of the Software.
# 
#   THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#   IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#   FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#   AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#   LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#   OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#   SOFTWARE.
# 

import re
from collections import namedtuple

def camel(name):
    return name.title().replace('_', '')

def argscall(args):
    return re.sub(r".+?\W([A-Za-z0-9$_]+)(, |$)", r"\1\2", args)

Func = namedtuple('Func', 'type name args vattrs body')

types = {
    'deque': [
        Func('const void *', 'get_index', 'size_t index', 'const', '{ return this->v[index]._; }'),
        Func('void *', 'index', 'size_t index', '', '{ return this->v[index]._; }'),
        Func('size_t', 'size', '', 'const', '{ return this->v.size(); }'),
        Func('void', 'clear', '', '', '{ this->v.clear(); }'),
        Func('void', 'insert', 'size_t index, const void *values, size_t count', '', '{ this->v.insert(this->v.begin() + index, (const element *)values, (const element *)values + count); }'),
        Func('void', 'erase', 'size_t index, size_t count', '', '{ this->v.erase(this->v.begin() + index, this->v.begin() + index + count); }'),
        Func('void', 'push_back', 'const void *value', '', '{ this->v.push_back(*(const element *)value); }'),
        Func('void', 'pop_back', '', '', '{ this->v.pop_back(); }'),
        Func('void', 'push_front', 'const void *value', '', '{ this->v.push_front(*(const element *)value); }'),
        Func('void', 'pop_front', '', '', '{ this->v.pop_front(); }')
    ]
}