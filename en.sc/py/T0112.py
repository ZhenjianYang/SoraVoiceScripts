from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0112   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0112.x',
        MapIndex            = 11,
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
        'Luke',                                 # 9
        'Maggy',                                # 10
        'Pat',                                  # 11
        'Rhett',                                # 12
        'Serra',                                # 13
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
        'ED6_DT26/CH20330 ._CH',             # 00
        'ED6_DT07/CH01110 ._CH',             # 01
        'ED6_DT07/CH01060 ._CH',             # 02
        'ED6_DT07/CH01120 ._CH',             # 03
        'ED6_DT07/CH01130 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH01110P._CP',             # 01
        'ED6_DT07/CH01060P._CP',             # 02
        'ED6_DT07/CH01120P._CP',             # 03
        'ED6_DT07/CH01130P._CP',             # 04
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 93320,
        Z                   = 0,
        Y                   = 162900,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 88100,
        Z                   = 0,
        Y                   = 162410,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )


    ScpFunction(
        "Function_0_172",          # 00, 0
        "Function_1_1EB",          # 01, 1
        "Function_2_1FA",          # 02, 2
        "Function_3_377",          # 03, 3
        "Function_4_4EB",          # 04, 4
        "Function_5_54F",          # 05, 5
        "Function_6_730",          # 06, 6
        "Function_7_907",          # 07, 7
        "Function_8_A04",          # 08, 8
    )


    def Function_0_172(): pass

    label("Function_0_172")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1D3")
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 55200, 100, 159950, 180)
    SetChrPos(0x9, 55120, 0, 161430, 180)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0x8, 4)

    label("loc_1D3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1EA")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 7)

    label("loc_1EA")

    Return()

    # Function_0_172 end

    def Function_1_1EB(): pass

    label("Function_1_1EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1F9")
    OP_6F(0x2, 15)

    label("loc_1F9")

    Return()

    # Function_1_1EB end

    def Function_2_1FA(): pass

    label("Function_2_1FA")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_361")

    label("loc_21F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_361")

    label("loc_238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_361")

    label("loc_251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_361")

    label("loc_26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_361")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_361")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B5")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_361")

    label("loc_2B5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CE")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_361")

    label("loc_2CE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_361")

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_300")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_361")

    label("loc_300")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_319")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_361")

    label("loc_319")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_332")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_361")

    label("loc_332")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34B")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_361")

    label("loc_34B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_361")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_361")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_376")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_361")

    label("loc_376")

    Return()

    # Function_2_1FA end

    def Function_3_377(): pass

    label("Function_3_377")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_386")
    Call(0, 8)
    Jump("loc_4EA")

    label("loc_386")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_414")

    ChrTalk(    #0
        0xFE,
        (
            "Well, Luke is a little ruffian.\x01",
            "I swear, that boy never runs\x01",
            "out of energy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "I'm sure he'll be up and about\x01",
            "by morning.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_4E7")

    label("loc_414")


    ChrTalk(    #2
        0xFE,
        (
            "Well, Luke is a little ruffian.\x01",
            "I swear, that boy never runs\x01",
            "out of energy!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "I'm sure he'll be up and about\x01",
            "by morning.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xFE,
        (
            "I'm sure he'll be running out\x01",
            "without even finishing breakfast\x01",
            "as always.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_4E7")

    TalkEnd(0x9)

    label("loc_4EA")

    Return()

    # Function_3_377 end

    def Function_4_4EB(): pass

    label("Function_4_4EB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4FA")
    Call(0, 8)
    Jump("loc_54E")

    label("loc_4FA")

    TalkBegin(0xA)

    ChrTalk(    #5
        0xA,
        (
            "Estelle! I'm not gonna cry\x01",
            "anymore!\x02\x03",

            "I can't show Luke any tears,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0xA)

    label("loc_54E")

    Return()

    # Function_4_4EB end

    def Function_5_54F(): pass

    label("Function_5_54F")

    TalkBegin(0xB)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_72C")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_5F5")

    ChrTalk(    #6
        0xFE,
        "Luke fell into a deep slumber.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "Pat went off to check on him\x01",
            "a little bit ago.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "I'm worried about Pat...\x01",
            "He's my only son, you know?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_72C")

    label("loc_5F5")


    ChrTalk(    #9
        0xFE,
        "Luke fell into a deep slumber.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "And stimulants aren't having\x01",
            "any effect on him. It's worrying...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "He's such a close friend of Pat's,\x01",
            "so I understand why he feels the\x01",
            "need to stay by his side, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0xFE,
        (
            "Pat's my only son, you know?\x01",
            "I don't know what I'd do if the same\x01",
            "thing happened to him...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_72C")

    TalkEnd(0xB)
    Return()

    # Function_5_54F end

    def Function_6_730(): pass

    label("Function_6_730")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_903")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_END)), "loc_7E4")

    ChrTalk(    #13
        0xFE,
        (
            "Pat doesn't want to leave\x01",
            "Luke's side for even a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        (
            "I don't want to tear him away from\x01",
            "his friend, so I asked Maggy to take\x01",
            "care of him for now.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_903")

    label("loc_7E4")


    ChrTalk(    #15
        0xFE,
        "Pat went to Ashton's for today.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "He doesn't want to leave Luke's\x01",
            "side for even a moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "I don't want to tear him away from\x01",
            "his friend, so I asked Maggy to take\x01",
            "care of him for now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0xFE,
        (
            "I know how he feels. It can't hurt\x01",
            "to let him stay out a little longer\x01",
            "than usual.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2)

    label("loc_903")

    TalkEnd(0xC)
    Return()

    # Function_6_730 end

    def Function_7_907(): pass

    label("Function_7_907")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x2, 15)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrFlags(0x8, 0x40)
    SetChrFlags(0x8, 0x4)
    SetChrPos(0x8, 55200, 100, 159950, 180)
    SetChrPos(0x9, 55120, 0, 161430, 180)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    ClearChrFlags(0x9, 0x80)
    ClearChrFlags(0xA, 0x80)
    SetChrSubChip(0x8, 4)
    OP_6D(52310, 0, 164340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(54780, 0, 161440, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0113   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_7_907 end

    def Function_8_A04(): pass

    label("Function_8_A04")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    OP_4A(0xA, 255)
    Fade(1000)
    SetChrPos(0x101, 56220, 0, 162560, 180)
    SetChrPos(0x103, 55060, 0, 162840, 180)
    SetChrPos(0xF8, 55900, 0, 164050, 180)
    SetChrPos(0xF9, 54700, 0, 164240, 180)
    OP_8C(0x9, 0, 0)
    OP_8C(0xA, 0, 0)
    OP_6D(55170, 0, 162450, 0)
    OP_67(0, 5530, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Sleep(200)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B5D")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as not met up with Luke and Pat again\x01",      # 0
            "Set as met up with Luke and Pat again\x01",          # 1
            "No change\x01",                                      # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_B51"),
        (1, "loc_B57"),
        (SWITCH_DEFAULT, "loc_B5D"),
    )


    label("loc_B51")

    OP_A3(0x1883)
    Jump("loc_B5D")

    label("loc_B57")

    OP_A2(0x1883)
    Jump("loc_B5D")

    label("loc_B5D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C3B")

    ChrTalk(    #19
        0xA,
        "Ah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x9,
        "#3POh, dearie me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x9,
        (
            "#3PEstelle Bright!\x01",
            "Look at you, a senior bracer and everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#1025F#4PUm, hey, Miss Maggy. Pat.\x01",
            "Sorry I didn't say hi earlier, Pat.\x02\x03",

            "#1003FWe, um...heard about Luke.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_CE9")

    label("loc_C3B")


    ChrTalk(    #23
        0xA,
        "Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x9,
        "#3POh, dearie me!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x9,
        (
            "#3PEstelle Bright! Look at you, a senior bracer\x01",
            "and everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x101,
        (
            "#1025F#4PUm, good evening.\x02\x03",

            "#1003FWe, um...heard about Luke.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_CE9")


    ChrTalk(    #27
        0xA,
        (
            "Umm, Es... Estelle...\x02\x03",

            "ESTEEEEELLE! WAAAAAAAH!\x02",
        )
    )

    CloseMessageWindow()
    OP_D2(0x260110, 0x260115, 0x5)
    SetChrFlags(0xA, 0x40)
    OP_8F(0xA, 0xDBCE, 0x0, 0x27A38, 0xFA0, 0x0)
    SetChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 5)
    SetChrSubChip(0x101, 0)
    SetChrFlags(0xA, 0x80)
    OP_91(0x101, 0x0, 0x0, 0xC8, 0xFA0, 0x0)

    def lambda_D6E():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_D6E)
    Sleep(50)

    def lambda_D81():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_D81)
    Sleep(50)

    def lambda_D94():
        TurnDirection(0xFE, 0xA, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_D94)
    Sleep(400)

    ChrTalk(    #28
        0x101,
        "#1004F#4PWhoa, hey, Pat! It is that bad...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x9,
        "#3PWell, you see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x9,
        (
            "#3POur little Pat is the one who found Luke\x01",
            "after he collapsed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#1003F#4POh, no...\x02\x03",

            "#1025FPat...don't worry.\x01",
            "It'll... It'll be okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0xA,
        "#6PWaaaah-haaaaah...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x103, 180, 400)
    Sleep(500)

    ChrTalk(    #33
        0x103,
        (
            "#022FMaggy. How is your grandson?\x01",
            "Is he hurt?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x9,
        (
            "#3PWhat? No, no, not at all!\x01",
            "He's just sound asleep.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x9,
        (
            "#3PReally, I think this is all a bit of a fuss.\x01",
            "He'll be right as rain tomorrow, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x9,
        (
            "#3PThe little rascal just wore himself out,\x01",
            "like boys do, you know.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x9,
        (
            "#3PReally... Him not waking up?\x01",
            "Foolish! Foolish...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x103,
        "#522FMaggy...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x101,
        (
            "#1010F#4P...\x02\x03",

            "#1002FHey, Pat?\x02\x03",

            "Can you tell us what happened when\x01",
            "Luke fell asleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xA,
        "#6PHuh? *sniffle*\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x103, 0xA, 400)

    ChrTalk(    #41
        0x101,
        (
            "#1002F#4PWe're investigating what happened on\x01",
            "behalf of the mayor... On behalf of the town.\x02\x03",

            "Pat, if there's ANYTHING you can tell us,\x01",
            "it might help us solve this and wake\x01",
            "Luke up.\x02\x03",

            "Please, Pat.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xA,
        (
            "#6PEstelle...\x02\x03",

            "Okay... I'll *sniffle* tell you...\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0x101, 0x2)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x101, 0)
    ClearChrFlags(0xA, 0x80)
    OP_0D()
    OP_8F(0xA, 0xDB6A, 0x0, 0x278D0, 0x3E8, 0x0)
    ClearChrFlags(0xA, 0x40)

    def lambda_11B1():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x103, 1, lambda_11B1)
    Sleep(50)

    def lambda_11C4():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_11C4)
    Sleep(50)

    def lambda_11D7():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_11D7)
    Sleep(400)

    ChrTalk(    #43
        0x101,
        (
            "#1025F#4PThanks, Pat.\x02\x03",

            "#1002FSo. Where and when did Luke\x01",
            "fall asleep?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xA,
        (
            "#6PUm...\x02\x03",

            "I wasn't there when he fell asleep, but\x01",
            "I found him on top of the clock tower.\x02\x03",

            "I think it was just past 5:00.\x02\x03",

            "We were playing hide and seek in the fog.\x02\x03",

            "I was it, and I was looking for Luke.\x02\x03",

            "And when I found him, he was asleep!\x02\x03",

            "I thought he was just being a jerk and\x01",
            "tried to wake him up, but, but, he wouldn't...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x101,
        (
            "#1007F#4PI see...\x02\x03",

            "#1015FEr, wait, one thing I don't see.\x01",
            "Who the heck carried Luke down\x01",
            "from the clock tower?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0xA,
        (
            "#6POh, that was Mr. Paddington.\x02\x03",

            "He came up and found us just when\x01",
            "I was trying to figure out what to do.\x02\x03",

            "He said he came up to make sure the\x01",
            "clock was working and the fog wasn't\x01",
            "causing any problems.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x101,
        (
            "#1011F#4POh. Yeah, that's just like Mr. Paddington.\x02\x03",

            "#1006FOkay, think I've got the gist of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x103,
        (
            "#020FPat, I was wondering.\x02\x03",

            "When you were playing, did anything\x01",
            "strange happen?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x103, 400)

    ChrTalk(    #49
        0xA,
        "#6PStrange?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x103,
        (
            "#020FDid you see anyone you didn't recognize?\x01",
            "Hear any strange sounds?\x02\x03",

            "Like Estelle said, anything could help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0xA,
        (
            "#6PUmmmm...\x02\x03",

            "I don't remember much except all the\x01",
            "white of the fog...\x02\x03",

            "I do remember thinking it was really creepy\x01",
            "not seeing anyone at the landing port.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x103,
        "#524FI see. Hmm.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x101,
        (
            "#1015F#4PSo, creepy fog aside, nothing really\x01",
            "suspicious happened.\x01",
            "Nuts.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x103,
        (
            "#026FSeems that way.\x02\x03",

            "#020FThank you, both of you.\x01",
            "You've given us some food for thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x9,
        "#3PI'm glad we could be of help, dearie.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xA, 0x101, 400)
    Sleep(500)

    ChrTalk(    #56
        0xA,
        (
            "#6PEstelle, Estelle!\x01",
            "Is Luke gonna be okay?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006F#4PYeah... You bet he will!\x02\x03",

            "Pat, don't cry anymore, okay?\x02\x03",

            "Luke'll tease you if he finds out\x01",
            "when he wakes up, you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0xA,
        (
            "#6PO-Okay... *sniffle*\x02\x03",

            "Yeah. I won't cry anymore!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(53810, 0, 164450, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 53810, 0, 164450, 0)
    SetChrPos(0x103, 53810, 0, 164450, 0)
    SetChrPos(0xF8, 53810, 0, 164450, 0)
    SetChrPos(0xF9, 53810, 0, 164450, 0)
    SetChrPos(0xA, 56170, 0, 161420, 180)
    OP_8C(0x9, 180, 0)
    OP_4B(0x9, 255)
    OP_4B(0xA, 255)
    OP_A2(0x1816)
    OP_28(0x90, 0x2, 0x20)
    OP_28(0x90, 0x1, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1967")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_1967")

    label("loc_1967")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_8_A04 end

    SaveToFile()

Try(main)
