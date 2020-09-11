# Find the 10 most frequently used words in a body of text
book = "Who Say? “All songs have been sung; All tales have been told; Live tongues are still’d-- Worn smooth by precedent!” In the fullness of the soul There lives--strong bound-- Only to be unloos’d by greater deed and action; An unfathomable wealth From which to draw forever-- Never to be wholly used. Is it for you To stand at the bier of the dead past Mute--to consent, that: “All! has been sung and writ”? No! Insistingly, Persistently beat loud upon the temple door--steeled well to hear the mock and din and laughter and deriding, doubting shouts of those within, That you may full awake the throng without-- Those who sleep, work, hope and pray. You must proclaim again, again, This Truth! The multitude at last will stand aghast, amazed, ashamed; Thy liberty deny, Yea, crucify. To them:--What is, is; and what is, is to remain unchanged forever. To learn the lesson, to equip and grade thy purging fire; Go forth to some unfrequented spot And reason with thyself, comparing notes with Nature. See it. Feel it. Hear it. The all-prevailing, pervading, constant, ever changing. From Winter’s silence, breathing, sighing, sleeping, creeping on to Spring with sap, with shoot, with bud and flower, hour on hour playing, plying gentleness and power for Summer’s rest to temper strength for birth in Autumn, with crowning brilliancy and rich rewards untaxed to bird, to beast, to insect and to man, gift on gift for full contentment, sustenance and labor. From this you will accumulate a store so full, That every thought’s a prayer; The simplest acts of things are miracles-- The whole a revelation, To guide thy way and being. Kill not, dissect not, nor rend or tear, But see and feel and hear. The earth, the air and sea abound With righteous living creatures, Intent upon some full purpose;-- Aside from man’s estate, Aside from his designing selfishness, intensely useless graspings, destruction, purposeless desire, For his good use and keeping, The forest, field and sea And all that lies beneath. But if to be a “Bard Sublime?”-- A prater, Aspiring to soar ’midst lofty peaks on painted scenes; to catch with musty mystery; with empty schemes of praise; with sheens of artificial light, spread o’er this prolonged night and sleep of letters; or with palsied moonbeams that miniature the day and blight tart speech and full-ripe reason; To buoy vanity; To bid for foolish charlatan’s esteem, To live apart at ease and shirk, Good hard holy healthy work; To mingle not with clean magnetic dirt, With healing, building sunshine, air and rain.-- Then be a heralder of “New Thought” Cite from thy store: Great Deeds And haughty interminglings; Praise, to have a share; Valor, in which words win; Chastisement, which you do not feel; Abnegation, with no self-denial. Whatever thy saying, Mark you full well That all such machinations Must and will be counted less Than Brawn-Studies in great Nature’s realm. If swept away from Nature’s gentle sway Too weak to rise and understand Thy full purpose, and the coming day:-- Then feed, feed on thy kind and kith and kin Plunge in, into the maelstrom; Amidst the deaf’ning roar, Swim ’midst molten masses, Breast cataracts of seething, living action, Tell of harnessing of power, Of screech and scream, Of whirr of wheels; Of lightning’s use and speed; Of clank and bang and whisp and twirl of rasp and plane and drill on rock and wood and metal. For therein lies a ripe, rich, unwrit story; And place the credit where the credit’s due. Use freely, and without fear thy caustic pen, Ruffle, ruthlessly pursue, dog and undo Proud spirited, designing men."

def freq_word(book):
    ## iterate through book and do not account for symbols
    # words are separated by spaces
    ## during iteration collect new words and add to a count of words
    ## add to dict
    ## sort dict
    
    word_counter = {}
    
    words = book.split(" ")
    for word in words:
        if word not in word_counter:
            word_counter[word]=1
        else:
            word_counter[word]+=1
            
    
        
    sort_word_counter = sorted(word_counter.items(), key=lambda x: x[1],
    reverse=True)
    
    #print (sort_word_counter[0:9])
    return sort_word_counter[0:9]
    
freq_word(book)
