

pairs = [
    {"prompt": "What to do if Cuts?", "completion": "Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until bleeding stops. Apply Petroleum Jelly to make sure that the wound is moist for quick healing. Finally cover the cut with a sterile bandage. Pain relievers such as acetaminophen can be applied."},
{"prompt": "how do you treat abrasions?", "completion": "Begin with washed hands.Gently clean the area with cool to lukewarm water and mild soap. Remove dirt or other particles from the wound using sterilized tweezers.For a mild scrape thatâ€™s not bleeding, leave the wound uncovered.If the wound is bleeding, use a clean cloth or bandage, and apply gentle pressure to the area to stop any bleeding.Cover a wound that bled with a thin layer of topical antibiotic ointment, like Bacitracin, or a sterile moisture barrier ointment, like Aquaphor. Cover it with a clean bandage or gauze. Gently clean the wound and change the ointment and bandage once per day.Watch the area for signs of infection, like pain or redness and swelling. See your doctor if you suspect infection."},
{"prompt": "How do you treat Sting?", "completion": "Remove any stingers immediately. Some experts recommend scraping out the stinger with a credit card. Applying ice to the site may provide some mild relief. Apply ice for 20 minutes once every hour as needed. Wrap the ice in a towel or keep a cloth between the ice and skin to keep from freezing the skin. Taking an antihistamine such as diphenhydramine (Benadryl) or a nonsedating one such as loratadine (Claritin) will help with itching and swelling. Take acetaminophen (Tylenol) or ibuprofen (Motrin)for pain relief as needed. Wash the sting site with soap and water. Placing hydrocortisone cream on the sting can help relieve redness, itching, and swelling."},
{"prompt": "How to remove Splinters", "completion": "1. SOAK IT IN EPSOM SALTS. Dissolve a cup of the salts into a warm bath and soak whatever part of the body has the splinter. Failing that, you can also put some of the salts onto a bandage pad and leave it covered for a day; this will eventually help bring the splinter to the surface. 2. VINEGAR OR OIL. Another simple way to draw out that stubborn splinter is to soak the affected area in oil (olive or corn) or white vinegar. Just pour some in a bowl and soak the area for around 20 to 30 minutes,"},
{"prompt": "How do you treat a sprain?", "completion": "Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake. To help stop swelling, compress the ankle with an elastic bandage until the swelling stops. In most cases, pain relievers â€” such as ibuprofen (Advil, Motrin IB, others) or naproxen sodium (Aleve, others) or acetaminophen (Tylenol, others) are enough to manage the pain of a sprained ankle."},
{"prompt": "How do you treat a strain?", "completion": "Rest,Ice,Compression and Elevation can be used to cure strains. Avoid using your muscle for a few days, especially if movement causes an increase in pain and also Apply ice immediately after injuring your muscle. This will minimize swelling. Donâ€™t put ice directly on your skin. Use an ice pack or wrap ice in a towel. To reduce swelling, wrap the affected area with an elastic bandage until swelling comes down."},
{"prompt": "How do you treat a mild Fever?", "completion": "To treat a fever at home: 1)Drink plenty of fluids to stay hydrated. 2)Dress in lightweight clothing. 3)Use a light blanket if you feel chilled, until the chills end. 4)Take acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others). 5) Get medical help if the fever lasts more than five days in a row."},
{"prompt": "How do you treat nasal Congestion?", "completion": "When youâ€™re stuffed up, focus on keeping your nasal passages and sinuses moist. To keep your nasal passages moist, you can: 1)Use a humidifier or vaporizer. 2)Drink lots of fluids. This will thin out your mucus, which could help prevent blocked sinuses. 3)Place a warm, wet towel on your face. It may relieve discomfort and open your nasal passages."},
{"prompt": "How to cure cough?", "completion": "1) Honey:- Use honey to treat a cough, mix 2 teaspoons (tsp) with warm water or an herbal tea. Drink this mixture once or twice a day. Do not give honey to children under 1 year of age. 2) Ginger:- Brew up a soothing ginger tea by adding 20â€“40 grams (g) of fresh ginger slices to a cup of hot water. Allow to steep for a few minutes before drinking. Add honey or lemon juice to improve the taste and further soothe a cough. 3) Fluids:- Staying hydrated is vital for those with a cough or cold. Research indicates that drinking liquids at room temperature can alleviate a cough, runny nose, and sneezing."},
{"prompt": "How do you treat sore throat?", "completion": "1) Make sure you get plenty of rest and drink a lot of fluids. 2)Inhale steam,Run hot water in a sink.Drape a towel over you to trap the steam, and have the person lean over the sink with the water running. Tell him to breathe deeply through his mouth and nose for 5 to 10 minutes. Repeat several times a day. 3)Have him sip chicken broth or warm tea with honey. Donâ€™t give honey to a child under 12 months of age."},
{"prompt": "How do you treat gas problems?", "completion": "1) Replenish body fluids 2)Do not take antidiarrheal drugs or laxatives or pain medication, unless specified by a medical professional.3)Taking antacids may help, per recommendation of a healthcare professional. 4)If prone to frequent heartburns, seek medical help. 5)Taking meals that are not spicy regularly, can relieve ulcer pains. 6)Seek medical help, if conditions persist or continue to worsen"},
{"prompt": "How do you treat Skin problems?", "completion": "1)Hydrocortisone cream. 2)Ointments like calamine lotion. 3)Antihistamines. 4)Cold compresses. 5)Oatmeal baths. 6)Talk to your doctor about what's best for your specific rash."},
{"prompt": "How do you treat Abdonominal Pain?", "completion": "1)Provide clear fluids to sip, such as water, broth, or fruit juice diluted with water. 2)Serve bland foods, such as saltine crackers, plain bread, dry toast, rice, gelatin, or applesauce. 3)Avoid spicy or greasy foods and caffeinated or carbonated drinks until 48 hours after all symptoms have gone away. "},
{"prompt": "How do you treat Bruises?", "completion": "1)Ice the bruise with an ice pack wrapped in a towel. 2)Leave it in place for 10 to 20 minutes. 3)Repeat several times a day for a day or two as needed. 4)Compress the bruised area if it is swelling, using an elastic bandage. "},
{"prompt": "How do you treat a Broken Toe?", "completion": "1)To help decrease pain and swelling in a broken toe, elevate the foot, ice the injury, and stay off the foot. 2)Depending on the severity of the fracture, the toe may need to be put back into place (reduced), and some compound toe fractures may require surgery.3) Most broken toes heal without complications in six weeks."},
{"prompt": "How do you treat Choking?", "completion": "1)Encourage them to keep coughing to try to clear the blockage. 2)Ask them to try to spit out the object if it's in their mouth. 3)If coughing doesn't work, start back blows and Abdonominal thrusts"},
{"prompt": "How do you treat a wound?", "completion": "1)Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. 2)If blood soaks through the bandage, place another bandage on top of the first and keep applying pressure. 3)Raise the injured body part to slow bleeding. 4)When bleeding stops, cover the wound with a new, clean bandage."},
{"prompt": "How do you treat Diarrhea?", "completion": "1)Hydrating the body is essential for recovering from diarrhea.This causes the body to lose electrolytes such as sodium and chloride. 2)It is highly recommended to avoid dairy products, as they may worsen diarrhea in some people. 3)However, if diarrhea lasts for more than 2 days, seek medical advice to avoid complications."},
{"prompt": "How do you treat a Frost bite?", "completion": "warm gently by soaking the affected area in warm water until it appears red and feels warm. loosely bandage the area with sterile gauze. "},
{"prompt": "How do you treat Heat Exhaustion?", "completion": "Remove tight or heavy clothing. Have the person sip chilled water. Cool the person by spraying or sponging with cool water and fanning "},
{"prompt": "How do you treat Heat Stroke?", "completion": "Sponge the person with cool water while fanning them. Place ice packs or cool wet towels on the neck, armpits and groin "},
{"prompt": "How do you treat a Insect Bite?", "completion": "Clean the affected area with soap and warm water. Use a cold pack to reduce swelling and pain. Apply calamine lotion to the affected area "},
{"prompt": "How do you treat a bleeding nose?", "completion": "Sit the person up straight and drop their head slightly forward. Apply finger and thumb pressure on the soft part of the nostrils below the bridge of the nose for atleast ten minutes. Encourage the person to breathe through their mouth "},
{"prompt": "How do you treat a Pulled Muscle?", "completion": "Ice the area immediately. Compress the area with an elastic bandage until the swelling stops. Elevate the injured area above the level of your heart which allows gravity to help reduce swelling"},
{"prompt": "How do you treat Sun Burn?", "completion": "Take frequent cool baths or showers to help relieve the pain. Use a moisturizer that contains aloe or soy to help soothe sunburned skin. Drink extra water"},
{"prompt": "How do you treat Vertigo?", "completion": "Lie down on your left side, staying still for 30 seconds. Then quickly move to lie down on the opposite end of the bed without changing the direction of your head. Keep your head at an angle of 45 degrees and lie for 30 seconds more. Return slowly to sitting and wait a few minutes."},
{"prompt": "How do you treat bleeding?", "completion": "Apply direct pressure to the wound using a bandage or cloth. Maintain pressure to the wound and raise the injured limb above the level of the heart if possible. Add more bandages as needed"},
{"prompt": "How do you treat an eye Injury?", "completion": "The eye should be washed with clean water or saline solution to remove any particles. If swollen, an ice pack should be placed over the eye. If bleeding, gauze should be placed over the cut "},
{"prompt": "How do you treat a chemical burn?", "completion": "Remove contaminated clothing and jewelry and rinse chemicals off for atleast 20 minutes, preferably in a shower. Bandage the burn with a dry sterile dressing. Protect the burned area from pressure and friction "},
{"prompt": "How do you treat a Poison?", "completion": "Call an ambulance immediately. Get the person into fresh air as soon as possible. If the person vomits, turn their head to the side to prevent choking."},
{"prompt": "How do you treat broken Teeth ?", "completion": "Preserve the tooth pieces in a container containing a little saline solution or milk. If you experience bleeding from the mouth, rinse with cold water. Put a piece of gauze to stop the bleeding and schedule an appointment with your dentist as soon as possible. "},
{"prompt": "How do you treat a seizure?", "completion": "Cushion their head if they are on the ground and loosen any tight clothing such as collar or tie to aid breathing. Turn them onto their side after convulsions stop, or if they are convulsing, but have food or fluid in their mouth. Talk to them calmly until they recover "},
{"prompt": "How do you treat a head Injury?", "completion": "Keep the head inline with the spine and prevent movement. Call for medical help. Stop any bleeding by firmly pressing a clean cloth to the wound unless you suspect a skull fracture. If the injury is serious, do not move the persons head "},
{"prompt": "How do you treat Faint?", "completion": "Prop the legs up about 12 inches or 30 centimeters to restore blood flow to the brain. Loosen belts, ties or other tight clothing.  "},
{"prompt": "How do you treat a mild Headache?", "completion": "Give ibuprofen (Advil, Motrin), aspirin, or acetaminophen (Tylenol) for pain. Avoid ibuprofen and other NSAIDs if the person has heart failure or kidney failure. Do not give aspirin to a child under age 18."},
{"prompt": "How do you treat a Cold?", "completion": "1)Keeping hydrated is absolutely vital to help 'flush' out the cold, as well as to break down congestion and keep your throat lubricated. 2)Vitamin C is extremely helpful when fighting infection, so at the first sign of a cold be sure to increase your intake by eating plenty of berries, citrus fruits, papayas, broccoli and red peppers which will help keep you protected. 3)When it comes to combating a cold,Vitamin D is essential in helping to regulate immune response."},
{"prompt": "How do you treat Rashes?", "completion": "1)Olive oil helps in healing and promotes skin renewal given it is packed with vitamin E and antioxidants. It also soothes the skin and reduces itching. 2)Baking soda is useful in drying skin rashes as also in relieving itching and inflammation. 3)Aloe Vera,Thanks to its antibacterial, antifungal, anti-inflammatory and emollient properties, aloe vera is excellent for treating a number of skin ailments including rashes as also soothing the skin."},
{"prompt": "How do you treat a snake bite?", "completion": "While waiting for medical help: 1)Move the person beyond striking distance of the snake. 2)Have the person lie down with wound below the heart. 3)Keep the person calm and at rest, remaining as still as possible to keep venom from spreading. 4)Cover the wound with loose, sterile bandage. 5)Remove any jewelry from the area that was bitten. 6)Remove shoes if the leg or foot was bitten."},
{"prompt": "How do you treat a animal bite?", "completion": "1)Wash the wound with soap and warm water. 2)Gently press a clean cloth over the wound to stop the flow of blood. 3)Apply an antibacterial ointment to the wound. 4)Cover with a sterile bandage. 5)Watch for signs of infection. 6)Seek help if you suspect infection or possible exposure to rabies, or if the wound is severe."},
{"prompt": "What to do if someone is Drowning?", "completion": "1)Place your ear next to the person's mouth and nose. Do you feel air on your cheek? 2)Look to see if the person's chest is moving.If the Person is Not Breathing, Check Pulse. 3)Check the person's pulse for 10 seconds.If There is No Pulse, Start CPR."},
{"prompt": "How to give CPR??", "completion": "1)For an adult or child, place the heel of one hand on the center of the chest at the nipple line. You can also push with one hand on top of the other. For an infant, place two fingers on the breastbone. 2)For an adult or child, press down at least 2 inches. Make sure not to press on ribs. For an infant, press down about 1 and 1/2 inches. Make sure not to press on the end of the breastbone. 3)Do chest compressions only, at the rate of 100-120 per minute or more. Let the chest rise completely between pushes. 4)Check to see if the person has started breathing."},
{"prompt": "How do you treat a Fracture?", "completion": "1)Stop any bleeding. Apply pressure to the wound with a sterile bandage, a clean cloth or a clean piece of clothing. 2)Immobilize the injured area. Don't try to realign the bone or push a bone that's sticking out back in. If you've been trained in how to splint and professional help isn't readily available, apply a splint to the area above and below the fracture sites. Padding the splints can help reduce discomfort. 3)Apply ice packs to limit swelling and help relieve pain. Don't apply ice directly to the skin. Wrap the ice in a towel, piece of cloth or some other material. 4)Treat for shock. If the person feels faint or is breathing in short, rapid breaths, lay the person down with the head slightly lower than the trunk and, if possible, elevate the legs."},

]


