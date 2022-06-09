class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        
        # default dict: won't return key error if key doesn't exist in dict
        from collections import defaultdict
        
        # key: course
        # val: list of courses I can take, after taking the key as pre req
        courseDict = defaultdict(list)
        
        # fill the dict
        for course, prereq in prerequisites:
            courseDict[prereq].append(course)
            
        # a list representing each course - True if checked not cyclic, False if not checked yet
        # if checked to be cyclic - return function as can't finish
        checked = [False] * numCourses
        # a list representing each course - True if active on current path checking for a cycle, False if not active
        path = [False] * numCourses
        
        
        def isCyclic(i):
            """
            type i: int, idx of course
            rtype: bool, True if course i belongs to a cycle, False otherwise
            """
            # already checked. don't need to check again
            if checked[i]:
                return False
            
            # already on the path - create a cycle
            if path[i]:
                return True
            
            # add this course on path
            path[i] = True
            
            # check the children of this course
            children = courseDict[i]
            for child in children:
                if isCyclic(child):
                    return True
            
            # children all checked. this course is checked
            checked[i] = True
            # take this course off the path - finish checking this path
            path[i] = False
            
            # not cyclic
            return False
           
        
        # check each course
        for i in range(numCourses):
            
            # pre reqs are cyclic. can't finish all classes
            if isCyclic(i):
                return False
            
        # all checked. not cyclic
        return True
            
            