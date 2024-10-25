# Load the Atomic Red Team module
Import-Module .\atomic-red-team\invoke-atomicredteam\Invoke-AtomicRedTeam.psd1

# Run a specific Atomic Test, for example T1003 (Credential Dumping)
$TechniqueId = "T1003"
Invoke-AtomicTest -TechniqueId $TechniqueId -PathToAtomicsFolder ".\atomic-red-team\atomics\"

# Save results if required
Write-Output "Atomic test executed for $TechniqueId"
