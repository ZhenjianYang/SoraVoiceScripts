from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0211   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0211.x',
        MapIndex            = 12,
        MapDefaultBGM       = "ed60084",
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
        'Mylene',                               # 9
        'Lita',                                 # 10
        'Mayor Klaus',                          # 11
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


    AddCharChip(
        'ED6_DT07/CH01180 ._CH',             # 00
        'ED6_DT26/CH20330 ._CH',             # 01
        'ED6_DT07/CH02350 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH01180P._CP',             # 00
        'ED6_DT26/CH20330P._CP',             # 01
        'ED6_DT07/CH02350P._CP',             # 02
    )

    DeclNpc(
        X                   = 200400,
        Z                   = 0,
        Y                   = 48360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 201800,
        Z                   = 0,
        Y                   = 48800,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 77760,
        Z                   = 0,
        Y                   = 3410,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_171",          # 01, 1
        "Function_2_180",          # 02, 2
        "Function_3_2FD",          # 03, 3
        "Function_4_3DD",          # 04, 4
        "Function_5_F14",          # 05, 5
        "Function_6_FF1",          # 06, 6
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_159")
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    OP_4A(0x9, 255)

    label("loc_159")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_170")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 5)

    label("loc_170")

    Return()

    # Function_0_122 end

    def Function_1_171(): pass

    label("Function_1_171")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_17F")
    OP_6F(0x5, 10)

    label("loc_17F")

    Return()

    # Function_1_171 end

    def Function_2_180(): pass

    label("Function_2_180")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A5")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2E7")

    label("loc_1A5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2E7")

    label("loc_1BE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D7")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2E7")

    label("loc_1D7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1F0")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2E7")

    label("loc_1F0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_209")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2E7")

    label("loc_209")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2E7")

    label("loc_222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23B")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2E7")

    label("loc_23B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2E7")

    label("loc_254")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2E7")

    label("loc_26D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2E7")

    label("loc_286")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2E7")

    label("loc_29F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B8")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2E7")

    label("loc_2B8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D1")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2E7")

    label("loc_2D1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2E7")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2FC")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2E7")

    label("loc_2FC")

    Return()

    # Function_2_180 end

    def Function_3_2FD(): pass

    label("Function_3_2FD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_30C")
    Call(0, 6)
    Jump("loc_3DC")

    label("loc_30C")

    TalkBegin(0x8)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_386")

    ChrTalk(    #0
        0xFE,
        (
            "If anything happens, we'll contact\x01",
            "the guild immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        "*siiigh* What is happening in this city?\x02",
    )

    CloseMessageWindow()
    Jump("loc_3D9")

    label("loc_386")


    ChrTalk(    #2
        0xFE,
        (
            "If anything happens, we'll contact\x01",
            "the guild immediately.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        "Be careful.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_3D9")

    TalkEnd(0x8)

    label("loc_3DC")

    Return()

    # Function_3_2FD end

    def Function_4_3DD(): pass

    label("Function_4_3DD")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_F10")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 3)), scpexpr(EXPR_END)), "loc_557")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_46D")

    ChrTalk(    #4
        0xA,
        (
            "#602FLita's sleeping in the room across\x01",
            "the way.\x02\x03",

            "My wife is tending to her, so please\x01",
            "ask her for the details.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_554")

    label("loc_46D")


    ChrTalk(    #5
        0xA,
        (
            "#602FI've already informed Aina about the\x01",
            "situation.\x02\x03",

            "You can focus on the investigation\x01",
            "without concern, Estelle.\x02\x03",

            "Lita's sleeping in the room across\x01",
            "the way.\x02\x03",

            "My wife is tending to her, so please\x01",
            "ask her for the details.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_554")

    Jump("loc_F10")

    label("loc_557")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 1)), scpexpr(EXPR_END)), "loc_8A9")

    ChrTalk(    #6
        0xA,
        (
            "#604FOh, hello, everyone.\x02\x03",

            "#603FTo think something so grave would\x01",
            "occur here...\x02\x03",

            "Unfortunately, I've been left with no\x01",
            "choice but to cancel my trip to the\x01",
            "capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        "#1004FWha...?! You canceled it?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x103,
        (
            "#023FSo you won't be attending the signing\x01",
            "ceremony?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "#603FYes. It pains me to do this to\x01",
            "Her Majesty, but I simply can't go\x01",
            "under these circumstances.\x02\x03",

            "Attending such ceremonies is part\x01",
            "of my duty as a mayor, that much is\x01",
            "true.\x02\x03",

            "#602FBut no matter the reason, I just cannot\x01",
            "leave the city as it is.\x02\x03",

            "Even if it is by order of the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        "#1020FThat's upsetting...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #11
        0xA,
        (
            "#602FI've talked to Aina about the\x01",
            "investigation from my end.\x02\x03",

            "Estelle, you can begin immediately.\x02\x03",

            "Hopefully, that will help prevent any\x01",
            "further harm.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#1002FYeah! Got it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x103,
        "#022FYes, we'll do what we can.\x02",
    )

    CloseMessageWindow()
    Jump("loc_F0D")

    label("loc_8A9")


    ChrTalk(    #14
        0xA,
        (
            "#604FOh, hello, everyone.\x02\x03",

            "#603FTo think something so grave would\x01",
            "occur here...\x02\x03",

            "I made the right call when canceling\x01",
            "my trip to the capital.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x101,
        (
            "#1015FHuh? Did you have some business\x01",
            "at the capital?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x103,
        (
            "#023FTrip to the capital?\x02\x03",

            "Could that have been in regards to\x01",
            "the non-aggression pact signing\x01",
            "ceremony?\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(400)

    ChrTalk(    #17
        0x101,
        "#1004FWha...?! The signing ceremony?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xA,
        (
            "#602FYes, indeed.\x02\x03",

            "Yes. It pains me to do this to\x01",
            "Her Majesty, but I simply can't go\x01",
            "under these circumstances.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1020FN-Not attend?!\x02\x03",

            "Is it okay to just skip it?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #20
        0xA,
        (
            "#603FOf course, attending such ceremonies\x01",
            "is part of my duty as a mayor, but...\x02\x03",

            "But no matter the reason, I just cannot\x01",
            "leave the city as it is.\x02\x03",

            "#602FEven if it is by order of the queen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1026FThat's upsetting...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C3E")

    ChrTalk(    #22
        0x105,
        (
            "#047F...I believe you've made the right decision.\x02\x03",

            "#042FAnd I'm sure Her Highness the Queen will\x01",
            "understand.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C3E")


    ChrTalk(    #23
        0xA,
        (
            "#602FShould any further trouble occur, I intend to\x01",
            "cooperate with the guild to respond to it.\x02\x03",

            "My apologies, but I may need to enlist your\x01",
            "services for a while.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        "#1002FYeah, of course!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_D6D")

    ChrTalk(    #25
        0x106,
        (
            "#050FYou need us, we're there.\x02\x03",

            "Feels like we're at the right\x01",
            "place at the right time.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_D6D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_DC7")

    ChrTalk(    #26
        0x108,
        (
            "#072FWe'd be glad to help.\x02\x03",

            "Maybe it was fate that brought\x01",
            "us here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_DC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E30")

    ChrTalk(    #27
        0x104,
        (
            "#030FLeave everything to us.\x02\x03",

            "Surely, the hand of fate has drawn\x01",
            "us to this place.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_E53")

    label("loc_E30")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_E53")

    ChrTalk(    #28
        0x107,
        "#062FOf course!\x02",
    )

    CloseMessageWindow()

    label("loc_E53")


    ChrTalk(    #29
        0xA,
        "#603FThank you very much.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x103,
        (
            "#022FAll right, should anything happen,\x01",
            "please contact the guild.\x02\x03",

            "Aina should be able to respond effectively.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #31
        0xA,
        "#602FI'll do just that.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1881)

    label("loc_F0D")

    OP_A2(0x189B)

    label("loc_F10")

    TalkEnd(0xA)
    Return()

    # Function_4_3DD end

    def Function_5_F14(): pass

    label("Function_5_F14")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6F(0x5, 10)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrSubChip(0x9, 0)
    SetChrPos(0x9, 201800, 0, 49000, 270)
    ClearChrFlags(0x8, 0x80)
    SetChrPos(0x8, 200400, 0, 48360, 90)
    OP_4A(0x9, 255)
    OP_6D(200500, 0, 45550, 0)
    OP_67(0, 8000, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_6D(201840, 0, 49170, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0135   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_5_F14 end

    def Function_6_FF1(): pass

    label("Function_6_FF1")

    EventBegin(0x0)
    OP_4A(0x8, 255)
    Fade(1000)
    SetChrPos(0x101, 199890, 0, 46520, 0)
    SetChrPos(0x103, 200990, 0, 46580, 0)
    SetChrPos(0xF8, 199780, 0, 45200, 0)
    SetChrPos(0xF9, 200960, 0, 45200, 0)
    OP_6D(200720, 0, 47460, 0)
    OP_67(0, 6690, -10000, 0)
    OP_6B(2600, 0)
    OP_6C(45000, 0)
    OP_6E(288, 0)
    OP_8C(0x8, 180, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #32
        0xFE,
        "#6PEstelle, Scherazard. Welcome.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x101,
        (
            "#1002FHi, ma'am. Did Mayor Klaus tell\x01",
            "you about us?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "#6PYes. You're investigating the fainting cases.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        (
            "#6PIf there is anything I can do to help,\x01",
            "please, feel free to ask.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x103,
        (
            "#026F#4PThank you.\x02\x03",

            "#022FWell, firstly...how is Lita?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0xFE,
        (
            "#6PAh, Lita... She won't awaken, no matter\x01",
            "what we do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "#6PI pray she'll wake normally come the\x01",
            "sunrise, whatever that's worth in this\x01",
            "fog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0xFE,
        (
            "#6P...but for now, all I can do is keep an\x01",
            "eye on her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x101,
        "#1007FThat's awful...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x103,
        (
            "#022F#4PWhere, exactly, did Lita collapse?\x01",
            "And do you remember when?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "#6PLet me see... It would have been just\x01",
            "before 5:00.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xFE,
        (
            "#6PI stepped out of the kitchen and found\x01",
            "her collapsed in the entryway.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        (
            "#6PI panicked a little, needless to say,\x01",
            "and called for Klaus, who was able\x01",
            "to carry her to bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "#6PBut to think there are others afflicted\x01",
            "the same way!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015FShe collapsed in the entryway?\x02\x03",

            "Hang on, was the door locked\x01",
            "at the time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        "#6PI...don't believe it would have been.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "#6PAfter all, people have been visiting all\x01",
            "day to speak to my husband about how\x01",
            "to deal with this fog.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x101,
        (
            "#1007FWell, that's a list of suspects a selge\x01",
            "long, then.\x02\x03",

            "#1002FOh, how long were you in the kitchen,\x01",
            "by the way?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        "#6PHmmm... About thirty minutes, I suppose?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x103,
        (
            "#026F#4PAll right. I think we have a good\x01",
            "picture of what happened.\x02\x03",

            "#022FOne last thing, if I may...\x02\x03",

            "Was there anything...strange before\x01",
            "or after Lita collapsed?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "#6PStrange? What do you mean?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x103,
        (
            "#020F#4PDid the house have any unfamiliar visitors,\x01",
            "or were there any odd sounds?\x02\x03",

            "Anything you can think of, ma'am.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        "#6PLet me think...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0xFE,
        (
            "#6PWell, I'm not sure I'd call\x01",
            "it 'strange,' but it was memorable.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0xFE,
        (
            "#6PWhile I was in the kitchen, I heard the\x01",
            "faint sound of a bell.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1898")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't heard about bell elsewhere(haven't heard from Euridice and Freemont)\x01",      # 0
            "Set as have heard about bell elsewhere(haven't heard from Euridice and Freemont)\x01",         # 1
            "No change\x01",                                                                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_188C"),
        (1, "loc_1892"),
        (SWITCH_DEFAULT, "loc_1898"),
    )


    label("loc_188C")

    OP_A3(0x1815)
    Jump("loc_1898")

    label("loc_1892")

    OP_A2(0x1815)
    Jump("loc_1898")

    label("loc_1898")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_199F")

    ChrTalk(    #57
        0x103,
        "#023F#4PThe sound of a bell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x101,
        (
            "#1004FHold on a sec.\x01",
            "Didn't...we hear one too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "#6PIt was such a lovely sound.\x01",
            "I thought Lita rang it, perhaps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0xFE,
        (
            "#6PBut that reminds me, I haven't been able\x01",
            "to find that bell. I wonder where she put it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1A80")

    label("loc_199F")


    ChrTalk(    #61
        0x103,
        "#022F#4P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#1002FThe sound of a bell here, too...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xFE,
        (
            "#6PIt was such a lovely sound.\x01",
            "I thought Lita rang it, perhaps.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "#6PBut that reminds me, I haven't been able\x01",
            "to find that bell. I wonder where she put it.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1A80")


    ChrTalk(    #65
        0x103,
        (
            "#026F#4P...You've given us a lot to think about,\x01",
            "ma'am.\x02\x03",

            "#020FIf anything else happens, please contact\x01",
            "us at the guild at once.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "#6PYes, of course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "#6POh, and everyone...do be careful,\x01",
            "won't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1025FYeah, we will.\x02\x03",

            "Thanks for your help.\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x8, 90, 0)
    OP_4B(0x8, 255)
    OP_A2(0x1813)
    OP_28(0x90, 0x2, 0x2)
    OP_28(0x90, 0x1, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1BB9")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_1BB9")

    label("loc_1BB9")

    EventEnd(0x0)
    Return()

    # Function_6_FF1 end

    SaveToFile()

Try(main)
