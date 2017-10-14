from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'T1103_1 ._SN',
        MapName             = 'Bose',
        Location            = 'T1103.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/T1103   ._SN',
            'ED6_DT21/T1103_1 ._SN',
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
        "Function_1_AB",           # 01, 1
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    Return()

    # Function_0_AA end

    def Function_1_AB(): pass

    label("Function_1_AB")

    TalkBegin(0x35)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C1")
    TurnDirection(0x4, 0x35, 0)

    label("loc_C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_118")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_118")
    TurnDirection(0x35, 0x101, 400)

    ChrTalk(    #0
        0x35,
        "What is it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x35,
        "Weren't you in a hurry?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x35, 0, 0)
    TalkEnd(0x35)
    Return()

    label("loc_118")

    Fade(1000)
    EventBegin(0x0)
    OP_6D(47700, 0, 47800, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2700, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0xF6, 48200, 0, 48120, 90)
    SetChrPos(0xF7, 48100, 0, 47360, 90)
    SetChrPos(0xF8, 47200, 0, 48130, 90)
    SetChrPos(0xF9, 47100, 0, 47320, 90)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xE), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BD")
    SetChrPos(0x4, 46150, 0, 47720, 90)

    label("loc_1BD")

    OP_0D()
    OP_62(0x35, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)
    OP_63(0x35)
    TurnDirection(0x35, 0x101, 400)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x7B, 0x1, 0x2000)"), scpexpr(EXPR_END)), "loc_2DC")

    ChrTalk(    #2
        0x35,
        "Say, are you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1007F#6PYeah, sorry about before.\x01",
            "Didn't really get to say, 'hi.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x35,
        "No, don't worry about it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x35,
        "I gather you're rather busy with work.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x101,
        (
            "#1006F#6PYou could say that.\x02\x03",

            "Are you here in Bose on work, too?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_2DC")


    ChrTalk(    #7
        0x35,
        "Say, are you...?\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x65, 0x0, 0x10)"), scpexpr(EXPR_END)), "loc_55F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_50B")

    ChrTalk(    #8
        0x101,
        (
            "#1000F#6POh, hey, you're the merchant who\x01",
            "was in Ruan!\x02\x03",

            "Are you working in Bose now?\x02\x03",

            "#1007F...Wait, now's not the time for this.\x02\x03",

            "We need to get to Ravennue, pronto!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x35,
        "You look like you're in a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x35,
        (
            "You're involved with this madness,\x01",
            "I assume?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1002F#6PYeah, I'm sorry, Orvid, but we're right\x01",
            "in the middle of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x35,
        (
            "Clearly! Don't worry, we can catch\x01",
            "up another time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x35,
        "Good luck to you. And be careful, now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1002F#6PYou be careful, too!\x02\x03",

            "We'll see you later.\x02",
        )
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0x35, 0, 0)
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    label("loc_50B")


    ChrTalk(    #15
        0x101,
        (
            "#1004F#6POh, you were in Manoria last, right?\x02\x03",

            "#1000FSo you're in Bose now?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_8A7")

    label("loc_55F")


    ChrTalk(    #16
        0x101,
        (
            "#1004F#6PWait, I know you. Orvid, right?\x02\x03",

            "Wow, it feels like it's been forever!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_5E8")

    ChrTalk(    #17
        0x106,
        "#052FSomeone you know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x106, 400)
    Jump("loc_690")

    label("loc_5E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_620")

    ChrTalk(    #18
        0x103,
        "#023FOh, someone you know?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x103, 400)
    Jump("loc_690")

    label("loc_620")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_656")

    ChrTalk(    #19
        0x108,
        "#070FYou know him, then?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x108, 400)
    Jump("loc_690")

    label("loc_656")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_690")

    ChrTalk(    #20
        0x104,
        "#030FAn acquaintance, I assume?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x104, 400)

    label("loc_690")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x342, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #21
        0x101,
        (
            "#1000F#6PYeah, Orvid's a merchant who gets\x01",
            "really er, 'special' ingredients.\x02\x03",

            "#1007F...Wait, now's not the time for this.\x02\x03",

            "We need to get to Ravennue, pronto!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x35,
        "You look like you're in a hurry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x35,
        (
            "Don't let me take your time.\x01",
            "Go do what you gotta do.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x35, 400)

    ChrTalk(    #24
        0x101,
        "#1002F#6PYeah, sorry. Pardon us!\x02",
    )

    CloseMessageWindow()
    OP_28(0x7B, 0x1, 0x2000)
    OP_8C(0x35, 0, 0)
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    label("loc_7E4")


    ChrTalk(    #25
        0x101,
        (
            "#1000FYeah, Orvid's a merchant who gets\x01",
            "really er, 'special' ingredients.\x02\x03",

            "I did a job for him a long time ago.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x35, 400)

    ChrTalk(    #26
        0x101,
        (
            "#1011F#6PSo, are you chasing the perfect ingredients\x01",
            "in Bose now?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_8A7")


    ChrTalk(    #27
        0x35,
        (
            "You know me too well! I'm coming to the\x01",
            "end of a long road.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x35,
        (
            "My ultimate goal is to secure a deal with\x01",
            "the Anterose.\x02\x03",

            "My first plan was to sell some of my\x01",
            "ingredients in the market...\x02\x03",

            "But, well, then this madness happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #29
        0x101,
        (
            "#1015F#6PArgh. Sorry, not really following.\x02\x03",

            "Your goal's to sell stuff to the Anterose\x01",
            "restaurant...but first you're going to sell\x01",
            "in the market? Why?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x35,
        (
            "If I could, I'd love to approach them\x01",
            "directly.\x02\x03",

            "However, they won't deal with anyone\x01",
            "who lacks a glowing recommendation\x01",
            "from a trustworthy source.\x02\x03",

            "Given how famous they are, it's only\x01",
            "natural they'd be cautious.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1004F#6PYeah, guess that's the Anterose for you.\x01",
            "They're kinda choosy... Maybe TOO choosy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x35,
        (
            "By the by, you're working in Bose for now,\x01",
            "I take it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1015F#6PYeah, as you saw, some...stuff happened.\x02\x03",

            "#1011FSpeaking of stuff...\x02\x03",

            "We actually have a job from the Anterose\x01",
            "at this very moment.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CA7")

    ChrTalk(    #34
        0x106,
        (
            "#050FYeah, we're collecting some ingredients\x01",
            "for 'em ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_CA7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_CFE")

    ChrTalk(    #35
        0x103,
        (
            "#020FYeah, we're collecting some ingredients\x01",
            "for them ourselves.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_CFE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D4A")

    ChrTalk(    #36
        0x108,
        (
            "#070FWe're the ones collecting ingredients this\x01",
            "time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_DAB")

    label("loc_D4A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DAB")

    ChrTalk(    #37
        0x104,
        (
            "#030FOur charge is to find certain ingredients\x01",
            "for them. A funny coincidence.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_DAB")

    OP_62(0x35, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #38
        0x35,
        (
            "WHAT?! Collecting ingredients?!\x02\x03",

            "And for the Anterose itself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1007F#6PYeah, it's been kind of a pain in the butt.\x02\x03",

            "They're looking for some REALLY\x01",
            "weird stuff.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x35,
        (
            "Well, well! You've got my attention.\x02\x03",

            "What ingredients do you need,\x01",
            "out of pure, academic curiosity?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        (
            "#1015F#6PUh, one sec. I've got the list in my\x01",
            "notebook...\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #42
        (
            "\x07\x05Estelle showed Orvid the list of ingredients from the\x01",
            "Anterose.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    ChrTalk(    #43
        0x35,
        (
            "HA HA HA! Is that really all?\x02\x03",

            "I practically walk around with this\x01",
            "kind of stuff all the time!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x101,
        "#1004F#6PWhaaaa...? Seriously?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109D")

    ChrTalk(    #45
        0x109,
        (
            "#1060FWell, heeeey. How's that for some\x01",
            "divine guidance?\x02\x03",

            "How about we take Aidios up on the help\x01",
            "and enlist Mr. Orvid's aid?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1237")

    label("loc_109D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1108")

    ChrTalk(    #46
        0x104,
        (
            "#030FHow utterly convenient!\x02\x03",

            "Beloved companions, why not enlist\x01",
            "the good man's aid?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1237")

    label("loc_1108")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_115B")

    ChrTalk(    #47
        0x108,
        (
            "#070FWeird coincidence, huh?\x02\x03",

            "Why don't we ask for his help?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1237")

    label("loc_115B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11DC")

    ChrTalk(    #48
        0x103,
        (
            "#020FAren't we lucky! Well, I won't look this\x01",
            "gift horse in the mouth.\x02\x03",

            "Perhaps we can strike a deal here?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1237")

    label("loc_11DC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1237")

    ChrTalk(    #49
        0x106,
        (
            "#051FTalk about a weird coincidence.\x02\x03",

            "How 'bout we help each other out?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1237")


    ChrTalk(    #50
        0x35,
        (
            "I would ask it of you before you ask me!\x01",
            "This is perfect for both of us.\x02\x03",

            "I'll be happy to provide you with the\x01",
            "ingredients if you'll introduce me to\x01",
            "the manager of the Anterose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x101,
        (
            "#1017F#6POh, that's all?\x02\x03",

            "Sure, we can do that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x35,
        "It's a deal, then!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/T1131   ._SN", 103, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    TalkEnd(0x35)
    Return()

    # Function_1_AB end

    SaveToFile()

Try(main)
