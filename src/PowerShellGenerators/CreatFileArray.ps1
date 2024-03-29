#$folderPath = "C:\Users\joser\iCloudDrive\Bear Bears\Male\Fur"
#$folderPath = "C:\Users\joser\iCloudDrive\Bear Bears\Male\Eyes"
$folderPath = "C:\Users\joser\iCloudDrive\Bear Bears\Male\Hair"
$folderPath = "C:\Users\joser\iCloudDrive\Bear Bears\Male\Mouth"

# Get all PNG files in the specified folder
$pngFiles = Get-ChildItem -Path $folderPath -Filter *.png

# Count the number of files
$fileCount = $pngFiles.Count

# Create an array to store the objects 
$jsonArray = @()

# Initialize the total count and minimum random value
$totalCount = 100
$minRandom = 2
$maxRandomWeight = 12
# Calculate the maximum random value based on the remaining total and minimum random value
$maxRandom = [Math]::Min($totalCount - ($fileCount - 1) * $minRandom + 1, $maxRandomWeight)

# Create an ArrayList of available counts
$availableCounts = [System.Collections.ArrayList]::new(1..$maxRandom)

# Iterate over each PNG file
foreach ($file in $pngFiles) {
    # If there are no available counts, reset the array
    if ($availableCounts.Count -eq 0) {
        $availableCounts.AddRange(1..$maxRandom)
    }

    # Select a random count from the available counts
    $randomIndex = Get-Random -Minimum 0 -Maximum $availableCounts.Count
    $randomCount = $availableCounts[$randomIndex]

    # Remove the selected count from the available counts
    $availableCounts.RemoveAt($randomIndex)

    # Deduct the random count from the total
    $totalCount -= $randomCount

    # Create a hashtable representing the object
    $object = @{
        "name" = $file.BaseName
        "count" = $randomCount
    }

    # Add the object to the JSON array
    $jsonArray += $object
}

# Convert the array to JSON
$jsonString = $jsonArray | ConvertTo-Json

# Output the JSON string
$jsonString
