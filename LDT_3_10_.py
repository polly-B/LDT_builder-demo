    #%$ thing that need doing:
#1.Figure out how to include button box press to end trial
#2.Figure out how to take out resp?!?!?!

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy2 Experiment Builder (v1.84.2),
    on Mon 24 Jul 13:18:29 2017
If you publish work using this script please cite the PsychoPy publications:
    Peirce, JW (2007) PsychoPy - Psychophysics software in Python.
        Journal of Neuroscience Methods, 162(1-2), 8-13.
    Peirce, JW (2009) Generating stimuli for neuroscience using PsychoPy.
        Frontiers in Neuroinformatics, 2:10. doi: 10.3389/neuro.11.010.2008
"""

from __future__ import absolute_import, division
from psychopy import locale_setup, gui, visual, core, data, event, logging, sound, hardware
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)
import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle
import os  # handy system and path functions
import sys  # to get file system encoding
#for button box
import serial
import serial.tools.list_ports
import time, sys, os#, pylab
useButtonBox = True
triggerTest = False
# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__)).decode(sys.getfilesystemencoding())
os.chdir(_thisDir)

# Store info about the experiment session
expName = 'LDT2'  # from the Builder filename that created this script
expInfo = {u'session': u'01', u'participant': u''}
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data' + os.sep + '%s_%s' % (expInfo['participant'], expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath=u'/Users/pollybarr/Documents/LDT_builder demo/LDT2.psyexp',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp

# Start Code - component code to be run before the window creation

#define button box
def initialiseButtonBox():
    serialPorts = serial.tools.list_ports.comports() #List of connected items
    devices = [port.description for port in serialPorts] #description attributes of connected items
    try: #is there an arduino box connected?
        boxPortIndex = devices.index('Arduino Uno') 
        buttonBox = serial.Serial(serialPorts[boxPortIndex].device, timeout=1, baudrate = 9600, write_timeout=1) #if there is, set it up
    except ValueError:
        print('Button box not found')
        return None
    buttonBox.in_waiting
    core.wait(1)
    time.sleep(1)
    line = buttonBox.readline()
    print('line is', line)
    if line == 'Initialised\r\n':
        print('buttonBox', line.split('\r\n')[0][1])
        buttonBox.write(b'p')
        line = buttonBox.readline()
    if line == 'waiting for input\r\n':
        print(line)
        return buttonBox
    else:
        print('Failed to initialise buttonBox')
        return None
if useButtonBox:
    buttonBox = initialiseButtonBox()
    buttonBox.in_waiting #The box can be tricky. You need to send it something in order for it to start responding to .write() commands. This just checks the number of lines in the output buffer.
    core.wait(3) #Wait for a couple of seconds. The box is kinda slow
    buttonBox.reset_input_buffer()
    nTriggerTestTrials = 0
    nTriggeredTestTrials = 0
    nNoTrigger = 0
    nTriggerTrials = 0
    nDone =0
    totalTrials = 0
    if triggerTest:
        nTriggerTestTrials += 1
win = visual.Window(
    size=(1440, 900), fullscr=True, screen=0,
    allowGUI=False, allowStencil=False,
    monitor='testMonitor', color='black', colorSpace='rgb',
    blendMode='avg', useFBO=True,
    units='norm')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess

# Initialize components for Routine "instructPractice"
instructPracticeClock = core.Clock()
instr1 = visual.TextStim(win=win, name='instr1',
    text="Ready for a practice\nYou will see a fixation cross with two items either side\nChoose '1' if no real words\nChoose '2' if one real word\nChoose '3' if two real words\nPress any key to continue",
    font='Courier',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
buttonBoxTrigger = [True]
trialClock = core.Clock()
buttonBoxStimuli = visual.Circle(win,fillColorSpace='rgb',fillColor=(1,1,1),radius=.02 ,pos=(-.625,-.47),units='height'); #Stimulus to trigger button box clock.
itemL = visual.TextStim(win=win, name='itemL',
    text='default text',
    font='courier',
    pos=[ 0,-0.20], height=0.15, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=0.0);
itemR = visual.TextStim(win=win, name='itemR',
    text='default text',
    font='courier',
    pos=(0,0.20), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);
#buttonBox = None
for n in range(10):
    try:
        # doesn't always work first time!
        serialPorts = serial.tools.list_ports.comports() #List of connected items
        devices = [port.description for port in serialPorts] #description attributes of connected items
        try: #is there an arduino box connected?
            boxPortIndex = devices.index('Arduino Uno') 
            buttonBox = serial.Serial(serialPorts[boxPortIndex].device, timeout=1, baudrate = 9600, write_timeout=1) #if there is, set it up
        except ValueError:
            print('Button box not found')
            return None
            buttonBox.in_waiting
            core.wait(2)
            time.sleep(1)
            line = buttonBox.readline()
            print('line is', line)
            if line == 'Initialised\r\n':
                print('buttonBox', line.split('\r\n')[0][1])
                buttonBox.write(b'p')
                line = buttonBox.readline()
            if line == 'waiting for input\r\n':
                print(line)
                return buttonBox
            else:
                print('Failed to initialise buttonBox')
                return None
            buttonBox.Clock = core.Clock()
# Initialize components for Routine "feedback"
feedbackClock = core.Clock()
#msg variable just needs some value at start
msg=''
feedback_2 = visual.TextStim(win=win, name='feedback_2',
    text='default text',
    font=u'Arial',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1,1,1], colorSpace='rgb', opacity=1,
    depth=-1.0);
# Initialize components for Routine "instruct"
instructClock = core.Clock()
instrText = visual.TextStim(win=win, name='instrText',
    text="OK. Ready for the real thing?\n\nChoose '1' if no real words\nChoose '2' if one real word\nChoose '3' if two real words\nPress any key to continue",
    font='Courier',
    pos=[0, 0], height=0.1, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Initialize components for Routine "trial"
buttonBoxStimuli = visual.Circle(win,fillColorSpace='rgb',opacity=  1.0, fillColor=(1,1,1),radius=.02 ,pos=(-.625,-.47),units='height'); #Stimulus to trigger button box clock.
buttonBoxTrigger = [True]
trialClock = core.Clock()
trialClock = core.Clock()
itemL = visual.TextStim(win=win, name='itemL',
    text='default text',
    font='courier',
    pos=[ 0,-0.20], height=0.15, wrapWidth=None, ori=0, 
    color='White', colorSpace='rgb', opacity=1,
    depth=0.0);
itemR = visual.TextStim(win=win, name='itemR',
    text='default text',
    font='courier',
    pos=(0,0.20), height=0.15, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-2.0);
fixation = visual.TextStim(win=win, name='fixation',
    text='+',
    font='Arial',
    pos=(0, 0), height=0.2, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-3.0);
blank = visual.TextStim(win=win, name='blank',
    text=None,
    font='Arial',
    pos=(0, 0), height=0.1, wrapWidth=None, ori=0, 
    color='white', colorSpace='rgb', opacity=1,
    depth=-4.0);

# Initialize components for Routine "thanks"
thanksClock = core.Clock()
thanksText = visual.TextStim(win=win, name='thanksText',
    text='This is the end of the experiment.\n\nThanks!',
    font='arial',
    pos=[0, 0], height=0.2, wrapWidth=None, ori=0, 
    color=[1, 1, 1], colorSpace='rgb', opacity=1,
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "instructPractice"-------
t = 0
instructPracticeClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructPracticeComponents = [instr1, ready1]
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instructPractice"-------
while continueRoutine:
    # get current time
    t = instructPracticeClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instr1* updates
    if t >= 0.0 and instr1.status == NOT_STARTED:
        # keep track of start time/frame for later
        instr1.tStart = t
        instr1.frameNStart = frameN  # exact frame index
        instr1.setAutoDraw(True)
    
    # *ready1* updates
    if t >= 0.0 and ready1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready1.tStart = t
        ready1.frameNStart = frameN  # exact frame index
        ready1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if useButtonBox:
            if totalTrials > 0:
                continueRoutine = False
        if len(theseKeys) > 0:  # at least one key was pressed
                continueRoutine = False
            # a response ends the routine

    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructPracticeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()
        win.clearBuffer()

# -------Ending Routine "instructPractice"-------
for thisComponent in instructPracticeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instructPractice" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions1.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values

# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice.keys():
        exec(paramName + '= thisPractice.' + paramName)

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice.keys():
            exec(paramName + '= thisPractice.' + paramName)
    
    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    if useButtonBox and not triggerTest:
        buttonBox.write(b'b') #start looking for a flash of light to trigger the clock
    elif useButtonBox and triggerTest:
        buttonBox.write(b'd') #if we're testing the trigger. Run the trigger test. Outputs "Triggered\r\n" if the photo cell is triggered
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    itemL.setText(left)
    resp = event.BuilderKeyResponse()
    itemR.setText(right)
    buttonBox.keys = []  # to store response values
    buttonBox.rt = []
    # keep track of which components have finished
    trialComponents = [fixation, blank,itemL, itemR, resp, buttonBox]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)

        # update/draw components on each fram        

        # *fixation* updates
        if t >= 0.5 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.5 + 0.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *blank* updates
        if t >= 0.0 and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank.status == STARTED and t >= frameRemains:
            blank.setAutoDraw(False)
            
        # *itemR* updates
        if t >= 1 and itemR.status == NOT_STARTED:
            # keep track of start time/frame for later
            itemR.tStart = t
            itemR.frameNStart = frameN  # exact frame index
            itemR.setAutoDraw(True);buttonBoxStimuli.draw()
        frameRemains = 1.0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if itemR.status == STARTED and t >= frameRemains:
            itemR.setAutoDraw(False)
        
        # *itemL* updates
        if t >= 1 and itemL.status == NOT_STARTED:
            # keep track of start time/frame for later
            itemL.tStart = t
            itemL.frameNStart = frameN  # exact frame index
            itemL.setAutoDraw(True)
        frameRemains = 1.0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if itemL.status == STARTED and t >= frameRemains:
            itemL.setAutoDraw(False)
        
        # *resp* updates
        if t >= 1 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp.keys == []:  # then this was the first keypress
                    resp.keys = theseKeys[0]  # just the first key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
        # *buttonBox* updates
        if useButtonBox:
            if t >= 1 and buttonBox.status == NOT_STARTED:
                # keep track of start time/frame for later
                buttonBox.tStart = t
                buttonBox.frameNStart = frameN  # exact frame index
                buttonBox.status = STARTED
                buttonBox.clock.reset()  # now t=0
                # clear buttonBox responses (in a loop - the Cedrus own function doesn't work well)
                buttonBox.poll_for_response()
                while len(buttonBox.response_queue):
                    buttonBox.clear_response_queue()
                    buttonBox.poll_for_response() #often there are more resps waiting!
            if buttonBox.status == STARTED:
                theseKeys=[]
    #            theseRTs=[]
                # check for key presses
                buttonBox.poll_for_response()
                while len(buttonBox.response_queue):
                    evt = buttonBox.get_next_response()
                    if evt['key'] not in ['123']:
                        continue  # we don't care about this key
                    if evt['pressed']:
                      theseKeys.append(evt['key'])
                      theseRTs.append(buttonBox.clock.getTime())
                    buttonBox.poll_for_response()
                buttonBox.clear_response_queue()  # don't process again
                if len(theseKeys) > 0:  # at least one key was pressed
                    if buttonBox.keys == []:  # then this is first keypress
                        buttonBox.keys = theseKeys[0]  # the first key pressed
                        buttonBox.rt = theseRTs[0]
                        # was this 'correct'?
                        if (buttonBox.keys == str(corrAns)) or (buttonBox.keys == corrAns):
                            buttonBox.corr = 1
                        else:
                            buttonBox.corr = 0
                        # a response ends the routine
                        continueRoutine = False   
    
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    if useButtonBox and not triggerTest:
        print('Button box info...')
        print('\t',buttonBox.in_waiting, 'bytes in BB buffer')
        BBLine = buttonBox.readline()
        print(BBLine)
        print(str(len(BBLine)))
        while buttonBox.in_waiting>0:
            print(buttonBox.readline())
        if BBLine != 'No Trigger\n\r' and BBLine !="Timed Out\n\r":
            BBLine = BBLine.split('\t')
            timing = BBLine[0]
            response = BBLine[1][0]#Second indexing removes \n\r
            triggered = True
            print('timing...')
            print('\t', str(timing))
            print('response...')
            print('\t', str(response))
            while buttonBox.in_waiting>0:
                print(buttonBox.readline())
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p') 
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
        elif BBLine=="Triggered\n\r": #and BBLine =="Timed Out\n\r":
            timing = response = 'NA'
            triggered = True
            nTriggeredTestTrials += 1
            while buttonBox.in_waiting>0:
                print(buttonBox.readline())
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p') 
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
#        elif BBLine=="No Trigger\n\r" and BBLine ="Timed Out\n\r":
#            timing = response = 'NA'
#            triggered = True
#            nTriggeredTestTrials += 1
#            while buttonBox.in_waiting>0:
#                print(buttonBox.readline())
#            buttonBox.reset_input_buffer()
#            buttonBox.write(b'p') 
#            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
        else:
            timing = response = 'NA'
            triggered = False
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p')
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
    elif useButtonBox and triggerTest:
        print('Button box info...')
        print('\t',buttonBox.in_waiting, 'bytes in BB buffer')
        BBLine = buttonBox.readline()
        print(BBLine)
        print(str(len(BBLine)))
        while buttonBox.in_waiting>0:
            print(buttonBox.readline())
        if BBLine=="Triggered\n\r":
            timing = response = 'NA'
            triggered = True
            nTriggeredTestTrials += 1
            while buttonBox.in_waiting>0:
                print(buttonBox.readline())
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p') 
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
        else:
            timing = response = 'NA'
            triggered = False
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p')
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
                # store data for practice (TrialHandler)
    practice.addData('resp.keys',resp.keys)
    practice.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        practice.addData('resp.rt', resp.rt)
    if useButtonBox:
        practice.addData('buttonBoxButton','\t')
        practice.addData('buttonBoxRT','\t')
    if BBLine != 'No Trigger\n\r' and BBLine !="Timed Out\n\r":
             practice.addData('buttonBoxButton',response)
             practice.addData('buttonBoxRT',timing)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'practice'
   # ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if useButtonBox:
#        msg="RT=%.3f" %(timing)
        if BBLine != 'No Trigger\n\r' and BBLine !="Timed Out\n\r":
           msg="good" 
        else:
              msg="Oops! That was too slow"
    elif resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    feedback_2.setText(msg)

    
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()

# ------Prepare to start Routine "instructText"-------
t = 0
instructClock.reset()  # clock
frameN = -1
continueRoutine = True
# update component parameters for each repeat
ready1 = event.BuilderKeyResponse()
# keep track of which components have finished
instructComponents = [instrText, ready1]
for thisComponent in instructComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "instruct"-------
while continueRoutine:
    # get current time
    t = instructClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *instrText* updates
    if t >= 0.0 and instrText.status == NOT_STARTED:
        # keep track of start time/frame for later
        instrText.tStart = t
        instrText.frameNStart = frameN  # exact frame index
        instrText.setAutoDraw(True)
    
    # *ready1* updates
    if t >= 0.0 and ready1.status == NOT_STARTED:
        # keep track of start time/frame for later
        ready1.tStart = t
        ready1.frameNStart = frameN  # exact frame index
        ready1.status = STARTED
        # keyboard checking is just starting
        event.clearEvents(eventType='keyboard')
    if ready1.status == STARTED:
        theseKeys = event.getKeys()
        
        # check for quit:
        if "escape" in theseKeys:
            endExpNow = True
        if len(theseKeys) > 0:  # at least one key was pressed
            # a response ends the routine
            continueRoutine = False
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in instructComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "instruct"-------
for thisComponent in instructComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "instruct" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trial = data.TrialHandler(nReps=1.0, method='sequential', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('conditions4.xlsx'),
    seed=None, name='trial')
thisExp.addLoop(trial)  # add the loop to the experiment
thistrial = trial.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thistrial.rgb)
if thistrial != None:
    for paramName in thistrial.keys():
        exec(paramName + '= thistrial.' + paramName)

for thistrial in trial:
    currentLoop = trial
    # abbreviate parameter names if possible (e.g. rgb = thistrial.rgb)
    if thistrial != None:
        for paramName in thistrial.keys():
            exec(paramName + '= thistrial.' + paramName)

    # ------Prepare to start Routine "trial"-------
    t = 0
    trialClock.reset()  # clock
    if useButtonBox and not triggerTest:
        buttonBox.write(b'b') #start looking for a flash of light to trigger the clock
    elif useButtonBox and triggerTest:
        buttonBox.write(b'd') #if we're testing the trigger. Run the trigger test. Outputs "Triggered\r\n" if the photo cell is triggered
    frameN = -1
    continueRoutine = True
    # update component parameters for each repeat
    itemL.setText(left)
    resp = event.BuilderKeyResponse()
    itemR.setText(right)

    # keep track of which components have finished
    trialComponents = [fixation, blank,itemL, itemR,resp]
    for thisComponent in trialComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "trial"-------
    while continueRoutine:
        # get current time
        t = trialClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each fram        

        # *fixation* updates
        if t >= 0.5 and fixation.status == NOT_STARTED:
            # keep track of start time/frame for later
            fixation.tStart = t
            fixation.frameNStart = frameN  # exact frame index
            fixation.setAutoDraw(True)
        frameRemains = 0.5 + 0.75- win.monitorFramePeriod * 0.75  # most of one frame period left
        if fixation.status == STARTED and t >= frameRemains:
            fixation.setAutoDraw(False)
        
        # *blank* updates
        if t >= 0.0 and blank.status == NOT_STARTED:
            # keep track of start time/frame for later
            blank.tStart = t
            blank.frameNStart = frameN  # exact frame index
            blank.setAutoDraw(True)
        frameRemains = 0.0 + 0.5- win.monitorFramePeriod * 0.75  # most of one frame period left
        if blank.status == STARTED and t >= frameRemains:
            blank.setAutoDraw(False)
            
        # *itemR* updates
        if t >= 1 and itemR.status == NOT_STARTED:
            # keep track of start time/frame for later
            itemR.tStart = t
            itemR.frameNStart = frameN  # exact frame index
            itemR.setAutoDraw(True);buttonBoxStimuli.draw()
        frameRemains = 1.0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if itemR.status == STARTED and t >= frameRemains:
            itemR.setAutoDraw(False)
        
        # *itemL* updates
        if t >= 1 and itemL.status == NOT_STARTED:
            # keep track of start time/frame for later
            itemL.tStart = t
            itemL.frameNStart = frameN  # exact frame index
            itemL.setAutoDraw(True)
        frameRemains = 1.0 + 0.25- win.monitorFramePeriod * 0.75  # most of one frame period left
        if itemL.status == STARTED and t >= frameRemains:
            itemL.setAutoDraw(False)
        
        # *resp* updates
        if t >= 1 and resp.status == NOT_STARTED:
            # keep track of start time/frame for later
            resp.tStart = t
            resp.frameNStart = frameN  # exact frame index
            resp.status = STARTED
            # keyboard checking is just starting
            win.callOnFlip(resp.clock.reset)  # t=0 on next screen flip
            event.clearEvents(eventType='keyboard')
        if resp.status == STARTED:
            theseKeys = event.getKeys(keyList=['1', '2', '3'])
            
            # check for quit:
            if "escape" in theseKeys:
                endExpNow = True
            if len(theseKeys) > 0:  # at least one key was pressed
                if resp.keys == []:  # then this was the first keypress
                    resp.keys = theseKeys[0]  # just the first key pressed
                    resp.rt = resp.clock.getTime()
                    # was this 'correct'?
                    if (resp.keys == str(corrAns)) or (resp.keys == corrAns):
                        resp.corr = 1
                    else:
                        resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False

        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "trial"-------
    for thisComponent in trialComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    # check responses
    if resp.keys in ['', [], None]:  # No response was made
        resp.keys=None
        # was no response the correct answer?!
        if str(corrAns).lower() == 'none':
           resp.corr = 1  # correct non-response
        else:
           resp.corr = 0  # failed to respond (incorrectly)
    if useButtonBox and not triggerTest:
        print('Button box info...')
        print('\t',buttonBox.in_waiting, 'bytes in BB buffer')
        BBLine = buttonBox.readline()
        print(BBLine)
        print(str(len(BBLine)))
        while buttonBox.in_waiting>0:
            print(buttonBox.readline())
        if BBLine=="Timed Out\r\n":
            timing = response = 'NA'
            triggered = True
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p')
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
        elif BBLine == "No Trigger\r\n":
            timing = response = "NA"
            nNoTrigger += 1
            triggered = False
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p')
            buttonBox.readline()
        else: #elif BBLine != 'No Trigger\n\r' and BBLine !="Timed Out\n\r":
            BBLine = BBLine.split('\t')
            timing = BBLine[0]
            response = BBLine[1][0]#Second indexing removes \n\r
            triggered = True
            print('timing...')
            print('\t', str(timing))
            print('response...')
            print('\t', str(response))
            while buttonBox.in_waiting>0:
                print(buttonBox.readline())
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p') 
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
    elif useButtonBox and triggerTest:
        print('Button box info...')
        print('\t',buttonBox.in_waiting, 'bytes in BB buffer')
        BBLine = buttonBox.readline()
        print(BBLine)
        print(str(len(BBLine)))
        while buttonBox.in_waiting>0:
            print(buttonBox.readline())
        if BBLine=="Triggered\n\r":
            timing = response = 'NA'
            triggered = True
            nTriggeredTestTrials += 1
            while buttonBox.in_waiting>0:
                print(buttonBox.readline())
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p') 
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
        else:
            timing = response = 'NA'
            triggered = False
            buttonBox.reset_input_buffer()
            buttonBox.write(b'p')
            buttonBox.readline() #Readline is just here to clear the "waiting for input" line from the box's buffer
    # store data for trial (TrialHandler)
    trial.addData('resp.keys',resp.keys)
    trial.addData('resp.corr', resp.corr)
    if resp.keys != None:  # we had a response
        trial.addData('resp.rt', resp.rt)
        if useButtonBox:
            trial.addData('buttonBoxButton','\t')
            trial.addData('buttonBoxRT','\t')
    if useButtonBox:
        trial.addData('buttonBoxButton','\t')
        trial.addData('buttonBoxRT','\t')
        if BBLine != 'No Trigger\n\r' and BBLine !="Timed Out\n\r":
             trial.addData('buttonBoxButton', response)
             trial.addData('buttonBoxRT', timing)
    # the Routine "trial" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'trial'
# ------Prepare to start Routine "feedback"-------
    t = 0
    feedbackClock.reset()  # clock
    frameN = -1
    continueRoutine = True
    routineTimer.add(1.000000)
    # update component parameters for each repeat
    if resp.corr:#stored on last run routine
      msg="Correct! RT=%.3f" %(resp.rt)
    else:
      msg="Oops! That was wrong"
    feedback_2.setText(msg)
    # keep track of which components have finished
    feedbackComponents = [feedback_2]
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    
    # -------Start Routine "feedback"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = feedbackClock.getTime()
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        
        # *feedback_2* updates
        if t >= 0.0 and feedback_2.status == NOT_STARTED:
            # keep track of start time/frame for later
            feedback_2.tStart = t
            feedback_2.frameNStart = frameN  # exact frame index
            feedback_2.setAutoDraw(True)
        frameRemains = 0.0 + 1.0- win.monitorFramePeriod * 0.75  # most of one frame period left
        if feedback_2.status == STARTED and t >= frameRemains:
            feedback_2.setAutoDraw(False)
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # check for quit (the Esc key)
        if endExpNow or event.getKeys(keyList=["escape"]):
            core.quit()
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "feedback"-------
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    
    thisExp.nextEntry()
# ------Prepare to start Routine "thanks"-------
t = 0
thanksClock.reset()  # clock
frameN = -1
continueRoutine = True
routineTimer.add(2.000000)
# update component parameters for each repeat
# keep track of which components have finished
thanksComponents = [thanksText]
for thisComponent in thanksComponents:
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED

# -------Start Routine "thanks"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = thanksClock.getTime()
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *thanksText* updates
    if t >= 0.0 and thanksText.status == NOT_STARTED:
        # keep track of start time/frame for later
        thanksText.tStart = t
        thanksText.frameNStart = frameN  # exact frame index
        thanksText.setAutoDraw(True)
    frameRemains = 0.0 + 2.0- win.monitorFramePeriod * 0.75  # most of one frame period left
    if thanksText.status == STARTED and t >= frameRemains:
        thanksText.setAutoDraw(False)
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # check for quit (the Esc key)
    if endExpNow or event.getKeys(keyList=["escape"]):
        core.quit()
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()


# -------Ending Routine "thanks"-------
for thisComponent in thanksComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()