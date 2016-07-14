import string

from CFD import Setup
from CFD import DSE

savepath = "C:\Temp\CFDScripts\\"
saveformat = ".png"

def main():
	# Save static images for all time steps
	study = Setup.DesignStudy.Create()
	scenario = study.getActiveScenario()
	results = scenario.results()

	if results is None:
		DSE.UI.ShowErrorMessage( "No results found" )
		return

	results.activate()

	steplist = results.resultStepStrings()

	for stepstring in steplist:
		# expecting a string in the format "50[Time = 0.5]"
		step = string.split( stepstring, "["  )[0]
		time = string.split( string.split( string.split( stepstring,"=" )[1], "]" ) [0] )[0]
		results.activateResultStep( int( step ) )
		filename = scenario.name() + " (" + time + "s)"
		path = savepath + filename + saveformat
		DSE.UI.SaveResultsImage( path )
		DSE.UI.ShowMessage( "Image Saved to " + path )

main()
