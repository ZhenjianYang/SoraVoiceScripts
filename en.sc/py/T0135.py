from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0135   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0135.x',
        MapIndex            = 7,
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        'Tabitha',                              # 9
        'Elissa',                               # 10
        'Densel',                               # 11
        'Faulkner',                             # 12
        'Miner Trent',                          # 13
        'Miner Bones',                          # 14
        'Captain Petrov',                       # 15
        'Crew Mem. Nora',                       # 16
        'Paddington',                           # 17
        'Zosimov',                              # 18
        'Anton',                                # 19
        'Ricky',                                # 20
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
        'ED6_DT07/CH02490 ._CH',             # 01
        'ED6_DT07/CH01280 ._CH',             # 02
        'ED6_DT07/CH01270 ._CH',             # 03
        'ED6_DT26/CH20312 ._CH',             # 04
        'ED6_DT07/CH01503 ._CH',             # 05
        'ED6_DT07/CH01500 ._CH',             # 06
        'ED6_DT07/CH01443 ._CH',             # 07
        'ED6_DT07/CH01540 ._CH',             # 08
        'ED6_DT07/CH01250 ._CH',             # 09
        'ED6_DT07/CH01450 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01140 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT26/CH20330P._CP',             # 00
        'ED6_DT07/CH02490P._CP',             # 01
        'ED6_DT07/CH01280P._CP',             # 02
        'ED6_DT07/CH01270P._CP',             # 03
        'ED6_DT26/CH20312P._CP',             # 04
        'ED6_DT07/CH01503P._CP',             # 05
        'ED6_DT07/CH01500P._CP',             # 06
        'ED6_DT07/CH01443P._CP',             # 07
        'ED6_DT07/CH01540P._CP',             # 08
        'ED6_DT07/CH01250P._CP',             # 09
        'ED6_DT07/CH01450P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01140P._CP',             # 0C
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
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 36450,
        Z                   = 0,
        Y                   = 126300,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = 34500,
        Z                   = 0,
        Y                   = 75200,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 39320,
        Z                   = 220,
        Y                   = 70940,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 5,
        ChipIndex           = 0x5,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 36640,
        Z                   = 0,
        Y                   = 72650,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 39470,
        Z                   = 1620,
        Y                   = 77070,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x155,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 41000,
        Z                   = 1500,
        Y                   = 79500,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = 37050,
        Z                   = 0,
        Y                   = 75490,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 41530,
        Z                   = 0,
        Y                   = 67550,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 12,
    )

    DeclNpc(
        X                   = 44910,
        Z                   = 0,
        Y                   = 71790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x111,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 13,
    )

    DeclNpc(
        X                   = 43750,
        Z                   = 0,
        Y                   = 73360,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 14,
    )


    DeclActor(
        TriggerX            = 35580,
        TriggerZ            = 0,
        TriggerY            = 74990,
        TriggerRange        = 800,
        ActorX              = 34500,
        ActorZ              = 1500,
        ActorY              = 75200,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_2B6",          # 00, 0
        "Function_1_32F",          # 01, 1
        "Function_2_33E",          # 02, 2
        "Function_3_4BB",          # 03, 3
        "Function_4_4C0",          # 04, 4
        "Function_5_83C",          # 05, 5
        "Function_6_B1B",          # 06, 6
        "Function_7_B8D",          # 07, 7
        "Function_8_D04",          # 08, 8
        "Function_9_EB6",          # 09, 9
        "Function_10_135E",        # 0A, 10
        "Function_11_13EC",        # 0B, 11
        "Function_12_18E5",        # 0C, 12
        "Function_13_19F9",        # 0D, 13
        "Function_14_1BBE",        # 0E, 14
        "Function_15_1D79",        # 0F, 15
        "Function_16_1E5B",        # 10, 16
    )


    def Function_0_2B6(): pass

    label("Function_0_2B6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_2D0")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F0)
    Event(0, 15)
    Jump("loc_32E")

    label("loc_2D0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_311")
    OP_4A(0x8, 255)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)
    SetChrPos(0x8, 88620, 0, 79000, 270)
    SetChrPos(0x9, 87090, 0, 79170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)

    label("loc_311")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_321")
    SetChrFlags(0x11, 0x80)

    label("loc_321")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32E")
    SetChrFlags(0x10, 0x10)

    label("loc_32E")

    Return()

    # Function_0_2B6 end

    def Function_1_32F(): pass

    label("Function_1_32F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_33D")
    OP_6F(0x0, 10)

    label("loc_33D")

    Return()

    # Function_1_32F end

    def Function_2_33E(): pass

    label("Function_2_33E")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_363")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_4A5")

    label("loc_363")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_4A5")

    label("loc_37C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_395")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_4A5")

    label("loc_395")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AE")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_3AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3C7")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_4A5")

    label("loc_3C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E0")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_4A5")

    label("loc_3E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3F9")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_4A5")

    label("loc_3F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_412")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_4A5")

    label("loc_412")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42B")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_4A5")

    label("loc_42B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_444")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_4A5")

    label("loc_444")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_45D")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_4A5")

    label("loc_45D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_476")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_4A5")

    label("loc_476")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_48F")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_4A5")

    label("loc_48F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_4A5")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_4BA")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_4A5")

    label("loc_4BA")

    Return()

    # Function_2_33E end

    def Function_3_4BB(): pass

    label("Function_3_4BB")

    Call(0, 4)
    Return()

    # Function_3_4BB end

    def Function_4_4C0(): pass

    label("Function_4_4C0")

    TalkBegin(0xB)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",                               # 0
            "Shop\x01",                               # 1
            "[Three-Eyed Soup] - 1600 mira\x01",      # 2
            "Leave\x01",                              # 3
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_53E")
    FadeToBright(300, 0)
    OP_0D()
    OP_A9(0x4)
    OP_56(0x0)
    TalkEnd(0xB)
    Return()

    label("loc_53E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_652")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x12), scpexpr(EXPR_PUSH_LONG, 0x640), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_618")
    SubMira(1600)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)
    OP_22(0xB, 0x0, 0x64)

    AnonymousTalk(    #0
        "\x06Ate #2CThree-Eyed Soup#0C.\x02",
    )

    CloseMessageWindow()
    OP_31(0x0, 0xFD, 0x7D0)
    OP_31(0x1, 0xFD, 0x7D0)
    OP_31(0x2, 0xFD, 0x7D0)
    OP_31(0x3, 0xFD, 0x7D0)
    OP_31(0x4, 0xFD, 0x7D0)
    OP_31(0x5, 0xFD, 0x7D0)
    OP_31(0x6, 0xFD, 0x7D0)
    OP_31(0x7, 0xFD, 0x7D0)
    OP_31(0x8, 0xFD, 0x7D0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_60A")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x6)"), scpexpr(EXPR_END)), "loc_5D9")
    Jump("loc_60A")

    label("loc_5D9")

    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #1
        "\x06Learned [#2CThree-Eyed Soup#0C] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_60A")

    OP_56(0x0)
    FadeToBright(1000, 0)
    Jump("loc_640")

    label("loc_618")

    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #2
        "Insufficient mira.\x02",
    )

    CloseMessageWindow()
    FadeToBright(300, 0)

    label("loc_640")

    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xB)
    Return()

    label("loc_652")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66C")
    FadeToBright(300, 0)
    TalkEnd(0xB)
    Return()

    label("loc_66C")

    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_838")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_725")

    ChrTalk(    #3
        0xB,
        (
            "Even though his wife's under that\x01",
            "strange sleep, the owner's still hard\x01",
            "at work, like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0xB,
        (
            "But, it sure feels like he's lacking\x01",
            "his usual energy.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_838")

    label("loc_725")


    ChrTalk(    #5
        0xB,
        (
            "Even though his wife's under that\x01",
            "strange sleep, the owner's still hard\x01",
            "at work, like always.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xB,
        (
            "But, it sure feels like he's lacking\x01",
            "his usual energy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xB,
        (
            "Elissa went off to tend to her mother\x01",
            "and hasn't come back yet...\x01",
            "I've got to hang in there the best I can.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_838")

    TalkEnd(0xB)
    Return()

    # Function_4_4C0 end

    def Function_5_83C(): pass

    label("Function_5_83C")

    TalkBegin(0xA)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_B17")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 4)), scpexpr(EXPR_END)), "loc_8F9")

    ChrTalk(    #8
        0xFE,
        (
            "I can't close the bar on a terrible night\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "Everyone's coming here to relieve\x01",
            "some of the stress.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0xFE,
        (
            "Sorry, but please take care of Tabitha\x01",
            "for me.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_B17")

    label("loc_8F9")

    OP_62(0xFE, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    TurnDirection(0xFE, 0x101, 0)
    Sleep(400)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x312, 3)), scpexpr(EXPR_END)), "loc_93A")

    ChrTalk(    #11
        0xFE,
        "Hey there, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_966")

    label("loc_93A")


    ChrTalk(    #12
        0xFE,
        "Hey there, you two. It's been a while.\x02",
    )

    CloseMessageWindow()

    label("loc_966")


    ChrTalk(    #13
        0x101,
        "#1003FDensel...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0xFE,
        "Sorry, but take care of Tabitha for me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xFE,
        (
            "I thought about closing up the bar\x01",
            "tonight, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0xFE,
        (
            "Everyone's gonna want some liquor\x01",
            "on a night like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xFE,
        (
            "As owner of the only bar in the city,\x01",
            "I can't shut my doors during a time\x01",
            "like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1010FI see...\x02\x03",

            "#1002FYeah... I get it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x103,
        (
            "#020FIf we get a hold of anything,\x01",
            "we'll let you know.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #20
        0xFE,
        "Yeah, thanks.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0xFE,
        "I'm counting on you.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1894)

    label("loc_B17")

    TalkEnd(0xA)
    Return()

    # Function_5_83C end

    def Function_6_B1B(): pass

    label("Function_6_B1B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_B2A")
    Call(0, 16)
    Jump("loc_B8C")

    label("loc_B2A")

    TalkBegin(0x9)

    ChrTalk(    #22
        0x9,
        "Estelle, I'm counting on you.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x9,
        (
            "I'm okay now, so good luck\x01",
            "with your investigation.\x02",
        )
    )

    CloseMessageWindow()
    TalkEnd(0x9)

    label("loc_B8C")

    Return()

    # Function_6_B1B end

    def Function_7_B8D(): pass

    label("Function_7_B8D")

    TalkBegin(0xC)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_D00")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_C1D")

    ChrTalk(    #24
        0xFE,
        (
            "I've never seen anything like this\x01",
            "fog before in my life.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xFE,
        (
            "If it's not sunny tomorrow,\x01",
            "I don't want to go to work.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_D00")

    label("loc_C1D")


    ChrTalk(    #26
        0xFE,
        (
            "*chomp chomp chomp*\x01",
            "Stho abhouth thodahy's fhog...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xFE,
        (
            "*munch munch munch*\x01",
            "Ih've nehvhuh seeh ahythih hike it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0xFE,
        (
            "*chew chew chew*\x01",
            "Ih hit's noh suhhy tomohho...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xFE,
        (
            "*guuuuuuuulp* *smack*\x01",
            "I don't wanna go to work...\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1)

    label("loc_D00")

    TalkEnd(0xC)
    Return()

    # Function_7_B8D end

    def Function_8_D04(): pass

    label("Function_8_D04")

    TalkBegin(0xD)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_EB2")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_D97")

    ChrTalk(    #30
        0xFE,
        (
            "I don't really think he needs to eat so\x01",
            "much that he's gotta skip out on work.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0xFE,
        "Wish he'd use that energy on the job!\x02",
    )

    CloseMessageWindow()
    Jump("loc_EB2")

    label("loc_D97")


    ChrTalk(    #32
        0xFE,
        "Trent was super late today, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0xFE,
        (
            "He said he got lost in the fog, but I'm\x01",
            "sure he was just out stuffing his face.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0xFE,
        "That guy is such a glutton...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0xFE,
        "He's even skipped out on work to eat!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0xFE,
        (
            "If he'd use that energy at work, he'd\x01",
            "be ten times better than he is now.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)

    label("loc_EB2")

    TalkEnd(0xD)
    Return()

    # Function_8_D04 end

    def Function_9_EB6(): pass

    label("Function_9_EB6")

    TalkBegin(0xE)
    ClearChrFlags(0xFE, 0x10)
    TurnDirection(0xFE, 0x0, 0)
    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_EDB")
    SetChrSubChip(0xFE, 2)
    Jump("loc_EF6")

    label("loc_EDB")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x4), scpexpr(EXPR_PUSH_LONG, 0x10E), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_EF1")
    SetChrSubChip(0xFE, 2)
    Jump("loc_EF6")

    label("loc_EF1")

    SetChrSubChip(0xFE, 1)

    label("loc_EF6")

    OP_8C(0xFE, 90, 0)
    SetChrFlags(0xFE, 0x10)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x100)"), scpexpr(EXPR_END)), "loc_1073")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_FA4")

    ChrTalk(    #37
        0xFE,
        (
            "I feel sorry for the passengers, but\x01",
            "there's not much we can do about\x01",
            "bad weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0xFE,
        (
            "The best we can do is pray the fog\x01",
            "clears soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1070")

    label("loc_FA4")


    ChrTalk(    #39
        0xFE,
        "Hey, if it isn't the bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0xFE,
        "The crew's all stuck here in Rolent, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0xFE,
        (
            "Looks like we're all in this together\x01",
            "until the weather clears up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0xFE,
        (
            "Nothing we can do except beg the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1070")

    Jump("loc_1355")

    label("loc_1073")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x40)"), scpexpr(EXPR_END)), "loc_1147")

    ChrTalk(    #43
        0xFE,
        "Looking for Zosimov this time?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xFE,
        "He went back to the landing port.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xFE,
        (
            "He's a weird one, that guy. Heard he ate\x01",
            "some potluck he found in a treasure chest\x01",
            "once and never was the same again.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1355")

    label("loc_1147")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x74, 0x1, 0x10)"), scpexpr(EXPR_END)), "loc_11F2")

    ChrTalk(    #46
        0xFE,
        "Looking for Quint?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xFE,
        (
            "He finished his dinner a while ago\x01",
            "and took off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0xFE,
        (
            "I doubt he went back to the ship.\x01",
            "He's probably out killing time in town.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1355")

    label("loc_11F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 4)), scpexpr(EXPR_END)), "loc_1289")

    ChrTalk(    #49
        0xFE,
        (
            "I feel sorry for the passengers, but\x01",
            "there's not much we can do about\x01",
            "bad weather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0xFE,
        (
            "The best we can do is pray the fog\x01",
            "clears soon.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1355")

    label("loc_1289")


    ChrTalk(    #51
        0xFE,
        "Hey, if it isn't the bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0xFE,
        "The crew's all stuck here in Rolent, too.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0xFE,
        (
            "Looks like we're all in this together\x01",
            "until the weather clears up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0xFE,
        (
            "Nothing we can do except beg the\x01",
            "Goddess.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x4)

    label("loc_1355")

    SetChrSubChip(0xFE, 0)
    TalkEnd(0xE)
    Return()

    # Function_9_EB6 end

    def Function_10_135E(): pass

    label("Function_10_135E")

    TalkBegin(0xF)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_13E8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 5)), scpexpr(EXPR_END)), "loc_139C")

    ChrTalk(    #55
        0xFE,
        "*sigh* I wonder when we'll take off.\x02",
    )

    CloseMessageWindow()
    Jump("loc_13E8")

    label("loc_139C")


    ChrTalk(    #56
        0xFE,
        "*sigh* I wonder when we'll take off.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0xFE,
        "I'm so sick of waiting...\x02",
    )

    CloseMessageWindow()
    OP_A2(0x5)

    label("loc_13E8")

    TalkEnd(0xF)
    Return()

    # Function_10_135E end

    def Function_11_13EC(): pass

    label("Function_11_13EC")

    TalkBegin(0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_18E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_END)), "loc_18A8")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x313, 0)), scpexpr(EXPR_END)), "loc_148E")

    ChrTalk(    #58
        0xFE,
        (
            "If I'd been at the clock tower,\x01",
            "I wouldn't have let the kid up...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0xFE,
        (
            "How could I have been away\x01",
            "when I needed to be there most?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_18A5")

    label("loc_148E")

    ClearChrFlags(0xFE, 0x10)

    ChrTalk(    #60
        0xFE,
        "Is Luke doing okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xFE,
        "I hope it's not serious...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1002FHe seems okay for now.\x02\x03",

            "He hasn't opened his eyes yet,\x01",
            "but it seems like he's just sleeping.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xFE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_63(0xFE)
    TurnDirection(0xFE, 0x101, 400)
    Sleep(400)

    ChrTalk(    #63
        0xFE,
        "Hello there, young lady.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0xFE,
        (
            "You went to check in on Luke,\x01",
            "didn't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x101,
        (
            "#1000FYeah, as part of a guild investigation.\x02\x03",

            "I heard you were the one who carried\x01",
            "him home, Mr. Paddington.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0xFE,
        "Yep, I did.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xFE,
        (
            "I found him unconscious at\x01",
            "the top of the clock tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x103,
        (
            "#020FWas there anything out of the\x01",
            "ordinary at the time?\x02\x03",

            "We'd appreciate it if you could\x01",
            "tell us even minor details.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x103, 400)

    ChrTalk(    #69
        0xFE,
        "I wish I could help you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0xFE,
        (
            "But, my mind was full of what\x01",
            "to do with Luke at the time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xFE,
        "I don't remember much else.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        "#1015FI see... Well, can't say I blame you.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #73
        0xFE,
        "I'm sorry I couldn't be more helpful.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x103,
        (
            "#020FNo, it's enough to have confirmed\x01",
            "that there was nothing particularly\x01",
            "noticeable.\x02\x03",

            "Thank you for your cooperation.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x101,
        "#1016FDon't drink too much, okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0xFE,
        "Yes, yes.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0xFE,
        "You all take care, too.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1898)

    label("loc_18A5")

    Jump("loc_18E1")

    label("loc_18A8")


    ChrTalk(    #78
        0xFE,
        "Is Luke doing okay?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0xFE,
        "I hope it's not serious...\x02",
    )

    CloseMessageWindow()

    label("loc_18E1")

    TalkEnd(0x10)
    Return()

    # Function_11_13EC end

    def Function_12_18E5(): pass

    label("Function_12_18E5")

    TalkBegin(0x11)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_19F5")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 6)), scpexpr(EXPR_END)), "loc_1950")

    ChrTalk(    #80
        0xFE,
        "Ahhh... That was goooood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0xFE,
        (
            "Now that my stomach's full,\x01",
            "it's time to get back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_19F5")

    label("loc_1950")


    ChrTalk(    #82
        0xFE,
        "Ahhh... That was goooood!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0xFE,
        (
            "Been a while since I had a proper\x01",
            "dinner like this. Mmmmm, yes-siree.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0xFE,
        (
            "Now that my stomach's full,\x01",
            "it's time to get back.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x6)

    label("loc_19F5")

    TalkEnd(0x11)
    Return()

    # Function_12_18E5 end

    def Function_13_19F9(): pass

    label("Function_13_19F9")

    OP_EA(0x1, 0x8, 0x0, 0x0)
    TalkBegin(0x12)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1BBA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 7)), scpexpr(EXPR_END)), "loc_1A9A")

    ChrTalk(    #85
        0xFE,
        (
            "I'll have to learn as much as I can\x01",
            "about that lady starting tomorrow.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0xFE,
        (
            "Gotta do proper research first if you\x01",
            "wanna get close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BBA")

    label("loc_1A9A")


    ChrTalk(    #87
        0xFE,
        (
            "That blond-haired lady's been on\x01",
            "my mind ever since I laid eyes upon\x01",
            "her...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #88
        0xFE,
        (
            "To think such a wonderful woman\x01",
            "even existed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0xFE,
        (
            "A chance meeting in a little village...\x01",
            "My serendipitous arrival...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0xFE,
        (
            "The Goddess may very well be directing\x01",
            "me to true love. Sweet Aidios...!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x7)

    label("loc_1BBA")

    TalkEnd(0x12)
    Return()

    # Function_13_19F9 end

    def Function_14_1BBE(): pass

    label("Function_14_1BBE")

    TalkBegin(0x13)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 2)), scpexpr(EXPR_END)), "loc_1D75")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 0)), scpexpr(EXPR_END)), "loc_1C46")

    ChrTalk(    #91
        0xFE,
        (
            "My buddy's fallen in love at first\x01",
            "sight. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0xFE,
        (
            "Well, it's nothing new, so not like\x01",
            "I'll worry about it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D75")

    label("loc_1C46")


    ChrTalk(    #93
        0xFE,
        (
            "My buddy's fallen in love at first\x01",
            "sight. Again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0xFE,
        (
            "Every time he opens his mouth he starts\x01",
            "talkin' about that woman. 'Blond goddess'\x01",
            "this, 'heavenly mandate' that...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0xFE,
        (
            "Well, it's nothing new, so not like\x01",
            "I'll worry about it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0xFE,
        (
            "Quick to flame, quick to cool.\x01",
            "That's Anton in a nutshell.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x8)

    label("loc_1D75")

    TalkEnd(0x13)
    Return()

    # Function_14_1BBE end

    def Function_15_1D79(): pass

    label("Function_15_1D79")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_4A(0x8, 255)
    OP_6F(0x0, 10)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x8, 0x2)
    SetChrSubChip(0x8, 2)
    SetChrPos(0x8, 88620, 0, 79000, 270)
    SetChrPos(0x9, 87090, 0, 79170, 90)
    ClearChrFlags(0x8, 0x80)
    ClearChrFlags(0x9, 0x80)
    OP_6D(82660, 0, 80340, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    FadeToBright(1000, 0)
    OP_6D(86990, 0, 80450, 3000)
    OP_0D()
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearChrFlags(0x0, 0x80)
    ClearChrFlags(0x1, 0x80)
    ClearChrFlags(0x2, 0x80)
    ClearChrFlags(0x3, 0x80)
    OP_DC()
    OP_A2(0x10F0)
    NewScene("ED6_DT21/T0112   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_15_1D79 end

    def Function_16_1E5B(): pass

    label("Function_16_1E5B")

    EventBegin(0x0)
    OP_4A(0x9, 255)
    Fade(1000)
    SetChrPos(0x101, 86750, 0, 80570, 180)
    SetChrPos(0x103, 87440, 0, 80930, 180)
    SetChrPos(0xF8, 85880, 0, 80850, 135)
    SetChrPos(0xF9, 85060, 0, 80750, 135)
    OP_8C(0x9, 0, 0)
    OP_6D(86420, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x200, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1F90")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set as haven't met Elissa again yet\x01",      # 0
            "Set as met Elissa again\x01",                  # 1
            "No change\x01",                                # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1F84"),
        (1, "loc_1F8A"),
        (SWITCH_DEFAULT, "loc_1F90"),
    )


    label("loc_1F84")

    OP_A3(0x1882)
    Jump("loc_1F90")

    label("loc_1F8A")

    OP_A2(0x1882)
    Jump("loc_1F90")

    label("loc_1F90")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x310, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E3")

    ChrTalk(    #97
        0xFE,
        "#6P*gasp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        "#7P#1008FUm... Hey, Elissa. Sorry I--\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0xFE,
        "#6PEsteeeeelle! Yes! Hi, hi!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0xFE,
        (
            "#6PThis is GREAT!\x01",
            "When did you get back from training?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0xFE,
        (
            "#6PI've been so worried!\x01",
            "You didn't come back for so long!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x101,
        (
            "#7P#1016FHaha, um, sorry.\x01",
            "I got kind of busy and couldn't say hi.\x02\x03",

            "#1015FSo...is your mom doing all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_213D")

    label("loc_20E3")


    ChrTalk(    #103
        0xFE,
        "#6PHi, Estelle! And...Scherazard?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #104
        0x101,
        (
            "#7P#1025FHi, Elissa.\x02\x03",

            "Umm, how's your mother?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_213D")


    ChrTalk(    #105
        0xFE,
        "#6PWell, it seems like she's sleeping okay.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0xFE,
        (
            "#6PBut I'm so worried! She won't, like, wake\x01",
            "up or do anything, even if you shake her!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #107
        0xFE,
        (
            "#6PFather Divine said there's nothing to\x01",
            "worry about, but...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#7P#1003FI see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x103,
        (
            "#020F#4PWe're investigating this at the request\x01",
            "of the mayor.\x02\x03",

            "Could we ask you a few questions?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0xFE,
        "#6POh, yeah, sure, sure!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0xFE,
        "#6PAsk me anything you want!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x101,
        (
            "#7P#1015FOkay, then.\x02\x03",

            "#1002FFirst, where'd your mother fall asleep?\x01",
            "And when?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0xFE,
        "#6PUm, lesse. It was about 5:00! I think.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0xFE,
        (
            "#6PMom and I went out to clean the chairs\x01",
            "and stuff on the terrace.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x103,
        "#023F#4PThe chairs?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0xFE,
        (
            "#6PYeah! We figured they might get damaged\x01",
            "from all the humidity in the air due to\x01",
            "this creepy fog, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #117
        0xFE,
        (
            "#6PWe'd finished weatherproofing the ground\x01",
            "floor, you see, so we figured we'd totally\x01",
            "store the chairs too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #118
        0x103,
        "#026F#4PI see... All right. And then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #119
        0xFE,
        (
            "#6POkay, so, while we were cleaning up,\x01",
            "Dad called me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "#6PWhen I got back, Mom was all zonked out\x01",
            "in one of the chairs!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0x101,
        "#7P#1002FSo you didn't see her fall asleep, then.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        "#6PYeah, sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0xFE,
        (
            "#6PSo I tried talking to her, shaking her...\x01",
            "but she wouldn't wake up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "#6PI totally freaked out and called Dad,\x01",
            "and he carried her up to her bed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0xFE,
        "#6PAnd then...she...she wouldn't...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0xFE,
        "#6PMom...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x101,
        "#7P#1025FElissa...\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x9, 0x40)
    OP_8F(0x101, 0x15414, 0x0, 0x13718, 0x3E8, 0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 4)
    SetChrSubChip(0x9, 0)
    Sleep(500)
    OP_99(0x9, 0x1, 0x2, 0x3E8)
    Sleep(1000)

    ChrTalk(    #128
        0xFE,
        "#6PAhaha, sorry!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #129
        0xFE,
        (
            "#6PI'm sort of losing it 'cause you're home too,\x01",
            "Estelle!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x101,
        (
            "#1012F#7PYeah... I know.\x02\x03",

            "It's okay, you don't need to worry.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0xFE,
        "#6PYeah...\x02",
    )

    CloseMessageWindow()
    OP_99(0x9, 0x2, 0x0, 0x3E8)
    Sleep(500)
    ClearChrFlags(0x101, 0x80)
    ClearChrFlags(0x9, 0x2)
    SetChrChipByIndex(0x9, 1)
    SetChrSubChip(0x9, 0)
    OP_8F(0x101, 0x153D8, 0x0, 0x1386C, 0x3E8, 0x0)
    Sleep(500)

    ChrTalk(    #132
        0xFE,
        "#6PI'm okay now, thanks!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0xFE,
        "#6PDid you wanna ask anything else?\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x40)

    ChrTalk(    #134
        0x101,
        (
            "#1007F#7PUh, one second.\x02\x03",

            "#1015FSchera, you got anything?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x103,
        (
            "#026F#4PPossibly.\x02\x03",

            "#022FElissa, did anything strange happen before\x01",
            "or after your mother went to sleep?\x02\x03",

            "Did you see anyone you didn't recognize,\x01",
            "or hear anything strange?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0xFE,
        "#6PPeople I didn't recognize...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #137
        0xFE,
        "#6PActually, yeah! Just as I was heading inside!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "#6PI saw this lady come out of the clock tower.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x103,
        (
            "#023F#4PA woman? Was it someone from Rolent,\x01",
            "you think?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0xFE,
        (
            "#6PUm, well, I couldn't see her face.\x01",
            "The fog made it kinda hard to see details.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0xFE,
        (
            "#6PBut her clothes were reeeeeally weird!\x01",
            "I figured she had to be a traveler of some\x01",
            "sort, y'know?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        "#1004F#7PReally weird? What was weird about them?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0xFE,
        (
            "#6PUmmm, she was wearing this sort of\x01",
            "black...dress...robe...thing?\x01",
            "I can't lie, it was kinda hot!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #144
        0xFE,
        (
            "#6PIt was a bit hard to see details through\x01",
            "the fog, though, like I said.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #145
        0x101,
        (
            "#1006F#7PI see. Still, this is REALLY valuable!\x02\x03",

            "We need to go tell Aina this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x103,
        (
            "#026F#4PYes, absolutely.\x02\x03",

            "#020FThank you, Elissa.\x01",
            "You've helped us tremendously.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #147
        0xFE,
        (
            "#6PNo, no, it's okay!\x01",
            "Good luck with your investigating...stuff!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #148
        0x101,
        (
            "#1006F#7PAnd don't worry, okay?\x01",
            "You can count on us to save your mom.\x02\x03",

            "We'll figure this out and wake her up!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #149
        0xFE,
        "#6PI know. Thanks, Estelle!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(82980, 0, 80630, 0)
    OP_67(0, 6150, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(315000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 82980, 0, 80630, 270)
    SetChrPos(0x103, 82980, 0, 80630, 270)
    SetChrPos(0xF8, 82980, 0, 80630, 270)
    SetChrPos(0xF9, 82980, 0, 80630, 270)
    OP_8C(0x9, 90, 0)
    OP_4B(0x9, 255)
    OP_43(0x9, 0x0, 0x0, 0x2)
    OP_A2(0x1814)
    OP_28(0x90, 0x2, 0x8)
    OP_28(0x90, 0x1, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 3)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x302, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2D9A")
    OP_28(0x90, 0x1, 0x200)
    Jump("loc_2D9A")

    label("loc_2D9A")

    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_16_1E5B end

    SaveToFile()

Try(main)
