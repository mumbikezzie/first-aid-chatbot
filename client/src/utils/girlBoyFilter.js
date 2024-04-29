export default function distinguishGender(name) {
    // Convert the name to lowercase for case-insensitive comparison
    const lowerName = name.toLowerCase();
  
    // Common suffixes for girl's names
    const girlSuffixes = ["a", "ia", "ina", "ella", "elle", "ette", "ie", "y", "ey", "i", "ina", "elle", "a", "etta", "elle", "elle", "is"];
  
    // Common suffixes for boy's names
    const boySuffixes = ["o", "us", "es", "is", "el", "ell", "an", "en", "er", "on", "on", "em", "y", "ey", "es"];
  
    // Check if the name ends with any of the girl suffixes
    for (const suffix of girlSuffixes) {
      if (lowerName.endsWith(suffix)) {
        return "girl";
      }
    }
  
    // Check if the name ends with any of the boy suffixes
    for (const suffix of boySuffixes) {
      if (lowerName.endsWith(suffix)) {
        return "boy";
      }
    }
  
    // If no suffix matches, return "unknown"
    return "unknown";
  }
