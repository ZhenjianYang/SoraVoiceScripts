from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2131_1 ._SN',
        MapName             = 'Ruan',
        Location            = 'T2131.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            '',
            '',
            '',
            '',
            '',
            '',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
    )

    DeclEntryPoint(
        Unknown_00              = 0,
        Unknown_04              = 0,
        Unknown_08              = 6000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 9500,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 2800,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 0,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_835",          # 01, 1
        "Function_2_378F",         # 02, 2
        "Function_3_69D9",         # 03, 3
        "Function_4_8803",         # 04, 4
        "Function_5_BB20",         # 05, 5
        "Function_6_BB50",         # 06, 6
        "Function_7_BB85",         # 07, 7
        "Function_8_BBB5",         # 08, 8
        "Function_9_BBDD",         # 09, 9
        "Function_10_BBE5",        # 0A, 10
        "Function_11_BBED",        # 0B, 11
        "Function_12_BBF5",        # 0C, 12
        "Function_13_BBFD",        # 0D, 13
        "Function_14_BC05",        # 0E, 14
        "Function_15_BC42",        # 0F, 15
        "Function_16_BC86",        # 10, 16
        "Function_17_BCE0",        # 11, 17
        "Function_18_BD5E",        # 12, 18
        "Function_19_C7B5",        # 13, 19
        "Function_20_CE71",        # 14, 20
        "Function_21_CEBD",        # 15, 21
        "Function_22_CEF8",        # 16, 22
        "Function_23_CF1C",        # 17, 23
        "Function_24_CF40",        # 18, 24
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x280, 0)), scpexpr(EXPR_END)), "loc_4AD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_1FB")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_128")

    ChrTalk(    #0
        0xFE,
        "Really, thanks for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "If anything else happens, I'll be\x01",
            "sure to look you guys up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F8")

    label("loc_128")


    ChrTalk(    #2
        0xFE,
        (
            "Until then, I'm parking my butt right\x01",
            "here until my husband walks down\x01",
            "those stairs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "Even if he decides to keep playing\x01",
            "till he's got nothing left, the casino will\x01",
            "show him what's what soon enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8")

    Jump("loc_4AA")

    label("loc_1FB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_END)), "loc_369")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_296")

    ChrTalk(    #4
        0xFE,
        (
            "I'm sorry, I know this isn't the\x01",
            "most normal request you've taken\x01",
            "on.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        (
            "I'll let you know if anything else\x01",
            "happens, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_366")

    label("loc_296")


    ChrTalk(    #6
        0xFE,
        (
            "Until then, I'm parking my butt right\x01",
            "here until my husband walks down\x01",
            "those stairs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Even if he decides to keep playing\x01",
            "till he's got nothing left, the casino will\x01",
            "show him what's what soon enough.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_366")

    Jump("loc_4AA")

    label("loc_369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x2)"), scpexpr(EXPR_END)), "loc_382")
    TalkEnd(0xFE)
    EventBegin(0x0)
    Call(1, 1)
    EventEnd(0x0)
    Return()

    label("loc_382")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_3B8")

    ChrTalk(    #8
        0xFE,
        (
            "Please, you've got to stop my\x01",
            "husband!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4AA")

    label("loc_3B8")

    OP_A2(0x7)

    ChrTalk(    #9
        0xFE,
        "Ahh, what do I do...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "My husband up and decided out of\x01",
            "nowhere that he wants to pursue a\x01",
            "full-time career in gambling.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "It's about the stupidest thing I've ever\x01",
            "heard coming from that mouth of his!\x01",
            "Someone, ANYONE, stop him!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4AA")

    Jump("loc_831")

    label("loc_4AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_END)), "loc_67A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_55D")

    ChrTalk(    #12
        0xFE,
        (
            "I couldn't stand watching and\x01",
            "came down to the first floor.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xFE,
        (
            "Oh, what I wouldn't give for the\x01",
            "staff here to put a stop to this idiotic\x01",
            "scheme of his.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_677")

    label("loc_55D")

    OP_A2(0x7)

    ChrTalk(    #14
        0xFE,
        (
            "*sigh* What am I going to do...?\x01",
            "My husband's such a fool.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I know him better than anyone, and he\x01",
            "always gets carried away. Won't be too\x01",
            "long before he declares himself a pro!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Oh, what I wouldn't give for the\x01",
            "staff here to put a stop to this idiotic\x01",
            "scheme of his.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_677")

    Jump("loc_831")

    label("loc_67A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 4)), scpexpr(EXPR_END)), "loc_6DD")

    ChrTalk(    #17
        0xFE,
        (
            "How strange.\x01",
            "There's no one in the store...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        "I wonder where the bartender went.\x02",
    )

    CloseMessageWindow()
    Jump("loc_831")

    label("loc_6DD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x242, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 2)), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_831")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_772")

    ChrTalk(    #19
        0xFE,
        (
            "I'm going to have to put a stop\x01",
            "to his gambling fun at some point,\x01",
            "though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0xFE,
        (
            "That man of mine never knows\x01",
            "when to quit.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_831")

    label("loc_772")

    OP_A2(0x7)

    ChrTalk(    #21
        0xFE,
        (
            "Slots are fun. All I did was mess\x01",
            "around a little bit and I won!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0xFE,
        (
            "My husband's on a winning streak, too.\x01",
            "I'm crossing my fingers that we go home\x01",
            "with more mira than when we left.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_831")

    TalkEnd(0xFE)
    Return()

    # Function_0_AA end

    def Function_1_835(): pass

    label("Function_1_835")

    OP_4A(0xE, 0)
    Fade(1000)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_0D()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_8EB")

    ChrTalk(    #23
        0xE,
        (
            "Oh, thank goodness!\x01",
            "You're back.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0xE,
        "Are you ready to hear me out?\x02",
    )

    CloseMessageWindow()
    Jump("loc_A2F")

    label("loc_8EB")


    ChrTalk(    #25
        0x101,
        (
            "#1011F#6PUm, may we have a moment?\x02\x03",

            "You wouldn't happen to be\x01",
            "Lakeisha, would you?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #26
        0xE,
        (
            "Yes, I'm Lakeish--\x01",
            "Oh!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xE,
        "Are you the bracers?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        "#1000F#6PYeah, we saw the posting.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xE,
        (
            "Good. You know a little bit of\x01",
            "what's going on, at least.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0xE,
        (
            "Are you all set?\x01",
            "I'd like to go over the details.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_A2F")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Yes\x01",      # 0
            "No\x01",       # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C71")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_B7B")

    ChrTalk(    #31
        0x101,
        (
            "#1015F#6PSorry.\x02\x03",

            "We're still a little busy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xE,
        (
            "Not even for a minute?\x01",
            "*sigh*\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xE,
        (
            "I know bracers are busy people, but\x01",
            "come back soon, okay? Remember,\x01",
            "my marriage is at stake here!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        (
            "#1000F#6PDon't worry, we will.\x01",
            "Sorry again, Lakeisha.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C63")

    label("loc_B7B")


    ChrTalk(    #35
        0x101,
        (
            "#1007F#6PSorry...\x02\x03",

            "We sort of can't right now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xE,
        "Oh, you can't?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xE,
        (
            "Well, come back here once your\x01",
            "schedule's opened up, okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xE,
        (
            "The future of our marriage depends\x01",
            "on you!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1000F#6PN-No worries. We'll be back\x01",
            "soon.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C63")

    OP_28(0x68, 0x1, 0x8000)
    OP_4B(0xE, 0)
    Return()

    label("loc_C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8000)"), scpexpr(EXPR_END)), "loc_D04")

    ChrTalk(    #40
        0x101,
        (
            "#1006F#6PYeah, we've been keeping you\x01",
            "waiting long enough, haven't we?\x01",
            "Sorry about that, Lakeisha.\x02\x03",

            "So, what can we do for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D4A")

    label("loc_D04")


    ChrTalk(    #41
        0x101,
        (
            "#1006F#6PYeah, of course it's okay.\x02\x03",

            "So, what can we do for you?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_D4A")

    OP_4A(0xD, 0)
    OP_4A(0xB, 0)
    OP_28(0x68, 0x1, 0x1)
    OP_28(0x68, 0x1, 0x2)

    ChrTalk(    #42
        0xE,
        (
            "What I'd like to ask of you is\x01",
            "very simple.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xE,
        (
            "Do something, ANYTHING, to make\x01",
            "my husband lose at gambling!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x2, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x3, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #44
        0x101,
        "#1004F#6P...Uh, what?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_E71")

    ChrTalk(    #45
        0x106,
        "#052FThat's it?\x02",
    )

    CloseMessageWindow()
    Jump("loc_E90")

    label("loc_E71")


    ChrTalk(    #46
        0x103,
        "#023FThat's your request?\x02",
    )

    CloseMessageWindow()

    label("loc_E90")


    ChrTalk(    #47
        0x104,
        (
            "#033FWin in a game of chance, is it?\x01",
            "A most intriguing request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xE,
        (
            "You heard me right. I don't care\x01",
            "what game, just please, win against\x01",
            "my husband.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0xE,
        (
            "He's always been the type to get so\x01",
            "wrapped up in whatever it is he's doing\x01",
            "that he doesn't know when to stop.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xE,
        (
            "I mean, really? He gets a few wins\x01",
            "in at the casino and suddenly he's\x01",
            "convinced he's a pro gambler!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xE,
        (
            "And I know that one-track mind of his--\x01",
            "if he says he wants to turn pro, anything\x01",
            "I say is in one ear and out the other.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xE,
        (
            "So I'd like you to nip that in the bud\x01",
            "before things go that far.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1016F#6PAh...haha. I see.\x02\x03",

            "Family circumstances, huh?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_113D")

    ChrTalk(    #54
        0x106,
        "#551FLooks like you've got it rough.\x02",
    )

    CloseMessageWindow()
    Jump("loc_116C")

    label("loc_113D")


    ChrTalk(    #55
        0x103,
        (
            "#026FSounds like things are hard\x01",
            "for you.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_116C")


    ChrTalk(    #56
        0xE,
        "No, I was naive.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xE,
        (
            "I should have just refused when\x01",
            "he suggested a casino trip...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xE,
        (
            "*sigh*\x01",
            "No point in complaining now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xE,
        (
            "Here, let me give you 1000 mira\x01",
            "as a wager.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #60
        "Received #4C1000#0C mira.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #61
        0xE,
        (
            "If you wager this all on one bet,\x01",
            "I'm sure my husband will take\x01",
            "you up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x105,
        (
            "#044FI sure hope so.\x02\x03",

            "Is your husband upstairs\x01",
            "at the casino right now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xE,
        (
            "Yes, he's made himself\x01",
            "nice and comfortable up there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xE,
        (
            "Last I saw, he was playing cards.\x01",
            "Phelio's his name.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1000F#6PUnderstood. We'll check the\x01",
            "card tables.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xE,
        (
            "Do me a favor and don't hold back.\x01",
            "Make sure he loses decisively.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xE,
        (
            "Is there anything else I can help\x01",
            "you with? Any questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1015F#6PWe're okay, I think.\x01",
            "You've covered all the basics.\x02\x03",

            "The real question is, how do we\x01",
            "win the match?\x02\x03",

            "I mean, gambling's ultimately luck,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xF7, 90, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1561")

    ChrTalk(    #69
        0x106,
        (
            "#050FYeah, but lettin' that luck live or\x01",
            "killin' it takes skill.\x02\x03",

            "Whether we can win or not depends\x01",
            "on your match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_15EA")

    label("loc_1561")


    ChrTalk(    #70
        0x103,
        (
            "#027FYes, but only to a degree.\x01",
            "Letting that luck live or killing\x01",
            "it takes skill.\x02\x03",

            "Whether we can win or not depends\x01",
            "on your match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_15EA")


    ChrTalk(    #71
        0x104,
        "#031FStrategy is the key, to be more precise.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 180, 400)

    ChrTalk(    #72
        0x101,
        (
            "#1015FHmmm... Guess we're in for some\x01",
            "fun times.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xE,
        (
            "If strategy's what you're worried\x01",
            "about, you'll be fine. My husband\x01",
            "is a total amateur.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0xE,
        (
            "He's terrible at lying! Every thought\x01",
            "that crosses his mind is written on\x01",
            "his face plain as day.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0xE,
        (
            "He's not normally the kind of\x01",
            "person well-suited to gambling.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 0, 400)

    ChrTalk(    #76
        0x101,
        (
            "#1011F#6PAh, really?\x02\x03",

            "#1006FHearing that makes me feel a little\x01",
            "bit more confident. Maybe.\x02\x03",

            "All right! Let's do this thing!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1864")

    ChrTalk(    #77
        0x106,
        (
            "#051FThat's the spirit.\x02\x03",

            "Nobody's ever won a game by\x01",
            "actin' like a sore loser before the\x01",
            "match even started.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18F9")

    label("loc_1864")


    ChrTalk(    #78
        0x103,
        (
            "#020FYeah! That's the spirit.\x02\x03",

            "Knowing the game is important, sure,\x01",
            "but having the drive to get in there\x01",
            "and win is what really brings it home.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_18F9")


    ChrTalk(    #79
        0xE,
        "I'm in your corner, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #80
        0xE,
        (
            "Now, get up there and knock my\x01",
            "husband down a few pegs!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_20(0x3E8)
    SoundLoad(254)
    SoundLoad(256)
    SoundLoad(663)
    SetChrPos(0xD, 32530, 0, 29680, 79)
    SetChrPos(0x101, 29280, 0, 35000, 180)
    SetChrPos(0xF7, 30180, 0, 35430, 180)
    SetChrPos(0x104, 28980, 0, 36040, 180)
    SetChrPos(0x105, 29800, 0, 36620, 180)
    OP_6D(28300, 0, 25990, 0)
    OP_6C(332000, 0)

    def lambda_19EC():
        OP_6D(29350, 0, 36160, 4000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_19EC)

    def lambda_1A04():
        OP_6C(315000, 4000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_1A04)
    OP_21()
    OP_1D(0x19)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()
    WaitChrThread(0x0, 0x1)
    WaitChrThread(0x0, 0x2)
    Sleep(400)

    ChrTalk(    #81
        0x104,
        (
            "#030FWhat a charming little casino!\x02\x03",

            "Its equipment looks brand new.\x01",
            "Was this established recently?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x105,
        (
            "#040FIn a way. It just reopened after\x01",
            "renovations during the Birthday\x01",
            "Celebration.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x101,
        (
            "#1011FHey, now that I think about it,\x01",
            "it was being worked on last time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x104,
        (
            "#035FI see.\x02\x03",

            "#033FSo, where is our high-rolling target?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x101,
        (
            "#1015FRight. His wife said he'd be at the\x01",
            "card tables...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    OP_62(0xF7, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xF7, 0xB, 400)
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1BFB")

    ChrTalk(    #86
        0x106,
        "#050FHmph. Bingo.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1C2F")

    label("loc_1BFB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1C2F")

    ChrTalk(    #87
        0x103,
        "#020FI'm pretty sure that would be him.\x02",
    )

    CloseMessageWindow()

    label("loc_1C2F")


    def lambda_1C35():
        TurnDirection(0x101, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1C35)
    Sleep(100)

    def lambda_1C48():
        TurnDirection(0x105, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_1C48)
    Sleep(50)

    def lambda_1C5B():
        TurnDirection(0x104, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x104, 1, lambda_1C5B)
    OP_4A(0xD, 255)
    OP_4A(0xB, 255)
    OP_6D(32170, 0, 30500, 2000)

    ChrTalk(    #88
        0xD,
        "#1PAllll right, come on, come on!\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2500)
    OP_63(0xD)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x320, 0x2EE0)

    ChrTalk(    #89
        0xD,
        "#3S#1PThere it is! Jack!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xD,
        (
            "#1POoooooh, this power on the draw!\x01",
            "I feel INVINCIBLE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0xB,
        "#2PIt is your win, sir.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xD,
        (
            "#1PKnow that you fought well,\x01",
            "my good man. I'm afraid you just\x01",
            "had the wrong opponent.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0xD,
        "#1PHa ha ha ha ha ha!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    OP_6D(29520, 0, 35790, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #94
        0x101,
        (
            "#1007FYep. He's exactly as she said.\x02\x03",

            "That's gotta be him.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_1ECA")

    ChrTalk(    #95
        0x106,
        (
            "#050FQuick, let's talk to him.\x02\x03",

            "If we waste any time, he's bound to\x01",
            "get wrapped up in another match.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F41")

    label("loc_1ECA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_1F41")

    ChrTalk(    #96
        0x103,
        (
            "#020FLet's catch his attention quickly.\x02\x03",

            "If we waste time, no doubt he'll get\x01",
            "wrapped up in another match.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F41")


    ChrTalk(    #97
        0x101,
        "#1002FAhh, right.\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_43(0x101, 0x1, 0x1, 0x5)
    Sleep(100)
    OP_43(0x104, 0x1, 0x1, 0x7)
    Sleep(400)
    OP_43(0xF7, 0x1, 0x1, 0x6)
    Sleep(200)
    OP_43(0x105, 0x1, 0x1, 0x8)
    Sleep(400)
    Fade(1000)
    OP_6D(32170, 0, 30500, 0)
    OP_6D(31090, 0, 31350, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #98
        0xD,
        "#5POkay, hit me agai--!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x101, 0x1)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 400)
    Sleep(1000)

    ChrTalk(    #99
        0xD,
        "#5PHuh? What's up with you guys?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        (
            "#1006F#6PWe've heard you know your\x01",
            "way around a card game, mister.\x02\x03",

            "So we'd like to challenge you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xD,
        "#5PChallenge? ME?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0xD,
        (
            "#5PAll right, I'll bite.\x01",
            "Question is, do you have the mira?\x01",
            "I'm not taking any cheap bets.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2147")

    ChrTalk(    #103
        0x106,
        (
            "#050F#4PThe wager's 1000 mira.\x01",
            "Rich enough for you?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217E")

    label("loc_2147")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_217E")

    ChrTalk(    #104
        0x103,
        "#027F#4PThe wager's 1000 mira. How's that?\x02",
    )

    CloseMessageWindow()

    label("loc_217E")


    ChrTalk(    #105
        0xD,
        (
            "#5PHeh, that's a mighty wager.\x01",
            "Fearless, aren't ya?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xD,
        "#5PFine, I'll take you guys on.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xD,
        (
            "#5POkay, so which one of you's\x01",
            "gonna be my opponent?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0xD,
        (
            "#5POr maybe all three of you wanna have\x01",
            "a piece of the Phelimaster at the same\x01",
            "time? That works, too. I'm feelin' lucky.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        (
            "#1016F#6PA-All at once is a bit crazy...\x01",
            "We're not playing old maid here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    OP_6D(32240, 0, 31870, 1000)

    ChrTalk(    #110
        0xB,
        (
            "#2PIn that case, good customers,\x01",
            "how would you like to try a variant\x01",
            "of poker?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xB,
        (
            "#2PThere are a few that allow a match\x01",
            "to be settled over several rounds.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_23AE():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_23AE)
    Sleep(100)

    def lambda_23C1():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_23C1)

    def lambda_23CF():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_23CF)
    Sleep(150)

    def lambda_23E2():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_23E2)
    TurnDirection(0xD, 0xB, 400)
    Sleep(400)

    ChrTalk(    #112
        0x101,
        (
            "#1004FSounds like just what we're\x01",
            "looking for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xD,
        "#5PI'll say. What are the rules?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xB,
        (
            "#2PBoth sides choose a lineup of\x01",
            "contenders and settle the match\x01",
            "over three rounds.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0xB,
        (
            "#2PEach round is normal poker,\x01",
            "and the first team to win one\x01",
            "match wins.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xB,
        (
            "#2PHowever, your team can only\x01",
            "'fold' one time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xB,
        (
            "#2PIf one team member folds, the rest\x01",
            "have no choice but to challenge.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0xD,
        "#5PAnd it's a three-round match, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xD,
        "#5PSimple. Quick. Elegant. I like it.\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xD, 0x101, 400)
    OP_6D(30280, 0, 32090, 1000)

    ChrTalk(    #120
        0xD,
        (
            "Only problem now is that there's\x01",
            "four of you.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #121
        0x101,
        (
            "#1006F#5PIt's not like all four of us need to\x01",
            "play.\x02\x03",

            "One of us can sit this one out.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0xD, 400)

    ChrTalk(    #122
        0x105,
        (
            "#043F#6PThat's perfect, actually.\x02\x03",

            "If I can, I'd like to be the one\x01",
            "to sit out.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    def lambda_270A():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_270A)

    def lambda_2718():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2718)

    def lambda_2726():
        TurnDirection(0xFE, 0x105, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2726)
    TurnDirection(0x0, 0x105, 400)

    ChrTalk(    #123
        0x101,
        "#1004F#5PYou sure, Kloe?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x105,
        (
            "#043F#6PStudents are forbidden to gamble\x01",
            "by school rules.\x02\x03",

            "I don't want you to think I'm trying\x01",
            "to skip out on our job, but it is kind\x01",
            "of...awkward for me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x101,
        (
            "#1016F#5PAhaha, no, I get where you're\x01",
            "coming from.\x02\x03",

            "Gambling's not exactly a healthy\x01",
            "part of your daily balanced school\x01",
            "curriculum.\x02\x03",

            "#1000FWe can handle it from here,\x01",
            "so take a load off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x105,
        "#047F#6PSorry for the mix-up.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xD, 400)

    ChrTalk(    #127
        0x104,
        (
            "#030F#3PAnd then there were three.\x01",
            "We're well on the road to a climactic\x01",
            "three-round match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0xD,
        (
            "Not that it would matter if there\x01",
            "were four or even five matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xD,
        "I'd win 'em all, anyway.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0xB,
        (
            "Are you satisfied with the rules\x01",
            "as I explained them?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_29E6():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_29E6)

    def lambda_29F4():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_29F4)

    def lambda_2A02():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2A02)

    def lambda_2A10():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2A10)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #131
        0xD,
        "Yeah, I'm okay with 'em.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_2A70")

    ChrTalk(    #132
        0x106,
        "#050F#6PSure, we don't mind either.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2A9A")

    label("loc_2A70")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_2A9A")

    ChrTalk(    #133
        0x103,
        "#020F#6PYes, we're fine, too.\x02",
    )

    CloseMessageWindow()

    label("loc_2A9A")


    ChrTalk(    #134
        0xB,
        (
            "Well, then, allow me a few moments\x01",
            "to make preparations.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xB,
        (
            "During that time, good guests,\x01",
            "please decide the order of your\x01",
            "matches.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x101,
        (
            "#1000FOrder? So who's gonna go first\x01",
            "and stuff?\x02\x03",

            "That shouldn't take us too long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xB,
        "Thank you very much.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x101, 400)

    ChrTalk(    #138
        0xD,
        "I'm ready whenever you guys are.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x10)
    OP_43(0xB, 0x1, 0x1, 0x14)
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x105, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_2C12():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_2C12)
    Sleep(100)

    def lambda_2C25():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x2, 1, lambda_2C25)
    Sleep(150)

    def lambda_2C38():
        TurnDirection(0xFE, 0x19, 400)
        ExitThread()

    QueueWorkItem(0x3, 1, lambda_2C38)
    TurnDirection(0x0, 0x105, 400)

    def lambda_2C4D():
        OP_8C(0xD, 90, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C4D)
    OP_69(0x105, 0x5DC)

    ChrTalk(    #139
        0x101,
        (
            "#1015FAll right, order time.\x02\x03",

            "How do we want to do this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x104,
        (
            "#035F#3PMight I suggest that we pick based\x01",
            "on our gambling prowess?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_3226")

    ChrTalk(    #141
        0x101,
        (
            "#1019FUh, full disclosure, guys. I have, like,\x01",
            "zero confidence in my card skills.\x02\x03",

            "I always, ALWAYS lost to Joshua.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x106,
        (
            "#053F#4PIt's been a while since I left\x01",
            "gambling behind myself.\x02\x03",

            "#050FBut, hey, this contest is all willpower.\x01",
            "I can make do.\x02\x03",

            "How about you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x104,
        (
            "#031F#3PWorry not; I'm a man who's rife\x01",
            "with confidence in my card game.\x02\x03",

            "Leave the center to me, for I am\x01",
            "certain I can play it well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0x106,
        "#050F#4PI'm good with that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1002FThat's one down. Olivier's second.\x02\x03",

            "It's between me and you now,\x01",
            "Agate.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #146
        0x106,
        (
            "#057F#4PI'll go first.\x02\x03",

            "You take the end.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0x106, 400)
    Sleep(400)

    ChrTalk(    #147
        0x101,
        (
            "#1020FWhaaat...?!\x02\x03",

            "Wh-Why are you picking for me?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #148
        0x104,
        (
            "#031F#3PHe who strikes with all his might\x01",
            "first, wins, yes?\x02\x03",

            "In other words, he plans to settle\x01",
            "things before you come into play.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0x106,
        (
            "#053F#4PExactly.\x02\x03",

            "Eh, there ain't no deep meaning\x01",
            "in the order anyway. Basically,\x01",
            "we just gotta win.\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x10)

    ChrTalk(    #150
        0x101,
        (
            "#1007FW-Well, sure, but the pressure's\x01",
            "on if it ends up going to the third\x01",
            "round...\x02",
        )
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 270, 400)

    ChrTalk(    #151
        0xB,
        (
            "I've finished preparing for the match.\x01",
            "Is everyone ready to begin?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xB, 400)

    ChrTalk(    #152
        0x104,
        "#032F#3PPoker faces on, comrades!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0x101,
        "#1009F*gulp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #154
        0x106,
        "#552F#4PAll right, let's do this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0x105,
        "#040F#6PGood luck, Estelle.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x105, 400)

    ChrTalk(    #156
        0x101,
        "#1016FY-Yeah, thanks.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x101, 90, 400)

    ChrTalk(    #157
        0x101,
        (
            "#1002FC'mon, Estelle! A girl's gotta do\x01",
            "what a girl's gotta do.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3749")

    label("loc_3226")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_3749")

    ChrTalk(    #158
        0x101,
        (
            "#1019FUh, full disclosure, guys. I have, like,\x01",
            "zero confidence in my card skills.\x02\x03",

            "I always, ALWAYS lost to Joshua.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #159
        0x101,
        (
            "#1006FOh, but I bet you're pretty confident,\x01",
            "right, Schera?\x02\x03",

            "You use cards a lot in fortune\x01",
            "telling, so I can picture you knowing\x01",
            "a thing or two about gambling.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #160
        0x103,
        (
            "#020F#2PYes, I know a little.\x02\x03",

            "#026FI've also got an ace up my sleeve\x01",
            "for the worst case scenario, too.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #161
        0x101,
        "#1011FAn ace?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #162
        0x103,
        (
            "#525F#2PHeehee.\x01",
            "It's a secret unless we need it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #163
        0x104,
        (
            "#031F#1PThen I believe we'll have Schera take up the\x01",
            "final step. Should good fortune fail us, we'll\x01",
            "certainly be in need of that extra bit of 'luck.'\x02\x03",

            "#030FThat being said, I would prefer to take up the\x01",
            "middle.\x02\x03",

            "The second match will likely require\x01",
            "a great deal of strategy, and I have\x01",
            "some confidence in my card game.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #164
        0x101,
        (
            "#1015FSo you're second, Olivier, and Schera's\x01",
            "last...\x02\x03",

            "#1004F...which means I'm first?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #165
        0x103,
        (
            "#021F#2PYes, that should be relatively\x01",
            "easy on you.\x02\x03",

            "Enjoy the hand without any pressure.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)
    OP_A3(0x10)

    ChrTalk(    #166
        0x101,
        "#1007FSo you say, but I'm still feeling it.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)
    OP_8C(0xB, 270, 400)

    ChrTalk(    #167
        0xB,
        "Ladies, gentlemen, we are ready.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)
    OP_8C(0x101, 90, 400)

    ChrTalk(    #168
        0x101,
        "#1002FAll right, we're up.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #169
        0x104,
        "#030F#1PHeh. Poker faces on, comrades!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #170
        0x105,
        "#040FGood luck, you guys.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #171
        0x101,
        "#1005FLet's win this thing!\x02",
    )

    CloseMessageWindow()

    label("loc_3749")

    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_43(0x9, 0x3, 0x1, 0x2)
    WaitChrThread(0x9, 0x3)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3777")
    OP_43(0x9, 0x3, 0x1, 0x3)
    WaitChrThread(0x9, 0x3)

    label("loc_3777")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_378E")
    OP_43(0x9, 0x3, 0x1, 0x4)
    WaitChrThread(0x9, 0x3)

    label("loc_378E")

    Return()

    # Function_1_835 end

    def Function_2_378F(): pass

    label("Function_2_378F")

    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0x18, 255)
    TurnDirection(0x18, 0xD, 0)
    LoadEffect(0x0, "craft\\cr201_01.eff")
    Sleep(1000)
    OP_6D(27430, 0, 32610, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_37F9")
    SetChrPos(0xF7, 33000, 0, 31870, 135)
    SetChrPos(0x101, 28570, 0, 31000, 90)
    Jump("loc_381B")

    label("loc_37F9")

    SetChrPos(0x101, 33000, 0, 31870, 135)
    SetChrPos(0xF7, 28570, 0, 31000, 90)

    label("loc_381B")

    SetChrPos(0x105, 27670, 0, 31940, 90)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    FadeToBright(2000, 0)
    OP_0D()
    OP_6D(32073, 0, 31585, 2000)
    Sleep(1000)

    ChrTalk(    #172
        0xB,
        "This marks the first round of three.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #173
        0xB,
        (
            "Poker rules in this region are as\x01",
            "standard.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #174
        0xB,
        (
            "However, there is a hierarchy among\x01",
            "suits.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #175
        0xB,
        (
            "The strongest is spade, followed by\x01",
            "hearts, diamonds, and finally, clubs.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #176
        0xB,
        "I will now begin dealing your cards.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_4EE8")
    Call(2, 3)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #177
        0xD,
        (
            "#1PHahaha, my lucky streak strikes\x01",
            "again! My first round and I've already\x01",
            "got a great hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #178
        0xD,
        "#1PMan, I've got this in the bag.\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #179
        0x101,
        "#1002F(H-He must have a really good hand...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #180
        0x104,
        (
            "#035F(If that truly were the case, I can assure\x01",
            "you that he'd be much quieter about it.)\x02\x03",

            "#030F(Remember, you can't challenge an\x01",
            "opponent who chooses to fold.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #181
        0x101,
        "#1015F(Ah, good point.)\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0xC8, 0x140, 0x12C, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #182
        (
            "#050F(Time to start this thing off.)\x02\x03",

            "(Do I aim big, or should I aim low...?) \x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Keep King, Swap All Other Cards\x01",      # 0
            "Aim For A 4-8 Straight\x01",               # 1
        )
    )

    MenuEnd(0x3)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EBB")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #183
        (
            "#050F(One way or another, the odds\x01",
            "aren't all that great.)\x02\x03",

            "(This is just the start, though.\x01",
            "I should go for the safest bet I got.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_3F42")

    label("loc_3EBB")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #184
        (
            "#050F(One way or another, the odds\x01",
            "aren't all that great.)\x02\x03",

            "(I've gotta just aim big and hope\x01",
            "I come out on top.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_3F42")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)
    OP_C6(0x9, 0x6, 0, 0, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #185
        0xB,
        "Would you like to change cards?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_407E")

    ChrTalk(    #186
        0x106,
        "#050F#4PYeah, four cards.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #187
        0xB,
        "And you, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #188
        0xD,
        "#1PI'll change three.\x02",
    )

    CloseMessageWindow()
    Jump("loc_40D1")

    label("loc_407E")


    ChrTalk(    #189
        0x106,
        "#050F#4PYeah, two cards.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #190
        0xB,
        "And you, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #191
        0xD,
        "#1PI'll change three.\x02",
    )

    CloseMessageWindow()

    label("loc_40D1")

    OP_59()
    Call(2, 4)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #192
        0x105,
        (
            "#042F(Agate's face hasn't even twitched,\x01",
            "he's so still.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #193
        0x104,
        (
            "#031F#4P(Yes, yes, quite the poker face,\x01",
            "indeed.)\x02\x03",

            "(A virile man such as he simply\x01",
            "begs for my affections by furrowing\x01",
            "his brows so pointedly.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #194
        0xD,
        (
            "#1PHeh heh, yes, yes. Fell right into\x01",
            "my hand while I was waiting.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #195
        0xD,
        (
            "#1PCome, good challenger.\x01",
            "Come at me any time!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #196
        0x101,
        (
            "#1007F(H-He's certainly confident.)\x02\x03",

            "(But I wonder how much of that\x01",
            "is a bluff.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 5)
    OP_0D()
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #197
        0xB,
        "Would you like to challenge him?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45DC")
    OP_28(0x68, 0x1, 0x8)

    ChrTalk(    #198
        0x106,
        (
            "#053F#4P...\x02\x03",

            "#050FNah, I'll fold.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #199
        0xD,
        "#1PAwww, you're folding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #200
        0xD,
        (
            "#1PI had a good hand, too.\x01",
            "That's too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #201
        0xB,
        (
            "With that, I'm afraid your team\x01",
            "can no longer fold.\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #202
        0x101,
        "#1026FAw, we folded.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #203
        0x104,
        (
            "#033F#2PI suppose there's little else to\x01",
            "be done when you're dealt a poor\x01",
            "hand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_4477():

        label("loc_4477")

        TurnDirection(0x104, 0x106, 400)
        OP_48()
        Jump("loc_4477")

    QueueWorkItem2(0x104, 1, lambda_4477)
    OP_8E(0x106, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #204
        0x101,
        (
            "#1006FGood work, Agate.\x02\x03",

            "I gotta say, though, it's not like\x01",
            "you to fold.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #205
        0x106,
        (
            "#551F#2PDon't say it. Even I think that.\x02\x03",

            "#552FThis is where things get tough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #206
        0x105,
        (
            "#042F#3PRight. Not being able to fold means\x01",
            "we no longer have a safety net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #207
        0x101,
        (
            "#1015FOh, yeah. You've got a point.\x02\x03",

            "This'll be harder than I thought.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4DB3")

    label("loc_45DC")

    OP_28(0x68, 0x1, 0x4)

    ChrTalk(    #208
        0x106,
        (
            "#053F#4PYeah, of course.\x02\x03",

            "I'll challenge here.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #209
        0xD,
        "#1PWh...?!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #210
        0xD,
        (
            "#1PA-Are you sure? I've got a really,\x01",
            "REALLY great hand, so...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #211
        0x106,
        (
            "#050F#4PYou sure yap a lot, you bastard.\x02\x03",

            "I said I'll challenge you. Shut up\x01",
            "and decide if you'll take it or not.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(400)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #212
        0xB,
        "What will you do, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #213
        0xD,
        "#1PWhat to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #214
        0xD,
        (
            "#1PI bet I could win with this hand,\x01",
            "so I'll--\x02",
        )
    )

    CloseMessageWindow()
    PlayEffect(0x0, 0x0, 0x106, 0, 200, 0, 0, 0, 0, 900, 900, 900, 0xFF, 0, 0, 0, 0)
    Sleep(400)
    OP_22(0x297, 0x0, 0x64)

    ChrTalk(    #215
        0x106,
        "#057F#4P...\x02",
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #216
        0xD,
        "#1PWhaaat?!\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00150")
    FadeToDark(300, 0, 100)
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)

    def lambda_4859():

        label("loc_4859")

        TurnDirection(0xB, 0xD, 400)
        OP_48()
        Jump("loc_4859")

    QueueWorkItem2(0xB, 1, lambda_4859)

    def lambda_486A():

        label("loc_486A")

        TurnDirection(0x18, 0xD, 400)
        OP_48()
        Jump("loc_486A")

    QueueWorkItem2(0x18, 1, lambda_486A)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_488D():
        OP_8F(0xD, 0x7E88, 0x0, 0x6E3E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_488D)

    def lambda_48A8():
        OP_9E(0xFE, 0x1E, 0x0, 0x3E8, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_48A8)

    ChrTalk(    #217
        0xD,
        "#5PEeeeeeeeep...!!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #218
        0xD,
        "#5PI-I fold! I fold!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #219
        0xD,
        (
            "#5PI'll fold, just please, don't do\x01",
            "anything to me!\x02",
        )
    )

    CloseMessageWindow()
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_44(0xB, 0x1)
    OP_44(0x18, 0x1)
    TurnDirection(0x106, 0xB, 400)
    Sleep(500)

    ChrTalk(    #220
        0x106,
        "#050F#4PHey, he said he's foldin'.\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xB, 0x106, 400)

    ChrTalk(    #221
        0xB,
        "Pardon?! Ahem! Ah, yes, so he did.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #222
        0xB,
        (
            "With that, sir, I'm afraid you can no\x01",
            "longer fold starting with the next round.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xD, 0x2, 0x1, 0x17)

    ChrTalk(    #223
        0xD,
        "*pant* *pant*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #224
        0xD,
        "Th-That was so sc-scary.\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)

    ChrTalk(    #225
        0x101,
        (
            "#1018FWoo! Phelio folded!\x02\x03",

            "#1016FWell, it might be more accurate to\x01",
            "say he got folded.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #226
        0x105,
        "#041F#3PHeehee... How very like Agate.\x02",
    )

    CloseMessageWindow()

    def lambda_4B01():

        label("loc_4B01")

        TurnDirection(0x104, 0x106, 400)
        OP_48()
        Jump("loc_4B01")

    QueueWorkItem2(0x104, 1, lambda_4B01)

    def lambda_4B12():

        label("loc_4B12")

        TurnDirection(0xD, 0x106, 400)
        OP_48()
        Jump("loc_4B12")

    QueueWorkItem2(0xD, 1, lambda_4B12)
    OP_8E(0x106, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)
    OP_44(0xD, 0x1)

    ChrTalk(    #227
        0x101,
        (
            "#1001FNice work, Agate.\x02\x03",

            "Now I know why you said you'd\x01",
            "challenge him with willpower.\x02\x03",

            "Not only did you actually do it, you\x01",
            "pulled through and won! Gotta admit,\x01",
            "I'm impressed. And kinda stunned.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #228
        0x104,
        (
            "#031F#2PYes, your recovery was remarkable.\x01",
            "Your position was looking very dangerous\x01",
            "for a moment there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #229
        0x106,
        (
            "#051F#2PYeah, I managed to work it out.\x02\x03",

            "#050FStill, we haven't won yet. Make sure\x01",
            "you guys're ready for the rest.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #230
        0x105,
        (
            "#042F#3PThat's true.\x02\x03",

            "We won the first match,\x01",
            "but it only takes one win from\x01",
            "him for us to lose the bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #231
        0x104,
        (
            "#030F#2PI may need the courage to\x01",
            "stand down if the situation call\x01",
            "for it, in other words.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_4DB3")

    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #232
        0xB,
        (
            "Sirs, are you prepared for the\x01",
            "next match?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #233
        0x104,
        (
            "#033F#4PAh, that's my cue.\x02\x03",

            "#035FMay Lady Luck favor me with her grace.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #234
        0x106,
        "#050F#6PCountin' on you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #235
        0x101,
        (
            "#1009F#3PAfter all the talking you did, I am SO\x01",
            "not gonna go easy on you if you lose.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    Jump("loc_69CD")

    label("loc_4EE8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_69CD")
    Call(2, 6)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #236
        0xD,
        (
            "#1PHahaha, my lucky streak strikes\x01",
            "again! My first round and I've already\x01",
            "got a great hand!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #237
        0xD,
        "#1PMan, I've got this in the bag.\x02",
    )

    CloseMessageWindow()
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #238
        0x105,
        "#040F(He must have an impressive hand.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #239
        0x104,
        (
            "#035F(If that truly were the case, I can assure\x01",
            "you that he'd be much quieter about it.)\x02\x03",

            "#030F(Remember, you can't challenge an\x01",
            "opponent who chooses to fold.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #240
        0x103,
        "#020F(Here's hoping our girl recognizes that.)\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x0, 0xA0, 0x64, 0x140, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x12C, 0xA0, 0x190, 0x140, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #241
        (
            "#1000F(Okay, I need to think real hard\x01",
            "about this.)\x02\x03",

            "(Should I swap out for a shot at\x01",
            "a big hand, or keep an easy one?)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Swap Leaving One Pair\x01",      # 0
            "Aim For Heart Flush\x01",        # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5438")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #242
        (
            "#1015F(It's still the first match, so the\x01",
            "theory's to go for the sure thing.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_54D3")

    label("loc_5438")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #243
        (
            "#1015F(It's still the first match, so they\x01",
            "say you should go for the sure thing,\x01",
            "right?)\x02\x03",

            "#1002F(Aww, whatever! I'm gonna aim big!)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_54D3")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)
    OP_C6(0x9, 0x6, 0, 0, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #244
        0xB,
        "Would you like to change cards?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5608")

    ChrTalk(    #245
        0x101,
        "#1000F#4PYeah, three cards.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #246
        0xB,
        "Sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #247
        0xD,
        "#1PI'll change three.\x02",
    )

    CloseMessageWindow()
    Jump("loc_5658")

    label("loc_5608")


    ChrTalk(    #248
        0x101,
        "#1000F#4PYeah, two cards.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #249
        0xB,
        "Sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #250
        0xD,
        "#1PI'll change three.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)

    label("loc_5658")

    OP_59()
    Call(2, 7)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5787")

    ChrTalk(    #251
        0x105,
        "#040F(You're so obvious, Estelle...)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #252
        0x104,
        (
            "#030F(I doubt he could read her the\x01",
            "way we can, but one can never\x01",
            "be too careful.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #253
        0x103,
        (
            "#025F(If things go sour, I'm sure it'll\x01",
            "be plain as day.)\x02\x03",

            "(I'd heard she was bad at this.\x01",
            "Understatement of the century.)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_5951")

    label("loc_5787")

    OP_59()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #254
        0x105,
        (
            "#045F(E-Estelle, anyone could see what\x01",
            "you're thinking right about now...)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #255
        0x104,
        (
            "#031F(She wears her heart so plainly\x01",
            "that I can almost see her hand as\x01",
            "if it were my own.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #256
        0x103,
        (
            "#025F(*sigh* I'd heard she was bad at\x01",
            "this, but I think even that's generous.\x01",
            "'Abysmal' is more like it.)\x02\x03",

            "(I can't imagine Joshua ever lost\x01",
            "a single hand to her unless he did it\x01",
            "on purpose.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_5951")

    OP_62(0xD, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #257
        0xD,
        (
            "#1PHeh heh, yes, yes. Fell right into\x01",
            "my hand while I was waiting.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x106, 400)

    ChrTalk(    #258
        0xD,
        (
            "#1PCome, good challenger.\x01",
            "Come at me any time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #259
        0x105,
        (
            "#045F(Phelio's behavior is no surprise.)\x02\x03",

            "(I wonder how confident he really is.)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 8)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #260
        0xB,
        "Would you like to challenge?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5F58")
    OP_28(0x68, 0x1, 0x40)

    ChrTalk(    #261
        0x101,
        "#1007F#4PNo, I'll fold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #262
        0xD,
        "#1PAw, you're folding?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #263
        0xD,
        (
            "#1PI had a good hand, too.\x01",
            "Too bad.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #264
        0xB,
        (
            "With that, I'm afraid your team\x01",
            "can no longer fold.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #265
        0x103,
        "#023FFolded in the end, did you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #266
        0x104,
        (
            "#030FEven we could see your lack of\x01",
            "confidence in your hand.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_5BC7():

        label("loc_5BC7")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_5BC7")

    QueueWorkItem2(0x104, 1, lambda_5BC7)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #267
        0x103,
        (
            "#021FStill, you knew when to bow\x01",
            "out gracefully. Folding was\x01",
            "surprisingly mature of you.\x02\x03",

            "I was sure you'd be stubborn\x01",
            "and challenge no matter what.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #268
        0x101,
        (
            "#1003F#2PWell, I WANTED to challenge it,\x01",
            "but...my hand wasn't great.\x02\x03",

            "#1007FBesides, it wouldn't have done us\x01",
            "much good if I'd just powered through\x01",
            "on willpower alone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #269
        0x103,
        (
            "#027FThat's a good way to think of it.\x02\x03",

            "#026FStill, now we're in a corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #270
        0x105,
        (
            "#042F#3PRight. Not being able to fold means\x01",
            "we no longer have a safety net.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #271
        0x101,
        (
            "#1015F#2POh, yeah. You've got a point.\x02\x03",

            "This'll be harder than I thought.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #272
        0xB,
        (
            "Sirs, are you prepared for the\x01",
            "next match?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #273
        0x104,
        (
            "#033F#4PAh, that's my cue.\x02\x03",

            "#035FMay Lady Luck favor me with her grace.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #274
        0x103,
        "#020F#3PWe're counting on you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #275
        0x101,
        (
            "#1009F#4PAfter all the talking you did, I am SO\x01",
            "not gonna go easy on you if you lose.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_69CD")

    label("loc_5F58")


    ChrTalk(    #276
        0x101,
        "#1005F#4POF COURSE I am! Duh!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_64DC")
    OP_28(0x68, 0x1, 0x10)
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #277
        0xD,
        "#1PWh...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #278
        0xD,
        (
            "#1PA-Are you sure? I've got a really,\x01",
            "REALLY great hand, so..\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #279
        0x101,
        (
            "#1012F#4PYeah, whatever. I don't really care.\x02\x03",

            "#1028FIf it's that good, why don't you\x01",
            "hurry up and bring it on?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #280
        0xB,
        "What will you do, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #281
        0xD,
        "#1PWhat to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #282
        0xD,
        (
            "#1PI could win with this hand if\x01",
            "I challenge, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #283
        0xD,
        "#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #284
        0xD,
        "#1PNo, I'll fold.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #285
        0xB,
        (
            "With that, sir, I'm afraid you can no\x01",
            "longer fold starting with the next round.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #286
        0x101,
        "#1018F#4PAll right, I did it!\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    def lambda_61D4():

        label("loc_61D4")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_61D4")

    QueueWorkItem2(0x104, 1, lambda_61D4)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #287
        0x103,
        "#021FGood work out there.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #288
        0x105,
        (
            "#040F#3PYou took a strong stance and\x01",
            "it paid off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #289
        0x101,
        "#1001F#2PYeah, I'm just glad I didn't lose.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #290
        0x104,
        (
            "#031F#2PWhat you did was more than\x01",
            "winning.\x02\x03",

            "Our opponent is now cornered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #291
        0x101,
        (
            "#1015F#2POh, I almost forgot. You can only\x01",
            "fold once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #292
        0x105,
        (
            "#042F#3PExactly. We won the first match,\x01",
            "but it only takes one win from him\x01",
            "for us to lose the bet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #293
        0x103,
        (
            "#022FAgreed. We'll have to proceed\x01",
            "carefully.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #294
        0xB,
        (
            "Sirs, are you prepared for the next\x01",
            "match?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x104, 90, 400)

    ChrTalk(    #295
        0x104,
        (
            "#033F#4PAh, that's my cue.\x02\x03",

            "#035FMay Lady Luck favor me with her grace.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #296
        0x103,
        "#020F#3PWe're counting on you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    ChrTalk(    #297
        0x101,
        (
            "#1009F#4PAfter all the talking you did, I am SO\x01",
            "not gonna go easy on you if you lose.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Jump("loc_69CD")

    label("loc_64DC")

    OP_28(0x68, 0x1, 0x20)
    TurnDirection(0xD, 0x101, 400)
    Sleep(500)

    ChrTalk(    #298
        0xD,
        "#1PAre you sure?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #299
        0xD,
        (
            "#1PYou don't look all that happy.\x01",
            "Did you really get something...?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #300
        0x101,
        "#1019F#4PUh...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #301
        0x101,
        "#1022F#4PS-Stop yapping and bring it on!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #302
        0xB,
        "What will you do, sir?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #303
        0xD,
        "#1PWhat to do...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #304
        0xD,
        (
            "#1PI could win with this hand if\x01",
            "I challenge...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #305
        0xD,
        "#1P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #306
        0xD,
        "#1PAll right, I'll challenge.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #307
        0x101,
        "#1020F#4P(Crap! He took me up on it.)\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)

    ChrTalk(    #308
        0xB,
        "If you would please show your cards.\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    TurnDirection(0x101, 0xB, 400)
    Sleep(1000)
    OP_63(0xFFFF)
    Call(2, 22)
    OP_59()

    ChrTalk(    #309
        0xB,
        "Sir, you are the victor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #310
        0xB,
        (
            "As agreed upon in advance,\x01",
            "this ends your match.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #311
        0x101,
        "#1008F#4PAwwww...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x103, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(2000)

    ChrTalk(    #312
        0x105,
        "#045F#3PW-We lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #313
        0x103,
        "#026FWell, that was quick.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #314
        0x104,
        (
            "#031F#2PHahaha. My, my, Estelle.\x02\x03",

            "Even the way you lose is\x01",
            "astoundingly spirited.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_6899():
        OP_6D(29690, 0, 31480, 1000)
        ExitThread()

    QueueWorkItem(0x19, 1, lambda_6899)
    SetChrFlags(0x101, 0x40)
    OP_8E(0x101, 0x7E68, 0x0, 0x7B70, 0xBB8, 0x0)
    OP_8E(0x101, 0x7E86, 0x0, 0x779C, 0xBB8, 0x0)
    ClearChrFlags(0x101, 0x40)

    def lambda_68E3():
        TurnDirection(0xFE, 0x101, 400)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_68E3)
    OP_43(0xD, 0x2, 0x1, 0x15)

    ChrTalk(    #315
        0xD,
        "#1PWh-Whaaaaaaat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #316
        0x101,
        (
            "#1016F#2PHey, hey! Once more, please!\x02\x03",

            "I'm begging you, one more go!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #317
        0x103,
        (
            "#025F*sigh* You idiot...\x02\x03",

            "This is embarrassing. Catch her\x01",
            "and then we can get out of here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_44(0xD, 0x2)
    Sleep(1000)
    Call(1, 18)
    Return()

    label("loc_69CD")

    FadeToDark(2000, 0, -1)
    OP_0D()
    Return()

    # Function_2_378F end

    def Function_3_69D9(): pass

    label("Function_3_69D9")

    OP_4A(0xB, 255)
    OP_4A(0xD, 255)
    OP_4A(0x18, 255)
    TurnDirection(0x18, 0xD, 0)
    Sleep(1000)
    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x104, 33000, 0, 31870, 135)
    SetChrPos(0x101, 28570, 0, 31000, 90)
    SetChrPos(0xF7, 28850, 0, 32500, 90)
    SetChrPos(0x105, 27670, 0, 31940, 90)
    SetChrPos(0xD, 32530, 0, 29680, 79)
    FadeToBright(2000, 0)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #318
        0xB,
        "I will now begin dealing your cards.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    Call(2, 9)
    Sleep(400)
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)

    ChrTalk(    #319
        0xD,
        "#1P...Here?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #320
        0xD,
        "#1PNo... It might come here.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #321
        0xD,
        "#1PHm...\x02",
    )

    CloseMessageWindow()
    OP_63(0xD)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #322
        0x101,
        "#1002F(H-He seems kinda hesitant.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #323
        0x105,
        "#042F(Yes, his expression is different.)\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_6B91")

    ChrTalk(    #324
        0x106,
        "#052F(He might have a good hand.)\x02",
    )

    CloseMessageWindow()
    Jump("loc_6BDB")

    label("loc_6B91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_6BDB")

    ChrTalk(    #325
        0x103,
        (
            "#022F(We should probably assume he's\x01",
            "got a pretty good hand.)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_6BDB")

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0xC8, 0x0, 0x12C, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0xC8, 0x140, 0x12C, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #326
        (
            "#030F(Now, what to do?)\x02\x03",

            "(Should I reach my hand out or\x01",
            "distract my foe?)\x02\x03",

            "(Heh, either or would make for\x01",
            "a worthy spectacle.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Exchange All Cards Leaving The Pair\x01",      # 0
            "Exchange One Card Leaving The Pair\x01",       # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6F6E")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #327
        (
            "#030F(Hmm...\x01",
            "I should play it straight here.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_6FB5")

    label("loc_6F6E")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #328
        (
            "#030F(Hmm...\x01",
            "Let's play the game of deception.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_6FB5")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)
    OP_C6(0x9, 0x6, 0, 0, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #329
        0xB,
        "Will you be changing cards?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_70F6")

    ChrTalk(    #330
        0x104,
        "#030F#4PI will! Three cards, please.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #331
        0xB,
        "You, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #332
        0xD,
        "#1PI'll take two cards.\x02",
    )

    CloseMessageWindow()
    Jump("loc_714D")

    label("loc_70F6")


    ChrTalk(    #333
        0x104,
        "#030F#4POne card only, please.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #334
        0xB,
        "You, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #335
        0xD,
        "#1PI'll take two cards.\x02",
    )

    CloseMessageWindow()

    label("loc_714D")

    OP_59()
    Call(2, 10)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #336
        0x101,
        (
            "#1002F(Man, I can't read his face at all.)\x02\x03",

            "(What the heck are you thinking,\x01",
            "Olivier?)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #337
        0x105,
        (
            "#040F(He has a surprisingly strong\x01",
            "poker face, doesn't he?)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1000)
    OP_63(0xD)

    ChrTalk(    #338
        0xD,
        "#1PAll right...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #339
        0xD,
        "#1PYeah, I'm okay.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_72B4")

    ChrTalk(    #340
        0x106,
        (
            "#555F(He seems awfully subdued compared\x01",
            "to before.)\x02\x03",

            "(Did he get some kinda big hand?)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7318")

    label("loc_72B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7318")

    ChrTalk(    #341
        0x103,
        (
            "#022F(That's a very restrained reaction\x01",
            "compared to before.)\x02\x03",

            "(Did he make a big hand?)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_7318")

    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(2, 20)
    OP_0D()
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #342
        0xB,
        "Will you challenge?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_7F51")
    OP_28(0x68, 0x1, 0x100)

    ChrTalk(    #343
        0x104,
        (
            "#031F#4PNo, I'll fold.\x02\x03",

            "It takes cunning to know when 'retreat'\x01",
            "becomes the more respectable strategy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #344
        0xD,
        "#1PTch, folded, did you?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0xD, 400)

    ChrTalk(    #345
        0x104,
        (
            "#033F#4POh? You seem quite disappointed.\x02\x03",

            "#031FIf I wasted a good hand of yours,\x01",
            "then may you have my most heartfelt\x01",
            "apologies.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0xD, 0x104, 400)
    Sleep(400)

    ChrTalk(    #346
        0xD,
        "#1PN-No, it's nothing like that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #347
        0xD,
        "#1PI didn't have much of a hand either.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #348
        0xB,
        (
            "As of the next round, neither\x01",
            "side will be able to fold.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(28820, 0, 31840, 0)
    OP_8C(0xD, 90, 0)
    OP_8C(0xB, 270, 0)
    OP_0D()

    ChrTalk(    #349
        0x101,
        (
            "#1004FWould you look at that!\x01",
            "He folded.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_75CF")

    ChrTalk(    #350
        0x106,
        (
            "#050F#4PProbably figured out his opponent\x01",
            "had the better hand.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_761C")

    label("loc_75CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_761C")

    ChrTalk(    #351
        0x103,
        (
            "#020F#4PHe probably figured out the odds\x01",
            "were in Phelio's favor.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_761C")


    def lambda_7622():

        label("loc_7622")

        TurnDirection(0xF7, 0x104, 400)
        OP_48()
        Jump("loc_7622")

    QueueWorkItem2(0xF7, 1, lambda_7622)
    OP_8E(0x104, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0xF7, 0x1)

    ChrTalk(    #352
        0x104,
        (
            "#031F#4PI have returned, my loves. ♪\x02\x03",

            "Did you see? My calm\x01",
            "and expert assessment of the situation\x01",
            "was flawless.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #353
        0x101,
        (
            "#1015FBut did Phelio really have a good hand?\x02\x03",

            "If you'd challenged, you might have won.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #354
        0x104,
        (
            "#035F#4PI'd say it is almost a certainty that he\x01",
            "had a much stronger hand than mine.\x02\x03",

            "Methinks if I had challenged, I'd be\x01",
            "swimming in a sea of tears by now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #355
        0x101,
        (
            "#1016FDon't you think that's a wee\x01",
            "bit dramatic...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #356
        0x105,
        (
            "#040F#3PNow that both sides have folded,\x01",
            "neither of us can back down from\x01",
            "the final round.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_7D3E")

    ChrTalk(    #357
        0x106,
        (
            "#050F#4PYeah, exactly.\x02\x03",

            "So we're gonna settle this nice\x01",
            "and clean in the next match.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #358
        0x101,
        (
            "#1002FYeah, we'll... Wait.\x02\x03",

            "#1004FNext match is my match,\x01",
            "isn't it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #359
        0x106,
        "#555F#4PKinda late for you to act clueless now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #360
        0x104,
        (
            "#030F#4POur fate is in your hands, Estelle.\x02\x03",

            "I shall pray for your victory with\x01",
            "all my strength.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #361
        0x101,
        (
            "#1016FP-Pray, huh...?\x02\x03",

            "#1015FThat doesn't necessarily mean\x01",
            "the hand of my dreams will come.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #362
        0x104,
        "#031F#4POh, but what if does?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #363
        0x101,
        (
            "#1019FWh-What? What's going on in your\x01",
            "twisted mind now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #364
        0x104,
        (
            "#032F#4PEstelle, if I could provide a word\x01",
            "of advice, hmm?\x02\x03",

            "If you're ever uncertain of which\x01",
            "cards to choose, you may be better\x01",
            "off simply tossing them to the wind.\x02\x03",

            "#031FThe thought reminds me of a popular\x01",
            "saying which illustrates my point\x01",
            "beautifully:\x02\x03",

            "'It's easier to re-bake a cake\x01",
            "than to re-coat the frosting.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #365
        0x101,
        (
            "#1007FPopular, my ass. You just made it up.\x02\x03",

            "#1002FStill, why tell me any of this?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #366
        0x104,
        (
            "#031F#4PMmm, just a hunch. Keep it at the\x01",
            "back of your mind during your match,\x01",
            "won't you?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #367
        0xB,
        "Are you ready for your final match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #368
        0x106,
        "#050F#4PHey, it's about that time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #369
        0x104,
        (
            "#031F#4PHeh. I pray Aidios grants you victory,\x01",
            "Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #370
        0x101,
        (
            "#1015FS-Sure, thanks.\x01",
            "(Something's bothering me...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_7F2B")

    label("loc_7D3E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_7F2B")

    ChrTalk(    #371
        0x103,
        (
            "#026F#4PYes, exactly.\x02\x03",

            "We'll be settling this cleanly in the\x01",
            "next match.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #372
        0x101,
        (
            "#1011FNext is Schera's turn, huh?\x02\x03",

            "#1001FCool! ♪ I've got a hunch that\x01",
            "things'll work out just fine.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #373
        0x103,
        (
            "#027FHopefully. \x02\x03",

            "Well, we'll see if Aidios is in a\x01",
            "generous mood.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 0)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #374
        0xB,
        "Are you ready for your final match?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #375
        0x104,
        "#030F#4PThe curtain rises.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x103, 400)

    ChrTalk(    #376
        0x104,
        (
            "#030F#4PWell, then, Schera.\x01",
            "Let's see what you can do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #377
        0x103,
        "#021FHaha, I'll try not to disappoint.\x02",
    )

    CloseMessageWindow()

    label("loc_7F2B")

    FadeToDark(2000, 0, -1)
    OP_0D()
    SetChrPos(0xD, 32398, 0, 30463, 90)
    OP_8C(0xB, 270, 0)
    Jump("loc_874E")

    label("loc_7F51")


    ChrTalk(    #378
        0x104,
        (
            "#031F#4PHeh, but of course.\x02\x03",

            "The word 'retreat' does not exist in\x01",
            "my dictionary.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #379
        0xB,
        "What will you do, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #380
        0xD,
        "#1PYeah, I'll take the challenge.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x104, 400)

    ChrTalk(    #381
        0xB,
        "If you would please show your cards.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 21)
    OP_59()

    ChrTalk(    #382
        0xB,
        "Sir, you are the victor.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #383
        0xB,
        (
            "As agreed to in advance,\x01",
            "this settles the match.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #384
        0x104,
        (
            "#035F#4PWell, victory is in the luck of the draw,\x01",
            "which means there must be a loser as\x01",
            "well. And this time, the loser is I.\x02\x03",

            "#031FHm? I know this piercing sensation...\x02\x03",

            "I feel a menacing presence at my back...\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #385
        0x101,
        (
            "#1009F#1PTh-That stupid bard...\x02\x03",

            "Olivierrrrrrr, you KNEW, didn't you?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #386
        0x105,
        "#045F#6PE-Estelle, try and hold it in.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xF7, 0x101, 400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_83AC")

    ChrTalk(    #387
        0x106,
        (
            "#053F#2PLike you're in any position to talk.\x02\x03",

            "Who was the one who was\x01",
            "whining before we even started?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #388
        0x101,
        "#1019F#1PMmmmm...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #389
        0x106,
        (
            "#057F#2PWe didn't lose because of him.\x02\x03",

            "If you got time to pummel the guy,\x01",
            "spend some of it thinkin' up a decent\x01",
            "excuse for our client.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xF7, 400)

    ChrTalk(    #390
        0x101,
        (
            "#1007F#1POh yeah... Crap. We failed our job.\x02\x03",

            "*sigh* How can I look the client in\x01",
            "the eye now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8733")

    label("loc_83AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_8733")
    TurnDirection(0x103, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x68, 0x1, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_8583")

    ChrTalk(    #391
        0x103,
        (
            "#027F#2PAre you really in a position to say\x01",
            "that?\x02\x03",

            "You folded in the first round yourself.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #392
        0x101,
        "#1019F#1PUgh... True.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #393
        0x103,
        (
            "#025F#2PWe folded there, so what else\x01",
            "could we do but challenge here?\x02\x03",

            "Half the fault lies with you,\x01",
            "so don't go trying to pass off blame.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #394
        0x101,
        (
            "#1007F#1PI get it. I get it, okay?\x02\x03",

            "*sigh* Still, how do we apologize to\x01",
            "our client?\x02\x03",

            "#1014FMan, why didn't I challenge him...?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8733")

    label("loc_8583")


    ChrTalk(    #395
        0x103,
        (
            "#027F#2PAre you really in a position to say\x01",
            "that?\x02\x03",

            "Who was the one who talked\x01",
            "about how bad they were at cards\x01",
            "before we even started?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #396
        0x101,
        "#1019F#1PUh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #397
        0x103,
        (
            "#026F#2PWe didn't lose because of Olivier.\x02\x03",

            "If you have time to complain,\x01",
            "spend some of it thinking about\x01",
            "an excuse for our client.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #398
        0x101,
        (
            "#1007F#1POh yeah... Crap. We failed our job.\x02\x03",

            "*sigh* How can I look the client in\x01",
            "the eye now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8733")

    OP_28(0x68, 0x1, 0x80)
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    Call(1, 18)
    Return()

    label("loc_874E")

    OP_6D(32073, 0, 31585, 0)
    SetChrPos(0x105, 27670, 0, 31940, 90)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_87AD")
    SetChrPos(0x101, 33000, 0, 31870, 135)
    SetChrPos(0xF7, 28570, 0, 31000, 90)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    Jump("loc_87E7")

    label("loc_87AD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_87E7")
    SetChrPos(0xF7, 33000, 0, 31870, 135)
    SetChrPos(0x104, 28850, 0, 32500, 90)
    SetChrPos(0x101, 28570, 0, 31000, 90)

    label("loc_87E7")

    SetChrPos(0xD, 32530, 0, 29680, 79)
    FadeToBright(2000, 0)
    OP_0D()
    Return()

    # Function_3_69D9 end

    def Function_4_8803(): pass

    label("Function_4_8803")

    Sleep(1000)

    ChrTalk(    #399
        0xB,
        "You are both prepared, I hope.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #400
        0xB,
        "We will now begin the final match.\x02",
    )

    CloseMessageWindow()
    Sleep(1000)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_A79E")
    Call(2, 11)
    OP_59()
    Sleep(400)
    TurnDirection(0x101, 0xD, 400)

    ChrTalk(    #401
        0x101,
        "#1002F#4P(How's Phelio acting this time?)\x02",
    )

    CloseMessageWindow()
    Call(1, 24)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #402
        0x105,
        "#045F(He's changed his tune.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #403
        0x106,
        (
            "#050F(Yeah, looks like he's got\x01",
            "somethin' worthwhile.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #404
        0x104,
        (
            "#030F(Now, how will you proceed in turn,\x01",
            "Estelle?)\x02\x03",

            "(I hope my advice fell on willing ears...)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x190, 0x0, 0x1F4, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x0, 0xA0, 0x64, 0x140, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0xC8, 0x0, 0x12C, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    TurnDirection(0x101, 0xB, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #405
        (
            "#1002F(This is bad. Phelio looks like\x01",
            "he's at the top of his game.)\x02\x03",

            "(Even if I complete the flush,\x01",
            "he might come out with an even\x01",
            "better hand.)\x02\x03",

            "#1015F(With the hand I've got, though,\x01",
            "there's not much more I can aim\x01",
            "for outside of that flush.)\x02\x03",

            "#1022F(Aaah, something in my gut's telling\x01",
            "me to just go with what Olivier said.\x01",
            "Throw all my cards out and start fresh.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x4, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Aim For A Diamond Flush\x01",      # 0
            "Exchange All Cards\x01",           # 1
        )
    )

    MenuEnd(0x4)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EAA")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #406
        (
            "#1007F(Yeah, but my gut could be wrong.\x01",
            "Aiming for a flush is obviously the\x01",
            "way to go.)\x02\x03",

            "(I can't really wish for something\x01",
            "I don't have.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_8F57")

    label("loc_8EAA")

    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Estelle")

    AnonymousTalk(    #407
        (
            "#1002F(Even if I finish the flush, if he's got\x01",
            "something better, there's no point.)\x02\x03",

            "#1007F(Mmmmm, never thought I'd say this,\x01",
            "but you win, Olivier.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_8F57")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)
    OP_C6(0x9, 0x6, 0, 0, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #408
        0xB,
        "Will you be changing your cards?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x4), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_97E1")

    ChrTalk(    #409
        0x101,
        "#1002F#4PYeah, two.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #410
        0xB,
        "And you, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #411
        0xD,
        "#1PI-I'll take just one.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 12)
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x105, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(400)

    ChrTalk(    #412
        0x105,
        (
            "#040F(Estelle's acting like she has\x01",
            "a pretty good hand, too.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #413
        0x104,
        (
            "#030F#4P(With the expression she wears now,\x01",
            "I would have to agree.)\x02\x03",

            "#034F(Still, if even your beloved audience can\x01",
            "see what you're thinking, Estelle... Hmm...\x01",
            "How do put this delicately...?)\x02\x03",

            "(Estelle's expressions are almost like\x01",
            "a semaphore.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #414
        0x106,
        (
            "#551F(She wasn't kiddin' when she said\x01",
            "she was bad at cards.)\x02",
        )
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    Call(1, 17)
    OP_59()
    Call(2, 19)
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #415
        0x101,
        (
            "#1020F#4PIs that a r-royal something or...?!\x02\x03",

            "Isn't that the strongest hand?!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #416
        0x106,
        (
            "#055FWhoa, whoa!\x01",
            "THAT hand, of all things.\x02\x03",

            "The odds of that are next to nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #417
        0x105,
        "#042FIt'll be hard to win against that hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #418
        0x104,
        (
            "#031FHahaha. Well, not much for that\x01",
            "except to put up your hands.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #419
        0xB,
        (
            "Please show your hand as well,\x01",
            "miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #420
        0xB,
        (
            "The conclusion of a match is never\x01",
            "known until the last card is on the\x01",
            "table.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #421
        0x101,
        (
            "#1016F#4PWell, I'm pretty sure we know this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 16)
    OP_59()

    ChrTalk(    #422
        0xB,
        "Hmm... It certainly is decisive...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #423
        0xB,
        "This match...is Phelio's victory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #424
        0xD,
        "#1PHahaha. Naturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #425
        0xD,
        (
            "#1PYou fought well, but you can't\x01",
            "win against a master of gambling.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #426
        0x105,
        "#043F#6P*sigh* We lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #427
        0x104,
        (
            "#030F#2PSo close.\x01",
            "If only we'd had a little push...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #428
        0x106,
        (
            "#053F#1PNot much you could even do against\x01",
            "the hand he got.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9617():

        label("loc_9617")

        TurnDirection(0x104, 0x101, 400)
        OP_48()
        Jump("loc_9617")

    QueueWorkItem2(0x104, 1, lambda_9617)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #429
        0x101,
        "#1007F#2PSorry, guys. I lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #430
        0x106,
        (
            "#050F#1PYou don't need to apologize to us.\x01",
            "Losin' was a group effort.\x02\x03",

            "If you want to apologize, you should\x01",
            "apologize to the client.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #431
        0x101,
        (
            "#1003F#2PCrap... We failed our job, didn't we?\x02\x03",

            "#1007F*sigh* How can I look the client in\x01",
            "the eye now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #432
        0x106,
        (
            "#552F#1PYeah, I feel you, but we've still\x01",
            "gotta go see her.\x02\x03",

            "It's one of the hard parts of being\x01",
            "a bracer.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x68, 0x1, 0x200)
    Call(1, 18)
    Return()

    label("loc_97E1")


    ChrTalk(    #433
        0x101,
        (
            "#1002F#4PYeah...\x02\x03",

            "#1007FAll five cards.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #434
        0xB,
        "...\x02",
    )

    CloseMessageWindow()

    def lambda_981D():

        label("loc_981D")

        TurnDirection(0x101, 0x104, 400)
        OP_48()
        Jump("loc_981D")

    QueueWorkItem2(0x101, 1, lambda_981D)

    ChrTalk(    #435
        0x101,
        "#1009F#4P(Okay. No turning back, Olivier.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #436
        0x104,
        "#031F(Well played, Estelle.)\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0xE)
    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #437
        0xB,
        "And you, sir?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #438
        0xD,
        "#1PI-I'll just swap one.\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x104, 0x1)

    ChrTalk(    #439
        0x101,
        "#1002F#4P(Wh-What is he doing?)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #440
        0x104,
        "#035F#2P(Heh...)\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00130")
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)
    Sleep(400)
    OP_62(0x104, 0x0, 2000, 0xA, 0xB, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #441
        0x104,
        "#035F#2PFuuuuuu～...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #442
        "\x07\x05Olivier blew in the dealer's ear.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_0D()
    OP_9E(0xB, 0xF, 0x0, 0x12C, 0x1388)
    OP_62(0xB, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_43(0xB, 0x1, 0x1, 0x10)

    ChrTalk(    #443
        0xB,
        "#1PAaaaaaah?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0xB, 0x1)

    ChrTalk(    #444
        0xB,
        "Wh-What on earth are you doing?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #445
        0x104,
        (
            "#031FHahaha, my apologies. I simply couldn't\x01",
            "endure the anxiety of the moment.\x01",
            "The tension 'escaped' me, so to speak.\x02\x03",

            "I feel MUCH calmer now, thanks to your\x01",
            "assistance.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    TurnDirection(0xD, 0x104, 400)
    OP_62(0xD, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0xA, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(500)
    OP_9E(0x101, 0xF, 0x0, 0x5DC, 0x1388)

    ChrTalk(    #446
        0x101,
        "#1022F(Y-You iiiiiiidiot!!)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #447
        0xB,
        "If you're satisfied, then, erm...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #448
        0xB,
        (
            "Step--Ahem!--Step back, please!\x01",
            "I can't proceed with the game until\x01",
            "you do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #449
        0x104,
        "#030F#2POh, my apologies. If you'll pardon me.\x02",
    )

    CloseMessageWindow()
    OP_43(0x104, 0x1, 0x1, 0xF)
    Sleep(2000)

    ChrTalk(    #450
        0x101,
        (
            "#1009F#4P(Mmmmrrrrr!)\x02\x03",

            "(He's an idiot, but I'm the bigger idiot\x01",
            "for actually believing in him.)\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0x1)
    OP_8E(0xB, 0x88C2, 0x0, 0x7684, 0x7D0, 0x0)
    OP_8C(0xB, 270, 400)
    Sleep(500)

    ChrTalk(    #451
        0xB,
        "W-Well, then, resuming as we were...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #452
        0xB,
        (
            "You wished to exchange your entire\x01",
            "hand, correct, miss?\x02",
        )
    )

    CloseMessageWindow()

    def lambda_9D54():
        TurnDirection(0x18, 0x101, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_9D54)
    TurnDirection(0x101, 0xB, 400)

    ChrTalk(    #453
        0x101,
        "#1007F#4PYeah, all five.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #454
        0xB,
        "And, here, one card for you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #455
        0xD,
        "#1PHeeheehee... All right, come on!\x02",
    )

    CloseMessageWindow()
    Call(1, 17)
    OP_59()
    Call(2, 19)
    OP_59()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x101, 0xD, 400)
    Sleep(1000)

    ChrTalk(    #456
        0x101,
        (
            "#1020F#4PA r-royal something or...?!\x02\x03",

            "Isn't that the strongest hand?!\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #457
        0x106,
        (
            "#052FWhoa, whoa!\x01",
            "THAT hand, of all things.\x02\x03",

            "The odds of that are next to nothing!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #458
        0x105,
        "#042FIt'll be hard to win against that hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #459
        0x104,
        (
            "#035FHmm...\x02\x03",

            "Are you sure about that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #460
        0x105,
        "#044FHuh...?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x101, 400)

    ChrTalk(    #461
        0xB,
        (
            "Please show your hand as well,\x01",
            "miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #462
        0xB,
        (
            "The conclusion of a match is never\x01",
            "known until the last card is on the\x01",
            "table.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x101, 135, 400)

    ChrTalk(    #463
        0x101,
        (
            "#1007F#4PYeah, yeah, I'll show.\x02\x03",

            "Not much of a point when\x01",
            "I'm up against a hand like that,\x01",
            "but rules are rules.\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 18)
    OP_59()

    ChrTalk(    #464
        0xB,
        "Hmm... It certainly is decisive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #465
        0xB,
        "Ah, but you have spades!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #466
        0xB,
        (
            "In that case, your hand trumps\x01",
            "Phelio's.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #467
        0xD,
        "#1PY-You're kidding me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #468
        0xB,
        "This match is yours, miss.\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x17)

    ChrTalk(    #469
        0x101,
        (
            "#1004F#4PW-We won...?\x02\x03",

            "We won!!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)

    def lambda_A15E():
        OP_95(0x101, 0x0, 0x3E8, 0x0, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_A15E)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Sleep(24)
    OP_51(0x101, 0x4, (scpexpr(EXPR_PUSH_LONG, 0x1E), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))

    ChrTalk(    #470
        0x101,
        "#1001F#3S#4PWoohoo! We won!!\x02",
    )

    CloseMessageWindow()
    OP_59()
    OP_43(0x101, 0x1, 0x1, 0x16)

    ChrTalk(    #471
        0xB,
        "Please check your wager.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #472
        "Received #4C2000#0C mira.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #473
        0x105,
        "#044F#6PWe...won?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #474
        0x104,
        "#031FHahaha. What a splendid turn of events!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x106, 0x104, 400)

    ChrTalk(    #475
        0x106,
        "#057F#1P...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x106, 400)
    Sleep(1000)

    ChrTalk(    #476
        0x104,
        "#031FWh-What is it, Agate?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #477
        0x106,
        (
            "#053F#1PHeh, I see.\x02\x03",

            "So that's why you were acting\x01",
            "so shady.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #478
        0x104,
        (
            "#031FHaha, come now, whatever could\x01",
            "you mean?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #479
        0x106,
        (
            "#551F#1PWell, whatever. I'll pretend I didn't\x01",
            "see it.\x02\x03",

            "It's why we won, so you won't see\x01",
            "me complainin'.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #480
        0x104,
        (
            "#030FHaha, always a pleasure to be at\x01",
            "your service.\x02",
        )
    )

    CloseMessageWindow()
    OP_63(0x101)
    OP_44(0x101, 0x1)
    OP_8E(0x101, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)

    ChrTalk(    #481
        0x101,
        (
            "#1001F#2PHee hee, sorry for holding things up! ♪\x02\x03",

            "Let's go report to the client.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #482
        0x101,
        (
            "#1019F#2PUh, you guys... Why are you gazing\x01",
            "at each other like that?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #483
        0x104,
        (
            "#035F#2PIsn't it obvious?\x02\x03",

            "Agate was so moved by my gallantry\x01",
            "in the second round that he's been dying\x01",
            "to make a move on me ever since.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #484
        0x106,
        (
            "#055F#1PWhat the--? Stop spouting r-random\x01",
            "crap, you dumbass!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x106, 400)

    ChrTalk(    #485
        0x104,
        (
            "#031F#2PCome now, my red-maned beau.\x01",
            "There's no reason to hide your feelings.\x01",
            "Or are we playing hard to get?\x02\x03",

            "Oh, Agate, you shy～little～boy～. ㈱\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x14, 0x17, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #486
        0x101,
        "#1020F#2PUhhhhh...\x02",
    )

    CloseMessageWindow()
    OP_62(0x106, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    TurnDirection(0x106, 0x101, 400)

    ChrTalk(    #487
        0x106,
        (
            "#055F#1PD-Don't listen to him!\x02\x03",

            "C'mon, let's go d-downstairs and\x01",
            "report to the client!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0xD, 0x1)
    OP_28(0x68, 0x1, 0x400)
    Call(1, 19)
    Return()

    label("loc_A79E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BB1F")
    Call(2, 14)
    OP_59()
    Sleep(400)
    TurnDirection(0x103, 0xD, 400)

    ChrTalk(    #488
        0x103,
        "#027F#4P(Now, how's my opponent looking?)\x02",
    )

    CloseMessageWindow()
    Call(1, 24)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0x106, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x104, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    OP_6D(29690, 0, 31480, 1000)

    ChrTalk(    #489
        0x105,
        "#045F(He's changed his tune.)\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #490
        0x101,
        (
            "#1002F(Yes, he's acting like he's got\x01",
            "a good hand.)\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #491
        0x104,
        (
            "#030F(Now, how will you proceed in turn,\x01",
            "Schera?)\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    FadeToDark(300, 0, 100)
    OP_C5(0x0, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x1, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E1, 0xEE, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x2, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DF, 0xEC, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x3, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DD, 0xEA, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x4, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1DB, 0xE8, 0x200, 0x200, 0x0, 0x0, 0x64, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x5, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xA3, 0xE8, 0x200, 0x200, 0x64, 0x140, 0xC8, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x6, 0xFFCE, 0xFFB0, 0x32, 0x50, 0xF3, 0xEA, 0x200, 0x200, 0x190, 0x140, 0x1F4, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x7, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x143, 0xEC, 0x200, 0x200, 0x64, 0x0, 0xC8, 0xA0, 0xFFFFFF, 0x0, "C_VIS228._CH")
    OP_C5(0x8, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x193, 0xEE, 0x200, 0x200, 0x0, 0x140, 0x64, 0x1E0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C5(0x9, 0xFFCE, 0xFFB0, 0x32, 0x50, 0x1E3, 0xF0, 0x200, 0x200, 0x12C, 0x0, 0x190, 0xA0, 0xFFFFFF, 0x0, "C_VIS229._CH")
    OP_C6(0x5, 0x3, -1, 400, 0)
    OP_C6(0x6, 0x3, -1, 400, 0)
    OP_C6(0x7, 0x3, -1, 400, 0)
    OP_C6(0x8, 0x3, -1, 400, 0)
    OP_C6(0x9, 0x3, -1, 400, 0)
    Sleep(1000)
    TurnDirection(0x103, 0xB, 0)
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #492
        (
            "#022F(One look and it's clear that Phelio's\x01",
            "got a big hand.)\x02\x03",

            "(In that case, a normal hand stands\x01",
            "a high chance of losing.)\x02\x03",

            "(Should I go for broke and pursue\x01",
            "a straight flush, I wonder?)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Swap Leaving The Ace Pair\x01",               # 0
            "Exchange Everything But The Spades\x01",      # 1
        )
    )

    MenuEnd(0x3)
    OP_5F(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_56(0x0)
    OP_AE(0x1F4)
    Sleep(1000)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ACEE")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Scherazard")

    AnonymousTalk(    #493
        (
            "#022F(An pair of aces isn't a hand to ignore.)\x02\x03",

            "(All right, let's go with this hand.)\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_ACEE")

    label("loc_ACEE")

    Call(2, 23)
    OP_C7(0x1, 0xFF, 0x0)
    OP_C6(0x0, 0x6, 0, 0, 0)
    OP_C6(0x1, 0x6, 0, 0, 0)
    OP_C6(0x2, 0x6, 0, 0, 0)
    OP_C6(0x3, 0x6, 0, 0, 0)
    OP_C6(0x4, 0x6, 0, 0, 0)
    OP_C6(0x5, 0x6, 0, 0, 0)
    OP_C6(0x6, 0x6, 0, 0, 0)
    OP_C6(0x7, 0x6, 0, 0, 0)
    OP_C6(0x8, 0x6, 0, 0, 0)
    OP_C6(0x9, 0x6, 0, 0, 0)
    FadeToBright(300, 0)
    Sleep(1000)
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #494
        0xB,
        "Would you like to change cards?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ADF8")

    ChrTalk(    #495
        0x103,
        "#022F#4PThree cards, please.\x02",
    )

    CloseMessageWindow()
    Jump("loc_AE18")

    label("loc_ADF8")


    ChrTalk(    #496
        0x103,
        "#022F#4PTwo cards, please.\x02",
    )

    CloseMessageWindow()

    label("loc_AE18")

    TurnDirection(0xB, 0xD, 400)

    ChrTalk(    #497
        0xB,
        "And for you?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #498
        0xD,
        "#1PO-One card, please.\x02",
    )

    CloseMessageWindow()
    OP_59()
    Call(2, 15)
    OP_59()
    Call(1, 17)
    OP_59()
    Call(2, 19)
    OP_59()

    ChrTalk(    #499
        0x103,
        "#022F#4P...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()

    ChrTalk(    #500
        0x101,
        (
            "#1020F#3PA r-royal something or...?!\x02\x03",

            "Isn't that the strongest hand?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #501
        0x105,
        "#042FIt'll be hard to win against that hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #502
        0x104,
        "#032F#4PHmm...\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_0D()
    TurnDirection(0xB, 0x103, 400)

    ChrTalk(    #503
        0xB,
        (
            "Please show your hand as well,\x01",
            "miss.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #504
        0xB,
        (
            "The conclusion of a match is never\x01",
            "known until the last card is on the\x01",
            "table.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B352")

    ChrTalk(    #505
        0x103,
        (
            "#025F#4PI'd normally be inclined to agree,\x01",
            "but I think but there's no mistaking\x01",
            "who the winner is today.\x02",
        )
    )

    CloseMessageWindow()
    Call(2, 17)
    OP_59()

    ChrTalk(    #506
        0xB,
        "Hmm... It certainly is decisive...\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)

    ChrTalk(    #507
        0xB,
        "This match...is Phelio's victory.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #508
        0xD,
        "#1PHahaha. Naturally.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #509
        0xD,
        (
            "#1PYou fought well, but you can't\x01",
            "win against a master of gambling.\x02",
        )
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_8C(0xD, 90, 0)
    OP_0D()

    ChrTalk(    #510
        0x105,
        "#043F#6P*sigh* We lost.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #511
        0x104,
        (
            "#030F#2PIt was a close match.\x01",
            "You had an opening, but I suppose\x01",
            "it wasn't meant to be.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_B18B():

        label("loc_B18B")

        TurnDirection(0x104, 0x103, 400)
        OP_48()
        Jump("loc_B18B")

    QueueWorkItem2(0x104, 1, lambda_B18B)
    OP_8E(0x103, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #512
        0x103,
        (
            "#025FSorry for losing like that.\x02\x03",

            "I had a hand that could have\x01",
            "challenged him. I just lost my\x01",
            "cool towards the end.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #513
        0x101,
        (
            "#1003F#1PNo, if you couldn't do it, Schera,\x01",
            "no one could.\x02\x03",

            "#1015FBut, crap... This means we failed\x01",
            "our job, huh?\x02\x03",

            "*sigh* How can I look the client in\x01",
            "the eye now?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #514
        0x103,
        (
            "#026FEven if we don't have any excuses,\x01",
            "we have to report.\x02\x03",

            "That's the hardest part of the job.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_28(0x68, 0x1, 0x800)
    Call(1, 18)
    Return()

    label("loc_B352")


    ChrTalk(    #515
        0x103,
        "#021F#4PIndeed.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xD, 0x103, 400)

    ChrTalk(    #516
        0xD,
        "#1PHmph. Showing your cards won't help.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #517
        0xD,
        (
            "#1PNot when I've got the best hand a guy\x01",
            "could ask for!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #518
        0x103,
        "#027F#4POh, is that really so?\x02",
    )

    CloseMessageWindow()
    OP_59()
    FadeToDark(300, 0, 100)
    OP_D9(0x0, "CTI00120")
    OP_22(0x21F, 0x0, 0x64)
    Sleep(2000)
    OP_D9(0x1)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(29690, 0, 31480, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #519
        0x101,
        "#1004FHuh...?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x105, 0x101, 400)

    ChrTalk(    #520
        0x105,
        "#044FWhat is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #521
        0x101,
        (
            "#1015FJust now, wasn't Schera's hand...?\x02\x03",

            "...\x02\x03",

            "#1016FS-Sorry. I think it was my imagination.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #522
        0x105,
        "#040FHm?\x02",
    )

    CloseMessageWindow()
    OP_59()
    Fade(1000)
    OP_6D(32073, 0, 31585, 0)
    OP_8C(0x105, 90, 0)
    OP_0D()
    Call(2, 18)
    OP_59()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #523
        0xD,
        "#1PN-No way!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #524
        0xB,
        "Hmm... It certainly is decisive...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #525
        0xB,
        "Ah, but you have spades!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #526
        0xB,
        (
            "In that case, your hand trumps\x01",
            "Phelio's.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)

    def lambda_B5D8():
        OP_95(0xD, 0x0, 0x3E8, 0x0, 0x1F4, 0x1388)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_B5D8)
    TurnDirection(0xD, 0xB, 400)

    ChrTalk(    #527
        0xD,
        "#1PY-You're kidding!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #528
        0xB,
        "This match is yours, miss.\x02",
    )

    CloseMessageWindow()
    OP_43(0xD, 0x1, 0x1, 0x17)

    ChrTalk(    #529
        0x103,
        "#025F#4PPhew! My goodness...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #530
        0xB,
        "Please check your wager.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #531
        "Received #4C2000#0C mira.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Fade(1000)
    OP_6D(27210, 0, 33050, 0)
    OP_0D()

    ChrTalk(    #532
        0x101,
        "#1008F#1PAhaha. I don't know how, but we won.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #533
        0x105,
        "#045F#6PI-I can't believe it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #534
        0x104,
        "#031FHahaha. What a splendid turn of events!\x02",
    )

    CloseMessageWindow()

    def lambda_B76A():

        label("loc_B76A")

        TurnDirection(0x104, 0x103, 400)
        OP_48()
        Jump("loc_B76A")

    QueueWorkItem2(0x104, 1, lambda_B76A)
    OP_8E(0x103, 0x74CC, 0x0, 0x7B02, 0x7D0, 0x0)
    OP_44(0x104, 0x1)

    ChrTalk(    #535
        0x101,
        (
            "#1001F#1PSchera, great work!\x02\x03",

            "I can't believe you turned that around!\x01",
            "Awww, you're just the best. ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #536
        0x104,
        "#031F#2PHa! A good show.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x104, 400)

    ChrTalk(    #537
        0x103,
        (
            "#027FIt's been a while since I was\x01",
            "that nervous.\x02\x03",

            "#525FI'm just glad I didn't stumble\x01",
            "all over myself.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #538
        0x101,
        "#1011F#1PHuh? What do you mean?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x104, 0x101, 400)

    ChrTalk(    #539
        0x104,
        "#035F#2POh, it's complicated.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #540
        0x105,
        "#040F#6P???\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #541
        0x101,
        (
            "#1004F#1PWait a sec...\x02\x03",

            "N-No way!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0x101, 400)

    ChrTalk(    #542
        0x103,
        (
            "#023FOh, didn't you realize?\x02\x03",

            "I thought you and Olivier had seen\x01",
            "through it.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)

    ChrTalk(    #543
        0x101,
        (
            "#1022F#1PI-I can't believe you...you...\x02\x03",

            "No wonder something was off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #544
        0x103,
        (
            "#021FYou know how it goes--sometimes\x01",
            "it takes a thief to catch a thief.\x02\x03",

            "#020FAll right, let's go report to the client.\x02\x03",

            "I don't think they noticed, but it's\x01",
            "probably best if we don't linger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #545
        0x101,
        (
            "#1002F#1PWorks for me.\x02\x03",

            "Let's go give Lakeisha the good news.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    Sleep(1000)
    OP_44(0xD, 0x1)
    OP_28(0x68, 0x1, 0x1000)
    Call(1, 19)

    label("loc_BB1F")

    Return()

    # Function_4_8803 end

    def Function_5_BB20(): pass

    label("Function_5_BB20")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7260, 0x0, 0x7F8A, 0x41A, 0x0)
    OP_8E(0xFE, 0x7A1C, 0x0, 0x77E2, 0x41A, 0x0)
    Return()

    # Function_5_BB20 end

    def Function_6_BB50(): pass

    label("Function_6_BB50")

    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_8E(0xFE, 0x75D0, 0x0, 0x80AC, 0x3E8, 0x0)
    OP_8E(0xFE, 0x7A12, 0x0, 0x7C6A, 0x3E8, 0x0)
    Return()

    # Function_6_BB50 end

    def Function_7_BB85(): pass

    label("Function_7_BB85")

    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x7134, 0x0, 0x7C88, 0x41A, 0x0)
    OP_8E(0xFE, 0x75DA, 0x0, 0x7814, 0x41A, 0x0)
    Return()

    # Function_7_BB85 end

    def Function_8_BBB5(): pass

    label("Function_8_BBB5")

    OP_8C(0xFE, 180, 400)
    Sleep(200)
    OP_8E(0xFE, 0x7468, 0x0, 0x7D64, 0x3E8, 0x0)
    TurnDirection(0xFE, 0xD, 400)
    Return()

    # Function_8_BBB5 end

    def Function_9_BBDD(): pass

    label("Function_9_BBDD")

    TurnDirection(0xFE, 0xB, 400)
    Return()

    # Function_9_BBDD end

    def Function_10_BBE5(): pass

    label("Function_10_BBE5")

    TurnDirection(0xFE, 0x19, 400)
    Return()

    # Function_10_BBE5 end

    def Function_11_BBED(): pass

    label("Function_11_BBED")

    TurnDirection(0xFE, 0x104, 400)
    Return()

    # Function_11_BBED end

    def Function_12_BBF5(): pass

    label("Function_12_BBF5")

    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_12_BBF5 end

    def Function_13_BBFD(): pass

    label("Function_13_BBFD")

    OP_69(0xD, 0x7D0)
    Return()

    # Function_13_BBFD end

    def Function_14_BC05(): pass

    label("Function_14_BC05")

    OP_8E(0x104, 0x79C2, 0x0, 0x7FC6, 0x7D0, 0x0)
    OP_8E(0x104, 0x8868, 0x0, 0x7DFD, 0x7D0, 0x0)
    OP_8E(0x104, 0x8949, 0x0, 0x792F, 0x7D0, 0x0)
    Return()

    # Function_14_BC05 end

    def Function_15_BC42(): pass

    label("Function_15_BC42")

    OP_8E(0x104, 0x8868, 0x0, 0x7DFD, 0x7D0, 0x0)
    OP_8E(0x104, 0x79C2, 0x0, 0x7FC6, 0x7D0, 0x0)
    OP_8E(0x104, 0x70B2, 0x0, 0x7EF4, 0x7D0, 0x0)
    TurnDirection(0x104, 0x101, 400)
    Return()

    # Function_15_BC42 end

    def Function_16_BC86(): pass

    label("Function_16_BC86")

    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_BCA3():
        TurnDirection(0xB, 0x104, 400)
        ExitThread()

    QueueWorkItem(0xB, 2, lambda_BCA3)

    def lambda_BCB1():
        TurnDirection(0x18, 0xB, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_BCB1)
    OP_8F(0xB, 0x88D5, 0x0, 0x7134, 0x1F40, 0x0)
    OP_62(0x18, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Return()

    # Function_16_BC86 end

    def Function_17_BCE0(): pass

    label("Function_17_BCE0")

    Sleep(1000)

    ChrTalk(    #546
        0xB,
        "Do you have your cards?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #547
        0xB,
        "Now, if you would...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #548
        0xB,
        "Please show your hands.\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #549
        0xD,
        "#1POkay, I'll show first.\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_17_BCE0 end

    def Function_18_BD5E(): pass

    label("Function_18_BD5E")

    OP_28(0x68, 0x4, 0x40)
    OP_28(0x68, 0x4, 0x80)
    OP_22(0x106, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #550
        "Quest #2C[Recruiting Great Gamblers] #0Cfailed...\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4A(0xE, 0)
    OP_4A(0xE, 0)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0xC)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #551
        0x101,
        (
            "#1003F#6P...And that's what happened.\x02\x03",

            "Our best efforts fell flat, and we lost.\x02\x03",

            "#1007FI am really, really sorry.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_BEF9")

    ChrTalk(    #552
        0x106,
        (
            "#053FSorry. We have no excuse.\x02\x03",

            "This was totally due to our inability.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_BF5F")

    label("loc_BEF9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_BF5F")

    ChrTalk(    #553
        0x103,
        (
            "#025FSorry, there's really no room for an excuse.\x02\x03",

            "This was totally due to our inability.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_BF5F")


    ChrTalk(    #554
        0xE,
        "I see... So my plan backfired.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #555
        0xE,
        (
            "I suppose there's nothing that can be\x01",
            "done at this point. Gambling's a\x01",
            "game of luck, and our luck went sour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #556
        0xE,
        (
            "You realize, though, that I was expecting\x01",
            "a little more than luck from bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #557
        0x101,
        "#1007F#6PS-Sorry...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #558
        0x104,
        (
            "#035FI agree that our aid was less than desirable,\x01",
            "there's no greater pain to a man's heart than\x01",
            "disappointing a woman of your caliber. \x02\x03",

            "#030FBe that as it may, I wouldn't worry about\x01",
            "your husband.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x1, 0xB)
    OP_43(0x105, 0x1, 0x1, 0xB)
    OP_43(0xE, 0x1, 0x1, 0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C155")
    OP_43(0x106, 0x1, 0x1, 0xB)
    Jump("loc_C163")

    label("loc_C155")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C163")
    OP_43(0x103, 0x1, 0x1, 0xB)

    label("loc_C163")


    ChrTalk(    #559
        0xE,
        "Oh? Why?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #560
        0x101,
        "#1004FHey, Olivier...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C1C9")

    ChrTalk(    #561
        0x106,
        (
            "#050FC'mon.\x02\x03",

            "Let's hear what he's got to say.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C203")

    label("loc_C1C9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C203")

    ChrTalk(    #562
        0x103,
        (
            "#020FCome on.\x02\x03",

            "Let's hear what he has to say.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C203")


    ChrTalk(    #563
        0x101,
        "#1015FO-Okay...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #564
        0x104,
        (
            "#035FPardon me for spilling a few trade secrets,\x01",
            "but most casinos have a person who is their\x01",
            "ace in the hole, so to speak.\x02\x03",

            "Someone who normally doesn't work in\x01",
            "the shop--the house's strongest dealer.\x02\x03",

            "#030FIf I were to venture an educated guess...\x02\x03",

            "I don't believe this establishment has\x01",
            "played their 'ace' yet.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C38F")

    ChrTalk(    #565
        0x106,
        "#052FSo, what? You think that guy's next?\x02",
    )

    CloseMessageWindow()
    Jump("loc_C3C9")

    label("loc_C38F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C3C9")

    ChrTalk(    #566
        0x103,
        "#023FSo you're saying that person is up next?\x02",
    )

    CloseMessageWindow()

    label("loc_C3C9")

    TurnDirection(0x104, 0xF7, 400)

    ChrTalk(    #567
        0x104,
        (
            "#030FYes. We've lost, so I suspect they'll\x01",
            "be making an appearance soon\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #568
        0x101,
        "#1015FAn ace in the hole... Huh.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #569
        0xE,
        "*sigh* I hope you're right.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #570
        0xE,
        (
            "What do you think? Can I really trust\x01",
            "what he's said?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(100)
    OP_62(0x105, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(150)
    OP_62(0xF7, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    def lambda_C4F9():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_C4F9)

    def lambda_C507():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_C507)

    def lambda_C515():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF7, 1, lambda_C515)
    OP_8C(0x104, 0, 400)

    ChrTalk(    #571
        0x101,
        (
            "#1016F#6PHaha, I dunno.\x02\x03",

            "I think you'll have to judge for yourself\x01",
            "how trustworthy that is.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #572
        0xE,
        (
            "Anyway, he'll have to come down\x01",
            "eventually. Till then, I'm waiting right\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #573
        0xE,
        (
            "I'll have to prepare for the worst in\x01",
            "case things don't turn out like you\x01",
            "said.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C688")

    ChrTalk(    #574
        0x106,
        (
            "#050FIn that case, we'll be moving on.\x02\x03",

            "Again, we're very sorry for today.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C6DF")

    label("loc_C688")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C6DF")

    ChrTalk(    #575
        0x103,
        (
            "#020FWell, then, we'll take our leave.\x02\x03",

            "Again, we're very sorry for today.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C6DF")


    ChrTalk(    #576
        0xE,
        "I believe you did the best you could.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #577
        0xE,
        (
            "If anything comes up again, I'm sure\x01",
            "I could still count on you to take on\x01",
            "the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #578
        0x101,
        "#1006F#6PYeah, ask us any time.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x7)
    OP_8C(0xE, 180, 0)
    OP_4B(0xE, 255)
    OP_4B(0xE, 255)
    OP_4B(0xD, 255)
    OP_4B(0x18, 255)
    OP_4B(0xB, 255)
    OP_8C(0x18, 270, 0)
    OP_8C(0xB, 270, 0)
    Return()

    # Function_18_BD5E end

    def Function_19_C7B5(): pass

    label("Function_19_C7B5")

    OP_28(0x68, 0x4, 0x10)
    OP_4A(0xE, 0)
    SetChrPos(0x101, 5600, 250, 33020, 0)
    SetChrPos(0xF7, 4770, 250, 32659, 0)
    SetChrPos(0x104, 5560, 250, 31520, 0)
    SetChrPos(0x105, 4580, 250, 31210, 0)
    OP_6D(4960, 250, 33040, 0)
    OP_20(0x3E8)
    OP_21()
    OP_1D(0xC)
    Sleep(400)
    FadeToBright(2000, 0)
    OP_0D()

    ChrTalk(    #579
        0xE,
        "Really?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #580
        0xE,
        "You really beat my husband?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #581
        0x101,
        (
            "#1006F#6PYeah, it was rough, but we took\x01",
            "him down.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_C8E0")

    ChrTalk(    #582
        0x106,
        (
            "#050FHere's your wager back.\x02\x03",

            "Your 1000 mira's doubled to 2000.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C933")

    label("loc_C8E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_C933")

    ChrTalk(    #583
        0x103,
        (
            "#020FThis here's your wager.\x02\x03",

            "The 1000 mira has doubled after our win.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C933")


    ChrTalk(    #584
        0xE,
        "Ah, that's fine. You can have that.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #585
        0xE,
        (
            "Think of it as making up for how\x01",
            "cheap the job pay was.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #586
        0x101,
        (
            "#1011F#6PHuh? Are you sure?\x02\x03",

            "I mean, I'm grateful, but, you know.\x02\x03",

            "#1015FAre you sure what we did is enough?\x02\x03",

            "I don't know if your husband will\x01",
            "learn his lesson just because he\x01",
            "lost against us.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #587
        0xE,
        (
            "Even if he doesn't, I'm sure the\x01",
            "casino will finish the job.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #588
        0xE,
        (
            "They're professionals in their own right,\x01",
            "after all. There's no way they'll let my\x01",
            "husband keep on this winning streak of his.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CB80")

    ChrTalk(    #589
        0x106,
        (
            "#051FHeh, true enough.\x02\x03",

            "#050FIn that case, we'll be moving on.\x02\x03",

            "That okay?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CBE6")

    label("loc_CB80")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CBE6")

    ChrTalk(    #590
        0x103,
        (
            "#021FThat's a good point.\x02\x03",

            "#020FIf that's the case, we'll be moving along.\x02\x03",

            "Is that okay?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CBE6")


    ChrTalk(    #591
        0xE,
        (
            "Yes, it's fine.\x01",
            "You've done more than enough.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #592
        0xE,
        (
            "I'm amazed you took a bizarre request\x01",
            "like this as seriously as you did, but\x01",
            "you guys have been true professionals.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #593
        0xE,
        (
            "You've done the Bracer Guild's reputation\x01",
            "justice in my eyes.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #594
        0x101,
        (
            "#1001F#6PHeehee, thanks.\x02\x03",

            "We're just doing our job, but it feels\x01",
            "awfully good to hear you say that!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #595
        0xE,
        (
            "If anything else happens, I'll be\x01",
            "sure to look you guys up.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_END)), "loc_CDAE")

    ChrTalk(    #596
        0x106,
        "#051FYeah, come to us any time.\x02",
    )

    CloseMessageWindow()
    Jump("loc_CDE8")

    label("loc_CDAE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_END)), "loc_CDE8")

    ChrTalk(    #597
        0x103,
        "#020FYes, we'll be here any time you need it.\x02",
    )

    CloseMessageWindow()

    label("loc_CDE8")

    OP_A2(0x7)
    AddMira(2000)
    OP_22(0x17, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #598
        "Quest #2C[Recruiting Great Gamblers] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_4B(0xE, 255)
    OP_4B(0xD, 255)
    OP_4B(0x18, 255)
    OP_4B(0xB, 255)
    OP_8C(0x18, 270, 0)
    OP_8C(0xB, 270, 0)
    Return()

    # Function_19_C7B5 end

    def Function_20_CE71(): pass

    label("Function_20_CE71")

    OP_8E(0xB, 0x8944, 0x0, 0x6FAE, 0x3E8, 0x0)
    TurnDirection(0x18, 0xB, 400)
    OP_4A(0x18, 255)
    OP_A5(0x10)

    def lambda_CE99():
        OP_8C(0x18, 270, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_CE99)
    OP_8E(0xB, 0x88C2, 0x0, 0x7684, 0x3E8, 0x0)
    OP_8C(0xB, 270, 400)
    Return()

    # Function_20_CE71 end

    def Function_21_CEBD(): pass

    label("Function_21_CEBD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CEF7")
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1000)
    Jump("Function_21_CEBD")

    label("loc_CEF7")

    Return()

    # Function_21_CEBD end

    def Function_22_CEF8(): pass

    label("Function_22_CEF8")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF1B")
    OP_62(0xFE, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1500)
    Jump("Function_22_CEF8")

    label("loc_CF1B")

    Return()

    # Function_22_CEF8 end

    def Function_23_CF1C(): pass

    label("Function_23_CF1C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_CF3F")
    OP_62(0xFE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(1500)
    Jump("Function_23_CF1C")

    label("loc_CF3F")

    Return()

    # Function_23_CF1C end

    def Function_24_CF40(): pass

    label("Function_24_CF40")

    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #599
        0xD,
        "#1P...Hmm?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #600
        0xD,
        "#1PI've got it! IT'S HERE!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    OP_62(0xD, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)

    ChrTalk(    #601
        0xD,
        "#1PCould it be...?!\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 0, 400)
    Sleep(2000)

    ChrTalk(    #602
        0xD,
        "#1PN-No, it's nothing.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #603
        0xD,
        "#1PD-Don't worry about it, really.\x02",
    )

    CloseMessageWindow()
    OP_8C(0xD, 90, 400)
    Sleep(1000)

    ChrTalk(    #604
        0xD,
        "#1PAaaahhh, what a cruddy hand.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #605
        0xD,
        "#1POh, man, I'm done for...\x02",
    )

    CloseMessageWindow()
    Return()

    # Function_24_CF40 end

    SaveToFile()

Try(main)
