# ROSITA in CoppeliaSim

## What is this?
This repo hosts our ([Marte(llo) team](https://rositascuola.altervista.org/team-martello-%f0%9f%94%a8-liceo-scientifico-l-spallanzani-tivoli-rm/)) attempt at making a somewhat workiking and accurate replica of the 4WD ROSITA rover.

## Installation

1. Install CoppeliaSim from [here](https://www.coppeliarobotics.com/)
2. Clone this repo
3. Install dipendencies (`pip -r requirements.txt`)

# IMPORTANT: Apply patch to Coppelia's remote API
append to `<installFolder>/addOns/ZMQ remote API server.lua` the following **before** opening Coppelia
```
sim.saveImage = wrap(sim.saveImage, function(origFunc)
    return function(img, res, opt, nm, q)
        local ret = origFunc(img, res, opt, nm, q)
        if type(ret) ~= 'string' then
            ret = ''
        end
        return ret
    end
end)
```
Thanks to the CoppeliaSim team for providing the patch
(see [CoppeliaSim Forum](https://forum.coppeliarobotics.com/viewtopic.php?p=40407#p40407) for more details. 
## Development
The reccomanded way to develop this project is by using **venv**s. This can be done, in Pycharm, by cloning the repository and by answering "yes" in the venv prompt. 
