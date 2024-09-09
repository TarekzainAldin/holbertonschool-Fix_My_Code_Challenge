###
# Sort integer arguments (ascending)
###

result = []
ARGV.each do |arg|
  # Skip if not an integer (positive or negative)
  next if arg !~ /^-?\d+$/

  # Convert to integer and push to the result array
  result << arg.to_i
end

# Sort the result array in ascending order
result.sort!

# Print the sorted array
puts result
