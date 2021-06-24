

# Azure Blob Storage Initial Client code here

# Idea, set a global ticker/clock so after 24 hours
#   (this could increase CPU load, having
#    listen for clock interrupts or check time)

# -> Therefore, after a threshold (exponential growth based on number of refreshes occurred since spin up)
#    we will redownload with the blob client

