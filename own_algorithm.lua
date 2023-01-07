local function longest_word(a, b)
	if #a < #b then
		a, b = b, a
	end
	return a, b
end


local function longest_common_match(a, b)
	-- Make sure a is the longest string

	if #a < 3 then
		return "Too short to compare."
	end

	-- Create an empty table to store the matches
	local matches = {}
	local all_match_count = 0

	-- Iterate over the characters in a
	for i = 1, #a do
		-- Iterate over the characters in b
		for j = 1, #b do
			-- Create an empty table to store the current match
			local current_match = {}

			-- Iterate over the characters in a starting at index i
			for k = i, #a do
				-- Check if the character at index k in a is the same as the character at index j in b
				if string.sub(a, k, k) == string.sub(b, j, j) then
					-- If the characters are the same, add the character to the current match table

					table.insert(current_match, string.sub(a, k, k))
					-- Increment j to compare the next character in b
					j += 1
				else
					-- If the characters are different, break the inner loop
					break
				end
			end

			local cur_word = table.concat(current_match)
			local cur_length = #cur_word
			if cur_length >= 1 then
				all_match_count += 1
			end
			-- If the current match is longer than the previous longest match, update the longest match
			if #current_match > #matches then
				matches = current_match
			end
		end
	end

	-- Return the longest match
	return table.concat(matches), all_match_count
end


local function perfect_common_match_calc(sentence)
	--[[ 
	In an ideal scenario, how many common matches would be made?
	If both strings are "aaabb" it's: 
	(how many a's * how many a's) + unique letter (how many b's * how many b's) + ... = 13
	]]

	local counts = {}
	
	for i = 1, #sentence do
		local letter = string.sub(sentence, i, i)

		if counts[letter] then
			counts[letter] = counts[letter] + 1
		else
			counts[letter] = 1
		end
	end
	
	local total_matches = 0
	
	for letter, count in pairs(counts) do
		total_matches += count * count
	end
	
	return total_matches
end


local a = "Now these two sentences are exactly similar."
local b = "Now these two sentences are exactly similar."

print("Input A: ", a)
print("Input B: ", b)


print("--------------")

local a, b = longest_word(a, b) -- Flips a or b depending on which is longest.
local perfect_match_count = perfect_common_match_calc(a)

local longest_match, all_match_count = longest_common_match(a, b)

local matches_length_compared = (#longest_match / #a) * 100 -- How big of a portion does the max match take of the sentence?

print("How big of a portion does the max match take of the sentence: ", matches_length_compared)

local match_count_similarity = (all_match_count / perfect_match_count) * 100 -- How many matches could've been made in perfect scenario?

print("Perfect match count similary would be: ", match_count_similarity)

local string_length_similarity = (#b / #a) * 100 -- How long both a and b are compared to each other?

print("Length difference:", string_length_similarity)


--------


-- Average 1 and 2:
local average_count_match_ratio = (matches_length_compared + match_count_similarity) / 2
local final = (string_length_similarity / 100) * average_count_match_ratio
print("Average count to match ratio: ", average_count_match_ratio)
print("Ratio between length of strings to average ratio: ", final)

print("Final Similarity Metric Ratio:", final, "with longest match: " .. longest_match)