def convert_my_data(raw_data):
    new_pairs = []

    for pair in pairs:

        prompt = pair["prompt"]
        completion = pair["completion"]
        
        new_pair = [
            rf"{prompt}",
            [completion]
        ]
        
        new_pairs.append(new_pair)

    return new_pairs


# result = convert_my_data(pairs)
# print(result)


my_data = [
    [
        r'What to do if Cuts?', 
        ['Wash the cut properly to prevent infection and stop the bleeding by applying pressure for 1-2minutes until bleeding stops. Apply Petroleum Jelly to make sure that the wound is moist for quick healing. Finally cover the cut with a sterile bandage. Pain relievers such as acetaminophen can be applied.']]
    , [
        r'how do you treat abrasions?', ['Begin with washed hands.Gently clean the area with cool to lukewarm water and mild soap. Remove dirt or other particles from the wound using sterilized tweezers.For a mild scrape thatâ€™s not bleeding, leave the wound uncovered.If the wound is bleeding, use a clean cloth or bandage, and apply gentle pressure to the area to stop any bleeding.Cover a wound that bled with a thin layer of topical antibiotic ointment, like Bacitracin, or a sterile moisture barrier ointment, like Aquaphor. Cover it with a clean bandage or gauze. Gently clean the wound and change the ointment and bandage once per day.Watch the area for signs of infection, like pain or redness and swelling. See your doctor if you suspect infection.']], 
    [r'How do you treat Sting?', ['Remove any stingers immediately. Some experts recommend scraping out the stinger with a credit card. Applying ice to the site may provide some mild relief. Apply ice for 20 minutes once every hour as needed. Wrap the ice in a towel or keep a cloth between the ice and skin to keep from freezing the skin. Taking an antihistamine such as diphenhydramine (Benadryl) or a nonsedating one such as loratadine (Claritin) will help with itching and swelling. Take acetaminophen (Tylenol) or ibuprofen (Motrin)for pain relief as needed. Wash the sting site with soap and water. Placing hydrocortisone cream on the sting can help relieve redness, itching, and swelling.']], 
    [r'How to remove Splinters', ['1. SOAK IT IN EPSOM SALTS. Dissolve a cup of the salts into a warm bath and soak whatever part of the body has the splinter. Failing that, you can also put some of the salts onto a bandage pad and leave it covered for a day; this will eventually help bring the splinter to the surface. 2. VINEGAR OR OIL. Another simple way to draw out that stubborn splinter is to soak the affected area in oil (olive or corn) or white vinegar. Just pour some in a bowl and soak the area for around 20 to 30 minutes,']], 
    [r'How do you treat a sprain?', ["Use an ice pack or ice slush bath immediately for 15 to 20 minutes and repeat every two to three hours while you're awake. To help stop swelling, compress the ankle with an elastic bandage until the swelling stops. In most cases, pain relievers â€” such as ibuprofen (Advil, Motrin IB, others) or naproxen sodium (Aleve, others) or acetaminophen (Tylenol, others) are enough to manage the pain of a sprained ankle."]], 
    [r'How do you treat a strain?', ['Rest,Ice,Compression and Elevation can be used to cure strains. Avoid using your muscle for a few days, especially if movement causes an increase in pain and also Apply ice immediately after injuring your muscle. This will minimize swelling. Donâ€™t put ice directly on your skin. Use an ice pack or wrap ice in a towel. To reduce swelling, wrap the affected area with an elastic bandage until swelling comes down.']], 
    [r'How do you treat a mild Fever?', ['To treat a fever at home: 1)Drink plenty of fluids to stay hydrated. 2)Dress in lightweight clothing. 3)Use a light blanket if you feel chilled, until the chills end. 4)Take acetaminophen (Tylenol, others) or ibuprofen (Advil, Motrin IB, others). 5) Get medical help if the fever lasts more than five days in a row.']],
     [r'How do you treat nasal Congestion?', ['When youâ€™re stuffed up, focus on keeping your nasal passages and sinuses moist. To keep your nasal passages moist, you can: 1)Use a humidifier or vaporizer. 2)Drink lots of fluids. This will thin out your mucus, which could help prevent blocked sinuses. 3)Place a warm, wet towel on your face. It may relieve discomfort and open your nasal passages.']], 
     [r'How to cure cough?', ['1) Honey:- Use honey to treat a cough, mix 2 teaspoons (tsp) with warm water or an herbal tea. Drink this mixture once or twice a day. Do not give honey to children under 1 year of age. 2) Ginger:- Brew up a soothing ginger tea by adding 20â€“40 grams (g) of fresh ginger slices to a cup of hot water. Allow to steep for a few minutes before drinking. Add honey or lemon juice to improve the taste and further soothe a cough. 3) Fluids:- Staying hydrated is vital for those with a cough or cold. Research indicates that drinking liquids at room temperature can alleviate a cough, runny nose, and sneezing.']], 
     [r'How do you treat sore throat?', ['1) Make sure you get plenty of rest and drink a lot of fluids. 2)Inhale steam,Run hot water in a sink.Drape a towel over you to trap the steam, and have the person lean over the sink with the water running. Tell him to breathe deeply through his mouth and nose for 5 to 10 minutes. Repeat several times a day. 3)Have him sip chicken broth or warm tea with honey. Donâ€™t give honey to a child under 12 months of age.']], 
     [r'How do you treat gas problems?', ['1) Replenish body fluids 2)Do not take antidiarrheal drugs or laxatives or pain medication, unless specified by a medical professional.3)Taking antacids may help, per recommendation of a healthcare professional. 4)If prone to frequent heartburns, seek medical help. 5)Taking meals that are not spicy regularly, can relieve ulcer pains. 6)Seek medical help, if conditions persist or continue to worsen']], 
     [r'How do you treat Skin problems?', ["1)Hydrocortisone cream. 2)Ointments like calamine lotion. 3)Antihistamines. 4)Cold compresses. 5)Oatmeal baths. 6)Talk to your doctor about what's best for your specific rash."]], 
     [r'How do you treat Abdonominal Pain?', ['1)Provide clear fluids to sip, such as water, broth, or fruit juice diluted with water. 2)Serve bland foods, such as saltine crackers, plain bread, dry toast, rice, gelatin, or applesauce. 3)Avoid spicy or greasy foods and caffeinated or carbonated drinks until 48 hours after all symptoms have gone away. ']], 
     [r'How do you treat Bruises?', ['1)Ice the bruise with an ice pack wrapped in a towel. 2)Leave it in place for 10 to 20 minutes. 3)Repeat several times a day for a day or two as needed. 4)Compress the bruised area if it is swelling, using an elastic bandage. ']], 
     [r'How do you treat a Broken Toe?', ['1)To help decrease pain and swelling in a broken toe, elevate the foot, ice the injury, and stay off the foot. 2)Depending on the severity of the fracture, the toe may need to be put back into place (reduced), and some compound toe fractures may require surgery.3) Most broken toes heal without complications in six weeks.']], 
     [r'How do you treat Choking?', ["1)Encourage them to keep coughing to try to clear the blockage. 2)Ask them to try to spit out the object if it's in their mouth. 3)If coughing doesn't work, start back blows and Abdonominal thrusts"]], 
     [r'How do you treat a wound?', ['1)Rinse the cut or wound with water and apply pressure with sterile gauze, a bandage, or a clean cloth. 2)If blood soaks through the bandage, place another bandage on top of the first and keep applying pressure. 3)Raise the injured body part to slow bleeding. 4)When bleeding stops, cover the wound with a new, clean bandage.']], 
     [r'How do you treat Diarrhea?', ['1)Hydrating the body is essential for recovering from diarrhea.This causes the body to lose electrolytes such as sodium and chloride. 2)It is highly recommended to avoid dairy products, as they may worsen diarrhea in some people. 3)However, if diarrhea lasts for more than 2 days, seek medical advice to avoid complications.']], 
     [r'How do you treat a Frost bite?', ['warm gently by soaking the affected area in warm water until it appears red and feels warm. loosely bandage the area with sterile gauze. ']], 
     [r'How do you treat Heat Exhaustion?', ['Remove tight or heavy clothing. Have the person sip chilled water. Cool the person by spraying or sponging with cool water and fanning ']], 
     [r'How do you treat Heat Stroke?', ['Sponge the person with cool water while fanning them. Place ice packs or cool wet towels on the neck, armpits and groin ']], 
     [r'How do you treat a Insect Bite?', ['Clean the affected area with soap and warm water. Use a cold pack to reduce swelling and pain. Apply calamine lotion to the affected area ']], 
     [r'How do you treat a bleeding nose?', ['Sit the person up straight and drop their head slightly forward. Apply finger and thumb pressure on the soft part of the nostrils below the bridge of the nose for atleast ten minutes. Encourage the person to breathe through their mouth ']], 
     [r'How do you treat a Pulled Muscle?', ['Ice the area immediately. Compress the area with an elastic bandage until the swelling stops. Elevate the injured area above the level of your heart which allows gravity to help reduce swelling']],
     [r'How do you treat Sun Burn?', ['Take frequent cool baths or showers to help relieve the pain. Use a moisturizer that contains aloe or soy to help soothe sunburned skin. Drink extra water']], 
     [r'How do you treat Vertigo?', ['Lie down on your left side, staying still for 30 seconds. Then quickly move to lie down on the opposite end of the bed without changing the direction of your head. Keep your head at an angle of 45 degrees and lie for 30 seconds more. Return slowly to sitting and wait a few minutes.']], 
     [r'How do you treat bleeding?', ['Apply direct pressure to the wound using a bandage or cloth. Maintain pressure to the wound and raise the injured limb above the level of the heart if possible. Add more bandages as needed']], 
     [r'How do you treat an eye Injury?', ['The eye should be washed with clean water or saline solution to remove any particles. If swollen, an ice pack should be placed over the eye. If bleeding, gauze should be placed over the cut ']], 
     [r'How do you treat a chemical burn?', ['Remove contaminated clothing and jewelry and rinse chemicals off for atleast 20 minutes, preferably in a shower. Bandage the burn with a dry sterile dressing. Protect the burned area from pressure and friction ']],
      [r'How do you treat a Poison?', ['Call an ambulance immediately. Get the person into fresh air as soon as possible. If the person vomits, turn their head to the side to prevent choking.']], 
      [r'How do you treat broken Teeth ?', ['Preserve the tooth pieces in a container containing a little saline solution or milk. If you experience bleeding from the mouth, rinse with cold water. Put a piece of gauze to stop the bleeding and schedule an appointment with your dentist as soon as possible. ']], 
      [r'How do you treat a seizure?', ['Cushion their head if they are on the ground and loosen any tight clothing such as collar or tie to aid breathing. Turn them onto their side after convulsions stop, or if they are convulsing, but have food or fluid in their mouth. Talk to them calmly until they recover ']],
       [r'How do you treat a head Injury?', ['Keep the head inline with the spine and prevent movement. Call for medical help. Stop any bleeding by firmly pressing a clean cloth to the wound unless you suspect a skull fracture. If the injury is serious, do not move the persons head ']], 
       [r'How do you treat Faint?', ['Prop the legs up about 12 inches or 30 centimeters to restore blood flow to the brain. Loosen belts, ties or other tight clothing.  ']], 
       [r'How do you treat a mild Headache?', ['Give ibuprofen (Advil, Motrin), aspirin, or acetaminophen (Tylenol) for pain. Avoid ibuprofen and other NSAIDs if the person has heart failure or kidney failure. Do not give aspirin to a child under age 18.']],
      [r'How do you treat a Cold?', ["1)Keeping hydrated is absolutely vital to help 'flush' out the cold, as well as to break down congestion and keep your throat lubricated. 2)Vitamin C is extremely helpful when fighting infection, so at the first sign of a cold be sure to increase your intake by eating plenty of berries, citrus fruits, papayas, broccoli and red peppers which will help keep you protected. 3)When it comes to combating a cold,Vitamin D is essential in helping to regulate immune response."]],
       [r'How do you treat Rashes?', ['1)Olive oil helps in healing and promotes skin renewal given it is packed with vitamin E and antioxidants. It also soothes the skin and reduces itching. 2)Baking soda is useful in drying skin rashes as also in relieving itching and inflammation. 3)Aloe Vera,Thanks to its antibacterial, antifungal, anti-inflammatory and emollient properties, aloe vera is excellent for treating a number of skin ailments including rashes as also soothing the skin.']],
        [r'How do you treat a snake bite?', ['While waiting for medical help: 1)Move the person beyond striking distance of the snake. 2)Have the person lie down with wound below the heart. 3)Keep the person calm and at rest, remaining as still as possible to keep venom from spreading. 4)Cover the wound with loose, sterile bandage. 5)Remove any jewelry from the area that was bitten. 6)Remove shoes if the leg or foot was bitten.']],
         [r'How do you treat a animal bite?', ['1)Wash the wound with soap and warm water. 2)Gently press a clean cloth over the wound to stop the flow of blood. 3)Apply an antibacterial ointment to the wound. 4)Cover with a sterile bandage. 5)Watch for signs of infection. 6)Seek help if you suspect infection or possible exposure to rabies, or if the wound is severe.']],
          [r'What to do if someone is Drowning?', ["1)Place your ear next to the person's mouth and nose. Do you feel air on your cheek? 2)Look to see if the person's chest is moving.If the Person is Not Breathing, Check Pulse. 3)Check the person's pulse for 10 seconds.If There is No Pulse, Start CPR."]],
           [r'How to give CPR??', ['1)For an adult or child, place the heel of one hand on the center of the chest at the nipple line. You can also push with one hand on top of the other. For an infant, place two fingers on the breastbone. 2)For an adult or child, press down at least 2 inches. Make sure not to press on ribs. For an infant, press down about 1 and 1/2 inches. Make sure not to press on the end of the breastbone. 3)Do chest compressions only, at the rate of 100-120 per minute or more. Let the chest rise completely between pushes. 4)Check to see if the person has started breathing.']], 
           [r'How do you treat a Fracture?', ["1)Stop any bleeding. Apply pressure to the wound with a sterile bandage, a clean cloth or a clean piece of clothing. 2)Immobilize the injured area. Don't try to realign the bone or push a bone that's sticking out back in. If you've been trained in how to splint and professional help isn't readily available, apply a splint to the area above and below the fracture sites. Padding the splints can help reduce discomfort. 3)Apply ice packs to limit swelling and help relieve pain. Don't apply ice directly to the skin. Wrap the ice in a towel, piece of cloth or some other material. 4)Treat for shock. If the person feels faint or is breathing in short, rapid breaths, lay the person down with the head slightly lower than the trunk and, if possible, elevate the legs."]]]

print("xcbvkdf")
print(my_data)