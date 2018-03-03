from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4206_1 ._SN',
        MapName             = 'Grancel',
        Location            = 'T4206.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60000",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T4206   ._SN',
            'ED6_DT21/T4206_1 ._SN',
            '',
            '',
            '',
            '',
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 0,
        Unknown_0C              = 4,
        Unknown_0E              = 5,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 2500,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 1,
        Unknown_3A              = 1,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_73E",          # 01, 1
        "Function_2_85D",          # 02, 2
        "Function_3_90B",          # 03, 3
        "Function_4_B98",          # 04, 4
        "Function_5_E63",          # 05, 5
        "Function_6_1201",         # 06, 6
        "Function_7_128A",         # 07, 7
        "Function_8_1343",         # 08, 8
        "Function_9_178B",         # 09, 9
        "Function_10_19C6",        # 0A, 10
        "Function_11_1AAA",        # 0B, 11
        "Function_12_1B56",        # 0C, 12
        "Function_13_1BDC",        # 0D, 13
        "Function_14_1C1A",        # 0E, 14
        "Function_15_1E1F",        # 0F, 15
        "Function_16_1FC2",        # 10, 16
        "Function_17_21C5",        # 11, 17
        "Function_18_2365",        # 12, 18
        "Function_19_23DC",        # 13, 19
        "Function_20_24D6",        # 14, 20
        "Function_21_253E",        # 15, 21
        "Function_22_25AB",        # 16, 22
        "Function_23_2639",        # 17, 23
        "Function_24_266F",        # 18, 24
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 0)), scpexpr(EXPR_END)), "loc_1CC")

    ChrTalk(    #0
        0x2D,
        (
            "#843FStill, I'm feeling keenly these days just how much\x01",
            "I need to improve myself.\x02\x03",

            "I'd love to go on some kind of extensive training\x01",
            "program, but this hardly seems the time for that.\x02\x03",

            "#840FPerhaps I'll bring up the matter with Elnan once\x01",
            "things have calmed down a little.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_73A")

    label("loc_1CC")


    ChrTalk(    #1
        0x2D,
        (
            "#840FGreetings, Joshua.\x02\x03",

            "You've done some fine work these past couple\x01",
            "of weeks.\x02\x03",

            "The damage reports on the regions of Liberl\x01",
            "you've been providing have proved invaluable\x01",
            "in allocating personnel.\x02\x03",

            "I really can't thank you enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x102,
        (
            "#1040FOh, you needn't thank me...\x02\x03",

            "#1035FBy the way, Kurt...I feel like I need to say\x01",
            "something regarding my bracer badge.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0x102)
    Sleep(500)

    ChrTalk(    #3
        0x102,
        (
            "#1043FAs you probably already know, what power\x01",
            "I have was given to me by the society.\x02\x03",

            "Before becoming a bracer, I used it to commit\x01",
            "many unforgivable crimes, too...\x02\x03",

            "No matter how much I think about it, I just can't\x01",
            "see how someone like me is fit to call himself a\x01",
            "a bracer.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x2D,
        (
            "#843FYou know, Joshua...\x02\x03",

            "...I've always seen power as an imperfect\x01",
            "concept.\x02\x03",

            "And that's why I believe people are able to\x01",
            "use it.\x02\x03",

            "#842FAm I wrong?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#1044F...No, I suppose not...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x2D,
        (
            "#845FThen what difference is there between us?\x02\x03",

            "We are both keenly aware of our flaws, and yet\x01",
            "we both use what limited power we have to do\x01",
            "what we believe to be right. I see no difference.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#1054F...Well, I can't really argue with that logic.\x02\x03",

            "I still can't pretend to be completely confident\x01",
            "in myself, though...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x2D,
        (
            "#841FBe that as it may, that's nothing to be ashamed of--\x01",
            "you should simply continue striving to overcome it.\x02\x03",

            "#840FAnd while this is but my personal opinion...\x02\x03",

            "...I'd say you're a model bracer.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x20)

    label("loc_73A")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_73E(): pass

    label("Function_1_73E")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4, 1)), scpexpr(EXPR_END)), "loc_7A0")

    ChrTalk(    #9
        0x2E,
        (
            "#820FIt's wild just how much energy these two\x01",
            "have.\x02\x03",

            "Are they always like this?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_859")

    label("loc_7A0")


    ChrTalk(    #10
        0x2E,
        (
            "#821FHaha. After all the work we've been doing lately,\x01",
            "it's great to be able to come to a swanky place\x01",
            "like this and put our feet up.\x02\x03",

            "#823FThe food's pretty good, too! *munch*\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x21)

    label("loc_859")

    TalkEnd(0xFE)
    Return()

    # Function_1_73E end

    def Function_2_85D(): pass

    label("Function_2_85D")

    TalkBegin(0xFE)

    ChrTalk(    #11
        0x2F,
        (
            "#835FI swear, it's like watching two children squabble.\x02\x03",

            "It's great that we're peaceful again and all, but\x01",
            "I think these two are taking things a little TOO\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_2_85D end

    def Function_3_90B(): pass

    label("Function_3_90B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5F3, 5)), scpexpr(EXPR_END)), "loc_ACF")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_END)), "loc_9AB")

    ChrTalk(    #12
        0x19,
        (
            "#811FSeriously! They'd both look amazing in dresses\x01",
            "if they took my advice!\x02\x03",

            "Maybe they'll let me test my theory if I ask them\x01",
            "nicely!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_ACC")

    label("loc_9AB")

    OP_8C(0x19, 270, 0)

    ChrTalk(    #13
        0x19,
        (
            "#818FHmm... Well, if you ask me...\x02\x03",

            "...throw some red earrings and a little ribbon on\x01",
            "Josette, then top it off with a nice, white dress.\x02\x03",

            "Same goes for Estelle if she let her hair down.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x19, 0x102, 500)
    Sleep(300)

    ChrTalk(    #14
        0x19,
        "#816FWhat do you think, Joshua?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x102,
        "#1048FWhat are you asking me for?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x9)

    label("loc_ACC")

    Jump("loc_B94")

    label("loc_ACF")


    ChrTalk(    #16
        0x19,
        (
            "#814FWow! I didn't know Josette was from the nobility.\x02\x03",

            "I always pictured Erebonian nobles as being real\x01",
            "stuffy and scary...\x02\x03",

            "#1311FHeehee. But maybe there are a few cute ones mixed\x01",
            "in there?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_B94")

    TalkEnd(0xFE)
    Return()

    # Function_3_90B end

    def Function_4_B98(): pass

    label("Function_4_B98")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 2)), scpexpr(EXPR_END)), "loc_C9F")

    ChrTalk(    #17
        0x2B,
        (
            "#1110FSpeaking of the Republic, parliament is still\x01",
            "very much in confusion over the Orbal Shutdown\x01",
            "Phenomenon.\x02\x03",

            "To say nothing of those steam tanks of Erebonia's.\x02\x03",

            "It's going to be quite a while before things \x01",
            "settle down there, too, I'd wager.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E5F")

    label("loc_C9F")


    ChrTalk(    #18
        0x2B,
        (
            "#1111FIt's nice to be able to attend a banquet like this.\x02\x03",

            "It truly drives home the point that this nation is\x01",
            "back at peace again.\x02\x03",

            "#1113FThe trouble regarding the Liber Ark and subsequent\x01",
            "restoration efforts have really shown me anew how\x01",
            "capable a ruler Queen Alicia is.\x02\x03",

            "She's handled all that's happened impeccably.\x02\x03",

            "If all of this had happened in the Republic,\x01",
            "it wouldn't have been resolved anywhere near\x01",
            "as smoothly, let me tell you.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A)

    label("loc_E5F")

    TalkEnd(0xFE)
    Return()

    # Function_4_B98 end

    def Function_5_E63(): pass

    label("Function_5_E63")

    OP_4A(0x26, 0)
    OP_4A(0x27, 0)
    TurnDirection(0x26, 0x102, 0)
    TurnDirection(0x27, 0x102, 0)
    Sleep(300)

    ChrTalk(    #19
        0x26,
        "#221FAh! Just the man, just the man!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1044F#2PPardon...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x27,
        (
            "#1101FOh?\x02\x03",

            "Is this the boy you were speaking of earlier?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x26,
        (
            "#225FThat's correct. This is Joshua.\x02\x03",

            "#220FI was just telling the ambassador here about\x01",
            "your various accomplishments, Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x27,
        (
            "#1100FIt's an honor to finally meet you.\x02\x03",

            "I'm the resident Erebonian ambassador here\x01",
            "in Liberl, Davil Crainagh.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x102,
        "#1054F#2PI-It's nice to meet you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x27,
        (
            "#1102FThe tale of how you flew on top of that flying city\x01",
            "all while knowing it may be the last thing you did\x01",
            "brought tears to my eyes.\x02\x03",

            "How you were able to participate in an operation\x01",
            "that may have brought your death, casting aside \x01",
            "even your girlfriend's objections, I don't know...\x02\x03",

            "#1100F...but I know this: Liberl needs more young men and\x01",
            "women like you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1049F#2PTh-Thank you for saying so, sir...\x02\x03",

            "(Just what has the duke been telling him?)\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x26, 180, 0)
    OP_8C(0x27, 0, 0)
    OP_4B(0x26, 0)
    OP_4B(0x27, 0)
    Return()

    # Function_5_E63 end

    def Function_6_1201(): pass

    label("Function_6_1201")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 5)), scpexpr(EXPR_END)), "loc_127C")
    OP_8C(0x26, 180, 0)

    ChrTalk(    #27
        0x26,
        (
            "#225FBut all was well that ended well, for by \x01",
            "miraculous chance, the two were able to\x01",
            "reunite...\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1286")

    label("loc_127C")

    Call(1, 5)
    OP_A2(0x15)
    OP_A2(0x16)

    label("loc_1286")

    TalkEnd(0xFE)
    Return()

    # Function_6_1201 end

    def Function_7_128A(): pass

    label("Function_7_128A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2, 6)), scpexpr(EXPR_END)), "loc_132E")

    ChrTalk(    #28
        0x27,
        (
            "#1102FIt should go without saying how touched\x01",
            "I am to see such spirit from our youths of\x01",
            "today.\x02\x03",

            "#1100FYou are truly Liberl's greatest treasures.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_133F")

    label("loc_132E")

    OP_8C(0xFE, 0, 0)
    Call(1, 5)
    OP_A2(0x15)
    OP_A2(0x16)

    label("loc_133F")

    TalkEnd(0xFE)
    Return()

    # Function_7_128A end

    def Function_8_1343(): pass

    label("Function_8_1343")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 2)), scpexpr(EXPR_END)), "loc_1413")

    ChrTalk(    #29
        0x1D,
        (
            "#115FThanks to Brigadier General Bright's mercy,\x01",
            "I was able to receive a full pardon for my\x01",
            "actions...\x02\x03",

            "...but I still feel as though I need to settle things\x01",
            "within myself after what I did.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1787")

    label("loc_1413")


    ChrTalk(    #30
        0x102,
        "#1040FYou were able to make it, Richard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x1D,
        (
            "#110FThanks to Brigadier General Bright's generosity,\x01",
            "yes.\x02\x03",

            "I've received an official pardon from Her Majesty\x01",
            "for my actions.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x102,
        (
            "#1040FProbably for foiling the society's attack\x01",
            "on Grancel, right?\x02\x03",

            "That's good news. I'm happy for you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x1D,
        (
            "#115FI wish I could say the same...but I don't feel\x01",
            "as though I deserve to be pardoned at all.\x02\x03",

            "Now that the nation is at peace, I feel this is\x01",
            "the time I should be facing up to my crimes--\x01",
            "not having them swept under the rug.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x102,
        "#1043FI can't say I don't understand, but still...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x1D,
        (
            "#111FHaha. Please, Joshua. You needn't look so\x01",
            "concerned.\x02\x03",

            "#115FI have no intention of refusing Her Majesty's \x01",
            "kindness or going against her will.\x02\x03",

            "I merely feel a strong desire to settle things\x01",
            "within myself, and I fully intend on following\x01",
            "through.\x02\x03",

            "#110FThat is all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x102,
        "#1040F...All right, then.\x02",
    )

    CloseMessageWindow()
    OP_A2(0xA)

    label("loc_1787")

    TalkEnd(0xFE)
    Return()

    # Function_8_1343 end

    def Function_9_178B(): pass

    label("Function_9_178B")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 6)), scpexpr(EXPR_END)), "loc_181C")

    ChrTalk(    #37
        0x1F,
        (
            "#183FI-I presume your business here is finished?\x01",
            "Then kindly begone.\x02\x03",

            "You'll get in His Excellency's way standing\x01",
            "around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19C2")

    label("loc_181C")


    ChrTalk(    #38
        0x102,
        (
            "#1044FOh. I wasn't expecting to find you here...\x02\x03",

            "#1040FStill, thank you very much for your support\x01",
            "during the attack on Grancel. It really did\x01",
            "help us all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1F,
        (
            "#183FOh, please. I only did what I did because it\x01",
            "was one of His Excellency's bail conditions.\x02\x03",

            "Make no mistake: I wouldn't have helped any\x01",
            "of you worthless drecks otherwise.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#1048F(You wouldn't think it would be so hard to\x01",
            "accept a thank you...)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0xE)

    label("loc_19C2")

    TalkEnd(0xFE)
    Return()

    # Function_9_178B end

    def Function_10_19C6(): pass

    label("Function_10_19C6")

    TalkBegin(0x2A)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3, 1)), scpexpr(EXPR_END)), "loc_19EB")

    ChrTalk(    #41
        0x2A,
        "#311FScree! Scree!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1AA6")

    label("loc_19EB")


    ChrTalk(    #42
        0x2A,
        "#310FScree! Scree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x102,
        "#1040FWell, well, Sieg! It's good to see you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x2A,
        "#311FScreeeee! ☆\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x102,
        (
            "#1054F(After all he did, I'd say he deserves a good\x01",
            "party as much as any human.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x19)

    label("loc_1AA6")

    TalkEnd(0x2A)
    Return()

    # Function_10_19C6 end

    def Function_11_1AAA(): pass

    label("Function_11_1AAA")

    TalkBegin(0xFE)

    ChrTalk(    #46
        0xFE,
        (
            "It was an honor to be able to put my skills to\x01",
            "the test making tonight's many dishes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "I do hope they will be to your satisfaction.\x01",
            "Please, have your fill.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_11_1AAA end

    def Function_12_1B56(): pass

    label("Function_12_1B56")

    TalkBegin(0xFE)

    ChrTalk(    #48
        0xFE,
        "Is there enough food available for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xFE,
        (
            "If there's anything you would like more of,\x01",
            "please feel free to let me know.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_12_1B56 end

    def Function_13_1BDC(): pass

    label("Function_13_1BDC")

    TalkBegin(0xFE)
    OP_8C(0xFE, 180, 0)

    ChrTalk(    #50
        0xFE,
        "U-Umm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xFE,
        "Could you two stop fighting?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_13_1BDC end

    def Function_14_1C1A(): pass

    label("Function_14_1C1A")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 5)), scpexpr(EXPR_END)), "loc_1D0C")

    ChrTalk(    #52
        0xFE,
        (
            "I normally work as a chef over at Sanktheim Gate,\x01",
            "but I was called over here to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "It's a real huge honor to be able to help out at\x01",
            "an occasion this spectacular. I doubt I'll ever\x01",
            "get an opportunity like THIS again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1E1B")

    label("loc_1D0C")


    ChrTalk(    #54
        0xFE,
        "Man, this is one hell of a party!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "I normally work as a chef over at Sanktheim Gate,\x01",
            "but I was called over here to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "It's a real huge honor to be able to help out at\x01",
            "an occasion this spectacular. I doubt I'll ever\x01",
            "get an opportunity like THIS again.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2D)

    label("loc_1E1B")

    TalkEnd(0xFE)
    Return()

    # Function_14_1C1A end

    def Function_15_1E1F(): pass

    label("Function_15_1E1F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 6)), scpexpr(EXPR_END)), "loc_1EAE")

    ChrTalk(    #57
        0xFE,
        "You're always welcome to the castle, Joshua.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xFE,
        (
            "I'd be more than happy to help you get dolled\x01",
            "up for the occasion, too. ㈱\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1FBE")

    label("loc_1EAE")


    ChrTalk(    #59
        0xFE,
        "Oh!\x02",
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #60
        0xFE,
        (
            "You're always welcome back to the castle\x01",
            "any time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        (
            "I'd be more than happy to help you get dolled\x01",
            "up for the occasion, too. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #62
        0x102,
        (
            "#1048FI'm never wearing a maid outfit again. Just so\x01",
            "you know.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2E)

    label("loc_1FBE")

    TalkEnd(0xFE)
    Return()

    # Function_15_1E1F end

    def Function_16_1FC2(): pass

    label("Function_16_1FC2")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x5, 7)), scpexpr(EXPR_END)), "loc_2085")

    ChrTalk(    #63
        0xFE,
        (
            "Now that everything's back to normal, it feels\x01",
            "like all that happened that day was some sort\x01",
            "of dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "Dream or real life, though, I'm just relieved it's\x01",
            "all finally over.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_21C1")

    label("loc_2085")


    ChrTalk(    #65
        0xFE,
        (
            "*sigh* Now that everything's back to normal,\x01",
            "it feels like all that happened that day was\x01",
            "some sort of dream.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        (
            "I'd certainly rather believe it was... Seeing the \x01",
            "castle gates fall and those scary people charging\x01",
            "through was like a nightmare...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        "I thought I was going to faint at the sight of it all.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2F)

    label("loc_21C1")

    TalkEnd(0xFE)
    Return()

    # Function_16_1FC2 end

    def Function_17_21C5(): pass

    label("Function_17_21C5")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 0)), scpexpr(EXPR_END)), "loc_2282")

    ChrTalk(    #68
        0xFE,
        (
            "I don't know what those society people were trying\x01",
            "to achieve by causing us so much trouble...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xFE,
        (
            "...but that was an experience I hope I never have to\x01",
            "go through again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2361")

    label("loc_2282")


    ChrTalk(    #70
        0xFE,
        (
            "Holding a party like this makes it feel like peace\x01",
            "has finally returned to the castle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        (
            "It certainly hasn't felt like that in the days leading\x01",
            "up to it. We were all busy clearing things up until\x01",
            "a few days ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x30)

    label("loc_2361")

    TalkEnd(0xFE)
    Return()

    # Function_17_21C5 end

    def Function_18_2365(): pass

    label("Function_18_2365")

    TalkBegin(0xFE)

    ChrTalk(    #72
        0xFE,
        (
            "Right! Next up, I need to give that guest their\x01",
            "drink...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xFE,
        "Umm... But what did I need to do after that?\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_18_2365 end

    def Function_19_23DC(): pass

    label("Function_19_23DC")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x6, 1)), scpexpr(EXPR_END)), "loc_242B")

    ChrTalk(    #74
        0xFE,
        "Erm... Excuse me...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xFE,
        "Have I given you some food already?\x02",
    )

    CloseMessageWindow()
    Jump("loc_24D2")

    label("loc_242B")


    ChrTalk(    #76
        0xFE,
        "Whew... There sure are a lot of guests today!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        (
            "By all means, help yourself to any of the food\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0xFE,
        "It'll all taste much better while it's still hot!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x31)

    label("loc_24D2")

    TalkEnd(0xFE)
    Return()

    # Function_19_23DC end

    def Function_20_24D6(): pass

    label("Function_20_24D6")

    TalkBegin(0xFE)

    ChrTalk(    #79
        0xFE,
        "Do you need something to drink, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xFE,
        "We have plenty available, alcoholic or otherwise.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_20_24D6 end

    def Function_21_253E(): pass

    label("Function_21_253E")

    TalkBegin(0xFE)

    ChrTalk(    #81
        0xFE,
        (
            "We're delighted to see you were able\x01",
            "to attend tonight's banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0xFE,
        "Please do enjoy yourself.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_21_253E end

    def Function_22_25AB(): pass

    label("Function_22_25AB")

    TalkBegin(0xFE)

    ChrTalk(    #83
        0xFE,
        (
            "The whole garden terrace is accessible to\x01",
            "guests of tonight's party.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "So please don't feel restricted, and do enjoy\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_22_25AB end

    def Function_23_2639(): pass

    label("Function_23_2639")

    TalkBegin(0xFE)

    ChrTalk(    #85
        0xFE,
        "Please, do enjoy yourself at the banquet.\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_23_2639 end

    def Function_24_266F(): pass

    label("Function_24_266F")

    TalkBegin(0xFE)

    ChrTalk(    #86
        0xFE,
        (
            "I'm terribly sorry, but I'm afraid you may not\x01",
            "pass beyond this point. These stairs lead to\x01",
            "Her Highness' private chamber.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xFE)
    Return()

    # Function_24_266F end

    SaveToFile()

Try(main)
