from ED6ScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'T0401   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0401.x',
        MapIndex            = 13,
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
        'Monster',                              # 9
        'Monster',                              # 10
        'Monster',                              # 11
        'Monster',                              # 12
        'Monster',                              # 13
        'Monster',                              # 14
        'Monster',                              # 15
        'Tio',                                  # 16
        'Will',                                 # 17
        'Chere',                                # 18
        'Franz',                                # 19
        'Hannah',                               # 20
        'Estelle',                              # 21
        'Cow',                                  # 22
        'Cow',                                  # 23
        'Target Camera',                        # 24
        'Milch Main Road',                      # 25
    )

    DeclEntryPoint(
        Unknown_00              = 21000,
        Unknown_04              = 0,
        Unknown_08              = 24000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )

    DeclEntryPoint(
        Unknown_00              = 21000,
        Unknown_04              = 0,
        Unknown_08              = 24000,
        Unknown_0C              = 4,
        Unknown_0E              = 0,
        Unknown_10              = 0,
        Unknown_14              = 8000,
        Unknown_18              = -10000,
        Unknown_1C              = 0,
        Unknown_20              = 0,
        Unknown_24              = 0,
        Unknown_28              = 3000,
        Unknown_2C              = 262,
        Unknown_30              = 45,
        Unknown_32              = 0,
        Unknown_34              = 360,
        Unknown_36              = 0,
        Unknown_38              = 0,
        Unknown_3A              = 13,
        InitScenaIndex          = 0,
        InitFunctionIndex       = 0,
        EntryScenaIndex         = 0,
        EntryFunctionIndex      = 1,
    )


    AddCharChip(
        'ED6_DT09/CH10100 ._CH',             # 00
        'ED6_DT09/CH10101 ._CH',             # 01
        'ED6_DT07/CH02480 ._CH',             # 02
        'ED6_DT07/CH01060 ._CH',             # 03
        'ED6_DT07/CH01070 ._CH',             # 04
        'ED6_DT07/CH01020 ._CH',             # 05
        'ED6_DT07/CH01030 ._CH',             # 06
        'ED6_DT07/CH00100 ._CH',             # 07
        'ED6_DT07/CH01710 ._CH',             # 08
        'ED6_DT07/CH00107 ._CH',             # 09
        'ED6_DT07/CH00102 ._CH',             # 0A
    )

    AddCharChipPat(
        'ED6_DT09/CH10100P._CP',             # 00
        'ED6_DT09/CH10101P._CP',             # 01
        'ED6_DT07/CH02480P._CP',             # 02
        'ED6_DT07/CH01060P._CP',             # 03
        'ED6_DT07/CH01070P._CP',             # 04
        'ED6_DT07/CH01020P._CP',             # 05
        'ED6_DT07/CH01030P._CP',             # 06
        'ED6_DT07/CH00100P._CP',             # 07
        'ED6_DT07/CH01710P._CP',             # 08
        'ED6_DT07/CH00107P._CP',             # 09
        'ED6_DT07/CH00102P._CP',             # 0A
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 24300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1730,
        Z                   = 0,
        Y                   = 23000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x5,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -75800,
        Z                   = 0,
        Y                   = 2400,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x6,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x7,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 39010,
        Z                   = 600,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 40980,
        Z                   = 600,
        Y                   = 23300,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x105,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 23910,
        Z                   = 30,
        Y                   = 66820,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = 41200,
        Y                   = -500,
        Z                   = 21800,
        Range               = 48300,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x4FB0,
        Unknown_18          = 0x0,
        Unknown_1C          = 11,
    )

    DeclEvent(
        X                   = 34900,
        Y                   = -1000,
        Z                   = 33900,
        Range               = 43000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xAD70,
        Unknown_18          = 0x0,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = 38700,
        Y                   = -500,
        Z                   = 37000,
        Range               = 35200,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0xB4DC,
        Unknown_18          = 0x0,
        Unknown_1C          = 29,
    )

    DeclEvent(
        X                   = 26000,
        Y                   = -500,
        Z                   = 26000,
        Range               = 19000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x7148,
        Unknown_18          = 0x0,
        Unknown_1C          = 30,
    )

    DeclEvent(
        X                   = 42360,
        Y                   = -500,
        Z                   = 15300,
        Range               = 50900,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x490C,
        Unknown_18          = 0x0,
        Unknown_1C          = 31,
    )

    DeclEvent(
        X                   = 35830,
        Y                   = -1000,
        Z                   = 26140,
        Range               = 34270,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x5D2A,
        Unknown_18          = 0x0,
        Unknown_1C          = 13,
    )

    DeclEvent(
        X                   = 39000,
        Y                   = -500,
        Z                   = 42000,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 18,
    )

    DeclEvent(
        X                   = 22700,
        Y                   = -500,
        Z                   = 25300,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 19,
    )

    DeclEvent(
        X                   = 46100,
        Y                   = -500,
        Z                   = 15200,
        Range               = 1000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 20,
    )


    ScpFunction(
        "Function_0_486",          # 00, 0
        "Function_1_552",          # 01, 1
        "Function_2_58D",          # 02, 2
        "Function_3_5A3",          # 03, 3
        "Function_4_5DE",          # 04, 4
        "Function_5_5E4",          # 05, 5
        "Function_6_5EA",          # 06, 6
        "Function_7_61D",          # 07, 7
        "Function_8_62C",          # 08, 8
        "Function_9_643",          # 09, 9
        "Function_10_857",         # 0A, 10
        "Function_11_861",         # 0B, 11
        "Function_12_92E",         # 0C, 12
        "Function_13_C37",         # 0D, 13
        "Function_14_F16",         # 0E, 14
        "Function_15_1178",        # 0F, 15
        "Function_16_119B",        # 10, 16
        "Function_17_11A3",        # 11, 17
        "Function_18_11B8",        # 12, 18
        "Function_19_11CC",        # 13, 19
        "Function_20_11E0",        # 14, 20
        "Function_21_11F4",        # 15, 21
        "Function_22_225A",        # 16, 22
        "Function_23_229E",        # 17, 23
        "Function_24_230E",        # 18, 24
        "Function_25_2323",        # 19, 25
        "Function_26_2338",        # 1A, 26
        "Function_27_234D",        # 1B, 27
        "Function_28_238A",        # 1C, 28
        "Function_29_2392",        # 1D, 29
        "Function_30_2424",        # 1E, 30
        "Function_31_24A2",        # 1F, 31
        "Function_32_2534",        # 20, 32
        "Function_33_2A62",        # 21, 33
        "Function_34_2A6A",        # 22, 34
    )


    def Function_0_486(): pass

    label("Function_0_486")

    SetChrFlags(0x9, 0x40)
    SetChrFlags(0xA, 0x40)
    SetChrFlags(0xB, 0x40)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_4C7")
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    SetChrPos(0x9, 39000, 0, 42000, 270)
    OP_43(0x9, 0x3, 0x0, 0x2)

    label("loc_4C7")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (1, "loc_4DB"),
        (102, "loc_53A"),
        (103, "loc_53A"),
        (SWITCH_DEFAULT, "loc_551"),
    )


    label("loc_4DB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52A")
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    OP_6D(28000, 0, 41000, 0)
    OP_6C(200000, 0)
    OP_6B(5000, 0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x102, 0x80)
    FadeToBright(3000, 0)
    Event(0, 6)
    Jump("loc_537")

    label("loc_52A")

    FadeToBright(3000, 0)
    Event(0, 9)

    label("loc_537")

    Jump("loc_551")

    label("loc_53A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_54E")
    Event(0, 14)

    label("loc_54E")

    Jump("loc_551")

    label("loc_551")

    Return()

    # Function_0_486 end

    def Function_1_552(): pass

    label("Function_1_552")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x29), scpexpr(EXPR_PUSH_LONG, 0x393), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_570")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_570")

    OP_16(0x2, 0xFA0, 0xFFFE8518, 0xFFFE8900, 0x30004)
    OP_1B(0x4, 0x0, 0x22)
    OP_22(0x1CF, 0x0, 0x64)
    Return()

    # Function_1_552 end

    def Function_2_58D(): pass

    label("Function_2_58D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5A2")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_58D")

    label("loc_5A2")

    Return()

    # Function_2_58D end

    def Function_3_5A3(): pass

    label("Function_3_5A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5DD")
    OP_95(0xFE, 0xFFFFFC18, 0x0, 0x0, 0x258, 0x640)
    OP_95(0xFE, 0x3E8, 0x0, 0x0, 0x258, 0x640)
    Jump("Function_3_5A3")

    label("loc_5DD")

    Return()

    # Function_3_5A3 end

    def Function_4_5DE(): pass

    label("Function_4_5DE")

    OP_22(0x190, 0x0, 0x64)
    Return()

    # Function_4_5DE end

    def Function_5_5E4(): pass

    label("Function_5_5E4")

    OP_22(0x191, 0x0, 0x64)
    Return()

    # Function_5_5E4 end

    def Function_6_5EA(): pass

    label("Function_6_5EA")

    EventBegin(0x0)
    Sleep(500)
    OP_43(0x0, 0x2, 0x0, 0x8)
    OP_43(0x0, 0x1, 0x0, 0x7)
    OP_6C(225000, 9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    NewScene("ED6_DT01/T0411   ._SN", 1, 0, 0)
    IdleLoop()
    Return()

    # Function_6_5EA end

    def Function_7_61D(): pass

    label("Function_7_61D")

    Sleep(2000)
    OP_6B(3000, 9000)
    Return()

    # Function_7_61D end

    def Function_8_62C(): pass

    label("Function_8_62C")

    Sleep(2000)
    OP_6D(16700, 0, 18800, 9000)
    Return()

    # Function_8_62C end

    def Function_9_643(): pass

    label("Function_9_643")

    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    OP_6D(26700, 0, 14500, 0)
    OP_6C(225000, 0)
    OP_6B(3500, 0)
    SetChrPos(0x101, 28000, 0, 14200, 90)
    SetChrPos(0x102, 25350, 570, 15020, 90)
    EventBegin(0x0)
    OP_43(0x0, 0x1, 0x0, 0xA)
    OP_8E(0x102, 0x6E28, 0x0, 0x3C28, 0x5DC, 0x0)
    Sleep(1000)

    ChrTalk(    #0
        0x101,
        (
            "#004FWow! It's really dark out here\x01",
            "in the countryside.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x1, 400)

    ChrTalk(    #1
        0x101,
        (
            "#000FSo, Joshua, how do you think we\x01",
            "should go about making the rounds?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 400)

    ChrTalk(    #2
        0x102,
        (
            "#2P#010FLet's see...\x02\x03",

            "#010FHow about we start by checking around\x01",
            "the house first and then move on to the\x01",
            "fields, stable, and greenhouses.\x02\x03",

            "#010FWe should be able to cover the\x01",
            "entire farm by doing it this way.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#006FAll right.\x02\x03",

            "#001FLet's go!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    Return()

    # Function_9_643 end

    def Function_10_857(): pass

    label("Function_10_857")

    OP_6B(3000, 4500)
    Return()

    # Function_10_857 end

    def Function_11_861(): pass

    label("Function_11_861")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_92D")
    OP_A2(0x231)
    OP_28(0x2, 0x1, 0x10)
    EventBegin(0x0)
    OP_6D(48090, 480, 19550, 3000)
    Fade(1000)
    SetChrPos(0x101, 43760, 280, 21120, 135)
    SetChrPos(0x102, 42420, 370, 21480, 135)
    OP_6D(43760, 280, 21120, 0)
    OP_6C(315000, 0)
    Sleep(1000)
    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x101)

    ChrTalk(    #4
        0x101,
        "#000FNo monsters here...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        "#010FAll right, let's keep moving.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_92D")

    Return()

    # Function_11_861 end

    def Function_12_92E(): pass

    label("Function_12_92E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C36")
    OP_A2(0x233)
    OP_28(0x2, 0x1, 0x40)
    EventBegin(0x0)
    OP_6D(39020, -300, 38660, 2000)
    Fade(1000)
    SetChrPos(0x101, 42390, -40, 37580, 270)
    SetChrPos(0x102, 42500, 30, 38900, 270)
    OP_6D(40310, -300, 38250, 0)
    OP_6C(135000, 0)
    Sleep(1000)

    ChrTalk(    #6
        0x101,
        (
            "#000F#4PIt's awfully quiet...all I hear\x01",
            "are the bugs chirping.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x102,
        (
            "#010F#6PIt doesn't look as if they've\x01",
            "shown up yet.\x02\x03",

            "#010FI wonder if they're aware of\x01",
            "our presence.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #8
        0x101,
        (
            "#501F#4PHey, Joshua. Did anyone ever\x01",
            "tell you that story as a kid?\x02\x03",

            "#501FYou know, the one about babies\x01",
            "being born in a cabbage patch?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #9
        0x102,
        (
            "#017F#6PNow there's another question\x01",
            "entirely out of the blue...\x02\x03",

            "#010FAnd no, I was told about an angel\x01",
            "with silver wings who delivers them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x101,
        (
            "#501F#4PInteresting. So the explanation for\x01",
            "where babies come from differs\x01",
            "depending on the region, huh?\x02\x03",

            "#501F...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x102,
        (
            "#010F#6P...\x02\x03",

            "#010FHow about we get back to work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x101,
        "#000F#4POkay.\x02",
    )

    CloseMessageWindow()
    EventEnd(0x0)

    label("loc_C36")

    Return()

    # Function_12_92E end

    def Function_13_C37(): pass

    label("Function_13_C37")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 2)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_F15")
    OP_A2(0x233)
    OP_A2(0x234)
    OP_28(0x2, 0x1, 0x80)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x9, 24900, 50, 30180, 86)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x3, 0x0, 0x2)

    ChrTalk(    #13
        0x101,
        "#004F(Pssst, look!)\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(1000)
    SetChrPos(0x101, 35400, 350, 25540, 267)
    SetChrPos(0x102, 35360, 340, 24500, 261)

    def lambda_CCC():

        label("loc_CCC")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_CCC")

    QueueWorkItem2(0x101, 1, lambda_CCC)

    def lambda_CDD():

        label("loc_CDD")

        TurnDirection(0xFE, 0x9, 0)
        OP_48()
        Jump("loc_CDD")

    QueueWorkItem2(0x102, 1, lambda_CDD)
    OP_0D()

    def lambda_CEF():
        OP_6D(34540, 80, 30070, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_CEF)

    def lambda_D07():
        OP_6C(45000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_D07)

    def lambda_D17():
        OP_8E(0x9, 0x8656, 0x46, 0x758A, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_D17)
    WaitChrThread(0x9, 0x1)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 200)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(    #14
        0x9,
        "Miyaaaoowwn!\x02",
    )

    CloseMessageWindow()
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xAF64, 0x118, 0x9042, 0x2EE0, 0x0)
    SetChrPos(0x9, 39000, 0, 42000, 270)

    ChrTalk(    #15
        0x101,
        "#004FIt's getting away!\x02",
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_8E(0x101, 0x89C6, 0x140, 0x6EAA, 0x1388, 0x0)
    OP_8C(0x101, 45, 400)
    OP_44(0x101, 0xFF)

    ChrTalk(    #16
        0x101,
        "#005FHey! Get back here, you little furball!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x102, 0x8994, 0x136, 0x68CE, 0x7D0, 0x0)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #17
        0x102,
        (
            "#012FI can still sense its presence...\x02\x03",

            "#012FIt's staying put on the farm\x01",
            "for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#009FWell, good! \x02\x03",

            "#005FBecause it's about to get caught!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    Sleep(50)
    EventEnd(0x4)
    ClearMapFlags(0x400000)
    OP_43(0x9, 0x3, 0x0, 0x2)

    label("loc_F15")

    Return()

    # Function_13_C37 end

    def Function_14_F16(): pass

    label("Function_14_F16")

    OP_A2(0x233)
    OP_A2(0x234)
    OP_28(0x2, 0x1, 0x80)
    EventBegin(0x0)
    SetMapFlags(0x400000)
    ClearMapFlags(0x1)
    SetChrPos(0x9, 24100, 0, 54800, 0)
    ClearChrFlags(0x9, 0x8)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x3, 0x0, 0x2)
    OP_90(0x101, 0x3E8, 0x0, 0x0, 0x7D0, 0x0)
    TurnDirection(0x101, 0x9, 400)

    ChrTalk(    #19
        0x101,
        "#004F(Pssst, look!)\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_43(0x9, 0x1, 0x0, 0xF)
    OP_8E(0x9, 0x5BCC, 0x0, 0x9C40, 0xBB8, 0x0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    TurnDirection(0x9, 0x101, 200)
    Sleep(1000)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(    #20
        0x9,
        "Miyaaaoowwn!\x02",
    )

    CloseMessageWindow()
    OP_43(0x101, 0x1, 0x0, 0x10)
    OP_62(0x9, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0x7148, 0x0, 0x7148, 0x2EE0, 0x0)
    SetChrPos(0x9, 39000, 0, 42000, 270)

    ChrTalk(    #21
        0x101,
        "#004FIt's getting away!\x02",
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x55BE, 0x0, 0x98F8, 0x1388, 0x0)
    OP_8C(0x101, 135, 400)

    ChrTalk(    #22
        0x101,
        "#005FHey! Get back here, you little furball!\x02",
    )

    CloseMessageWindow()
    OP_44(0x102, 0xFF)
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #23
        0x102,
        (
            "#012FI can still sense its presence...\x02\x03",

            "#012FIt's staying put on the farm\x01",
            "for the moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x101,
        (
            "#009FWell, good! \x02\x03",

            "#005FBecause it's about to get caught!\x02",
        )
    )

    CloseMessageWindow()
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    OP_44(0x9, 0xFF)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    EventEnd(0x0)
    ClearMapFlags(0x400000)
    OP_43(0x9, 0x3, 0x0, 0x2)
    Return()

    # Function_14_F16 end

    def Function_15_1178(): pass

    label("Function_15_1178")

    OP_6D(24100, 0, 47800, 1000)
    OP_6D(23500, 0, 40000, 4000)
    Return()

    # Function_15_1178 end

    def Function_16_119B(): pass

    label("Function_16_119B")

    OP_69(0x101, 0x3E8)
    Return()

    # Function_16_119B end

    def Function_17_11A3(): pass

    label("Function_17_11A3")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_11B7")
    TurnDirection(0xFE, 0x9, 0)
    OP_48()
    Jump("Function_17_11A3")

    label("loc_11B7")

    Return()

    # Function_17_11A3 end

    def Function_18_11B8(): pass

    label("Function_18_11B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11CB")
    Call(0, 21)
    Call(0, 29)

    label("loc_11CB")

    Return()

    # Function_18_11B8 end

    def Function_19_11CC(): pass

    label("Function_19_11CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11DF")
    Call(0, 21)
    Call(0, 30)

    label("loc_11DF")

    Return()

    # Function_19_11CC end

    def Function_20_11E0(): pass

    label("Function_20_11E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_11F3")
    Call(0, 21)
    Call(0, 31)

    label("loc_11F3")

    Return()

    # Function_20_11E0 end

    def Function_21_11F4(): pass

    label("Function_21_11F4")

    EventBegin(0x0)
    ClearMapFlags(0x1)
    TurnDirection(0x0, 0x9, 0)
    TurnDirection(0x1, 0x9, 0)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_22(0x194, 0x0, 0x64)
    OP_44(0x9, 0xFF)
    OP_95(0x9, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0x9, 0x0, 400)

    ChrTalk(    #25
        0x101,
        (
            "#006FI got 'im!\x02\x03",

            "#006FI think it's time to teach this\x01",
            "critter a lesson!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#012FHere's where our job really starts,\x01",
            "so stay alert and don't let your\x01",
            "guard down!\x02",
        )
    )

    CloseMessageWindow()
    Battle(0x393, 0x0, 0x0, 0x2, 0xFF)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (1, "loc_1310"),
        (3, "loc_1315"),
        (0, "loc_1316"),
        (SWITCH_DEFAULT, "loc_2259"),
    )


    label("loc_1310")

    OP_B4(0x0)
    Jump("loc_2259")

    label("loc_1315")

    Return()

    label("loc_1316")

    EventBegin(0x0)
    FadeToBright(2000, 0)
    ClearChrFlags(0xA, 0x8)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x3, 0x0, 0x2)
    ClearChrFlags(0xB, 0x8)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x3, 0x0, 0x2)
    ClearChrFlags(0xC, 0x8)
    ClearChrFlags(0xC, 0x80)
    OP_43(0xC, 0x3, 0x0, 0x2)
    ClearChrFlags(0xD, 0x8)
    ClearChrFlags(0xD, 0x80)
    OP_43(0xD, 0x3, 0x0, 0x2)
    ClearChrFlags(0xE, 0x8)
    ClearChrFlags(0xE, 0x80)
    OP_43(0xE, 0x3, 0x0, 0x2)
    SetChrPos(0xC, 33150, 0, 16129, 225)
    SetChrPos(0xD, 33390, 0, 15210, 270)
    SetChrPos(0xE, 32990, 0, 14530, 315)
    SetChrPos(0x12, 29700, 0, 16600, 0)
    SetChrPos(0xF, 29000, 0, 14200, 0)
    SetChrPos(0x10, 28100, 0, 15300, 0)
    SetChrPos(0x13, 28300, 0, 16400, 0)
    SetChrPos(0x11, 29300, 0, 17100, 0)
    SetChrPos(0x101, 30920, 0, 15780, 270)
    SetChrPos(0x102, 30630, 0, 14650, 315)
    TurnDirection(0xF, 0xE, 0)
    TurnDirection(0x10, 0xD, 0)
    TurnDirection(0x11, 0xE, 0)
    TurnDirection(0x12, 0x101, 0)
    TurnDirection(0x13, 0x102, 0)
    OP_44(0x12, 0xFF)
    OP_44(0xF, 0xFF)
    OP_44(0x10, 0xFF)
    OP_44(0x13, 0xFF)
    OP_44(0x11, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    OP_43(0x11, 0x3, 0x0, 0x17)
    OP_6D(30470, 0, 16280, 0)
    OP_6C(315000, 0)
    OP_6B(3000, 0)
    OP_6B(2800, 3000)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(    #27
        0xC,
        "#2PMiyaaooow...\x02",
    )

    CloseMessageWindow()
    OP_43(0x10, 0x3, 0x0, 0x16)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(    #28
        0xE,
        "Miyuuuu...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x12,
        (
            "My goodness! The work of a\x01",
            "bracer is something else.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x12,
        (
            "You kids have done a fine job of\x01",
            "rounding up these critters!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x101,
        (
            "#000F#4PTee-hee, it was nothing, really.\x02\x03",

            "#000FI wanted to ask you though, now\x01",
            "that they've been caught, what\x01",
            "do you plan on doing with them?\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        10,
        0,
        (
            "[I don't think they'll cause any more trouble.]\x01",      # 0
            "[Do we really have to exterminate them...?]\x01",          # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1688"),
        (1, "loc_188C"),
        (SWITCH_DEFAULT, "loc_1A26"),
    )


    label("loc_1688")


    ChrTalk(    #32
        0x101,
        (
            "#000F#4PNow that we've given these critters\x01",
            "a good thrashing, I don't think\x01",
            "they'll cause any more trouble.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #33
        0x102,
        (
            "#012F#3PEstelle...how's that going to benefit\x01",
            "anyone if we show these creatures\x01",
            "any mercy now?\x02\x03",

            "#012FWe're here to do a job by exterminating\x01",
            "the monsters, remember?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #34
        0x101,
        "#003F#4PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        (
            "#015F#3PIn any case, we're here to\x01",
            "do a job in Dad's place.\x02\x03",

            "#015FIf the same thing happens again, what\x01",
            "will you have to say for yourself?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#007F#4PI see what you're getting at, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A26")

    label("loc_188C")


    ChrTalk(    #37
        0x101,
        (
            "#003F#4PDo we really have to exterminate\x01",
            "them...?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #38
        0x102,
        (
            "#012F#3POf course we do, Estelle.\x01",
            "That's the whole reason we came\x01",
            "up here in the first place.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #39
        0x101,
        "#003F#4PB-But...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        (
            "#015F#3PThe mission of a bracer is to protect\x01",
            "civilians and uphold justice...\x02\x03",

            "#015FShowing mercy to a bunch of\x01",
            "monsters is just absurd and\x01",
            "completely illogical.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x101,
        "#007F#4PI see what you're getting at, but...\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A26")

    label("loc_1A26")


    ChrTalk(    #42
        0xF,
        "...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xF,
        (
            "You know, it was only some vegetables\x01",
            "that were damaged so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0xF,
        (
            "What do you think about letting\x01",
            "it slide this time?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x13,
        "You know...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x13,
        (
            "After taking a beating like that,\x01",
            "I'm sure they've learned their\x01",
            "lesson.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10, 400)

    ChrTalk(    #47
        0x101,
        "#501F#4PTio, Mrs. Perzel...\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x13, 400)

    ChrTalk(    #48
        0x102,
        (
            "#012F#3PBut in this case,\x01",
            "I strongly suggest otherwise...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x12,
        (
            "I myself am against killing them,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x12,
        (
            "Whether it's us or them, the fact of\x01",
            "the matter is: we're all living beings\x01",
            "trying to survive on the same land.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x12,
        (
            "To some degree, I think we need to be\x01",
            "mindful of those creatures living around\x01",
            "us as we go about our daily lives.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "I know you may disagree with me,\x01",
            "Joshua...but would you mind sparing\x01",
            "these critters just this once?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x102,
        (
            "#015F#3P...\x02\x03",

            "#010FUnderstood...\x02\x03",

            "#010FSince this is coming from the ones\x01",
            "who suffered the actual loss, I won't\x01",
            "object to your request.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x12,
        (
            "I'm really sorry about this, Joshua.\x01",
            "I know I had you two come all the\x01",
            "way up here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x12,
        (
            "I'll make sure to reinforce the\x01",
            "fence and devise a way to prevent\x01",
            "this from happening again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x101,
        "#001F#4PThen that's that.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xD, 400)
    TurnDirection(0x102, 0xD, 400)

    ChrTalk(    #57
        0x101,
        (
            "#5P#006FAll right you critters, you'd better\x01",
            "count your blessings!\x02",
        )
    )

    CloseMessageWindow()
    OP_8E(0x101, 0x7AD0, 0x0, 0x3DA4, 0x7D0, 0x0)
    Sleep(100)
    SetChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 10)
    OP_22(0x1F4, 0x0, 0x64)
    OP_99(0x101, 0x0, 0xC, 0x7D0)
    OP_44(0x11, 0xFF)
    OP_44(0x10, 0xFF)

    ChrTalk(    #58
        0x101,
        (
            "#5P#005FIf we catch you around here again,\x01",
            "you won't be so lucky! Now scram!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xC, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xC, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xC, 0x101, 0)
    OP_62(0xD, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xD, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xD, 0x101, 0)
    OP_62(0xE, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    OP_95(0xE, 0x0, 0x0, 0x0, 0x320, 0x2EE0)
    TurnDirection(0xE, 0x101, 0)
    OP_22(0x194, 0x0, 0x64)

    ChrTalk(    #59
        0xC,
        "#2PMigyaaaw!!\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    OP_A2(0x3)
    SetChrPos(0xC, 0, 0, 0, 0)
    SetChrPos(0x9, 33150, 0, 16129, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0x9, 0x1, 0x0, 0x18)
    Sleep(200)
    OP_43(0xB, 0x2, 0x0, 0x1B)
    SetChrPos(0xD, 0, 0, 0, 0)
    SetChrPos(0xA, 33390, 0, 15210, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0xA, 0x1, 0x0, 0x19)
    Sleep(200)
    SetChrPos(0xE, 0, 0, 0, 0)
    SetChrPos(0xB, 32990, 0, 14530, 0)
    OP_22(0x81, 0x0, 0x64)
    OP_43(0xB, 0x1, 0x0, 0x1A)
    Sleep(1000)
    OP_A3(0x3)
    OP_44(0x9, 0xFF)
    OP_44(0xA, 0xFF)
    OP_44(0xB, 0xFF)
    OP_44(0xC, 0xFF)
    OP_44(0xD, 0xFF)
    OP_44(0xE, 0xFF)
    TurnDirection(0x101, 0xB, 0)
    Sleep(2000)
    TurnDirection(0x12, 0x101, 400)

    ChrTalk(    #60
        0x12,
        (
            "Well, I'll consider this matter closed.\x01",
            "Tonight's been a long night, so how about\x01",
            "we head back to the house and hit the sack.\x02",
        )
    )

    CloseMessageWindow()
    OP_43(0xF, 0x1, 0x0, 0x1C)
    OP_43(0x10, 0x1, 0x0, 0x1C)
    OP_43(0x11, 0x1, 0x0, 0x1C)
    OP_43(0x13, 0x1, 0x0, 0x1C)
    OP_44(0x101, 0xFF)
    OP_51(0x101, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x101, 0x800)
    SetChrChipByIndex(0x101, 65535)
    TurnDirection(0x101, 0x10, 400)
    TurnDirection(0x102, 0x12, 400)

    ChrTalk(    #61
        0x12,
        (
            "The two of you are more than\x01",
            "welcome to spend the night.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        "#001F#4PSounds good to me.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x102,
        "#010F#3PI appreciate your hospitality.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_221E")
    OP_2B(0x2, 0x2)
    Jump("loc_222B")

    label("loc_221E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_222B")
    OP_2B(0x2, 0x1)

    label("loc_222B")

    OP_A2(0x239)
    OP_28(0x2, 0x1, 0x800)
    OP_28(0x2, 0x1, 0x1000)
    OP_28(0x2, 0x4, 0x10)
    OP_20(0x5DC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_21()
    NewScene("ED6_DT01/T0411   ._SN", 1, 0, 0)
    IdleLoop()

    label("loc_2259")

    Return()

    # Function_21_11F4 end

    def Function_22_225A(): pass

    label("Function_22_225A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_229D")
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(300)
    OP_95(0xFE, 0x0, 0x0, 0x0, 0x190, 0xBB8)
    Sleep(2500)
    Jump("Function_22_225A")

    label("loc_229D")

    Return()

    # Function_22_225A end

    def Function_23_229E(): pass

    label("Function_23_229E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_230D")
    Sleep(3000)
    OP_8F(0xFE, 0x733C, 0x0, 0x4394, 0x12C, 0x0)
    Sleep(2000)
    OP_8F(0xFE, 0x7274, 0x0, 0x42CC, 0x5DC, 0x0)
    Sleep(3000)
    OP_8F(0xFE, 0x72D8, 0x0, 0x4330, 0x12C, 0x0)
    Sleep(500)
    OP_8F(0xFE, 0x7274, 0x0, 0x42CC, 0x2BC, 0x0)
    Jump("Function_23_229E")

    label("loc_230D")

    Return()

    # Function_23_229E end

    def Function_24_230E(): pass

    label("Function_24_230E")

    OP_8E(0x9, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_24_230E end

    def Function_25_2323(): pass

    label("Function_25_2323")

    OP_8E(0xA, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_25_2323 end

    def Function_26_2338(): pass

    label("Function_26_2338")

    OP_8E(0xB, 0x85AC, 0x32, 0x740E, 0x2EE0, 0x0)
    Return()

    # Function_26_2338 end

    def Function_27_234D(): pass

    label("Function_27_234D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_END)), "loc_2389")
    TurnDirection(0xF, 0xA, 0)
    TurnDirection(0x10, 0xA, 0)
    TurnDirection(0x11, 0xA, 0)
    TurnDirection(0x12, 0xA, 0)
    TurnDirection(0x13, 0xA, 0)
    TurnDirection(0x101, 0xA, 0)
    TurnDirection(0x102, 0xA, 0)
    OP_48()
    Jump("Function_27_234D")

    label("loc_2389")

    Return()

    # Function_27_234D end

    def Function_28_238A(): pass

    label("Function_28_238A")

    TurnDirection(0xFE, 0x101, 400)
    Return()

    # Function_28_238A end

    def Function_29_2392(): pass

    label("Function_29_2392")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2423")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A3(0x0)
    OP_A2(0x1)
    OP_A3(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xB1BC, 0x0, 0xB220, 0x2EE0, 0x0)
    OP_8E(0x9, 0xBB80, 0x0, 0xC738, 0x2EE0, 0x0)
    SetChrPos(0x9, 22700, 0, 25300, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Call(0, 32)

    label("loc_2423")

    Return()

    # Function_29_2392 end

    def Function_30_2424(): pass

    label("Function_30_2424")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_24A1")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A3(0x0)
    OP_A3(0x1)
    OP_A2(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0x846C, 0x0, 0x3A98, 0x2EE0, 0x0)
    SetChrPos(0x9, 46100, 0, 15200, 0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    Call(0, 32)

    label("loc_24A1")

    Return()

    # Function_30_2424 end

    def Function_31_24A2(): pass

    label("Function_31_24A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2533")
    EventBegin(0x0)
    ClearMapFlags(0x1)
    OP_A2(0x0)
    OP_A3(0x1)
    OP_A3(0x2)
    OP_62(0x9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_69(0x9, 0x1F4)
    OP_43(0x101, 0x1, 0x0, 0x11)
    OP_43(0x102, 0x1, 0x0, 0x11)
    OP_22(0x81, 0x0, 0x64)
    OP_8E(0x9, 0xA4D8, 0x0, 0x2A94, 0x2EE0, 0x0)
    OP_8E(0x9, 0x927C, 0x0, 0x27D8, 0x2EE0, 0x0)
    OP_44(0x101, 0xFF)
    OP_44(0x102, 0xFF)
    SetChrPos(0x9, 39000, 0, 42000, 270)
    Call(0, 32)

    label("loc_2533")

    Return()

    # Function_31_24A2 end

    def Function_32_2534(): pass

    label("Function_32_2534")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25E0")

    ChrTalk(    #64
        0x101,
        "#000FAaaah! It got away!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x102,
        (
            "#010FThese little ones look like they\x01",
            "have a tendency to run.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x102,
        (
            "#010FLet's think about this from a\x01",
            "battle perspective.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_25E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 6)), scpexpr(EXPR_END)), "loc_26AC")
    OP_A2(0x237)
    OP_28(0x2, 0x1, 0x400)

    ChrTalk(    #67
        0x101,
        "#007FAaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x102,
        (
            "#012FYou're still a little off.\x02\x03",

            "#012FRemember, you need to move in on it from\x01",
            "behind as it's scampering away and then\x01",
            "make a grab at it when you're close enough.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_26AC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 5)), scpexpr(EXPR_END)), "loc_2991")
    OP_A2(0x236)
    OP_28(0x2, 0x1, 0x200)

    ChrTalk(    #69
        0x101,
        (
            "#009FN-Not again! \x02\x03",

            "#009FFor being such a ball of chub,\x01",
            "what's up with those speedy feet?!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x1, 0x0, 0)

    ChrTalk(    #70
        0x102,
        (
            "#012FWhile I admit that creature's a nimble one,\x01",
            "I get the feeling that its instincts are\x01",
            "much sharper than how fast it can run.\x02\x03",

            "#012FEven so, it has an opening\x01",
            "we can take advantage of.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x0, 0x1, 500)
    ClearMapFlags(0x1)
    OP_51(0x17, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x17, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x102, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_SUB), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_69(0x17, 0x320)

    ChrTalk(    #71
        0x101,
        "#004FAn opening?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x102,
        (
            "#012FIt appears to have a habit of letting\x01",
            "down its guard whenever it\x01",
            "scampers off.\x02\x03",

            "#012FIf we can catch it off guard and\x01",
            "sneak up on it from behind, we\x01",
            "may get lucky enough to bag it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x101,
        (
            "#006FNot a bad idea. So we close in\x01",
            "on it from behind as it's running\x01",
            "away, right?\x02\x03",

            "#006FLet's give it a shot!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2A4C")

    label("loc_2991")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_2A4C")
    OP_A2(0x235)
    OP_28(0x2, 0x1, 0x100)

    ChrTalk(    #74
        0x101,
        "#004FAaaah!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x102,
        (
            "#012FThat's too bad. I guess it noticed\x01",
            "us trying to sneak up on it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#009FI swear I'm going to catch that little\x01",
            "bugger the next time I see it!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2A4C")

    OP_44(0x0, 0xFF)
    OP_44(0x1, 0xFF)
    OP_44(0x9, 0xFF)
    EventEnd(0x1)
    OP_43(0x9, 0x3, 0x0, 0x2)
    Return()

    # Function_32_2534 end

    def Function_33_2A62(): pass

    label("Function_33_2A62")

    OP_69(0x101, 0x3E8)
    Return()

    # Function_33_2A62 end

    def Function_34_2A6A(): pass

    label("Function_34_2A6A")

    EventBegin(0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46, 4)), scpexpr(EXPR_END)), "loc_2B58")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE9")

    ChrTalk(    #77
        0x102,
        (
            "#012FThe monsters are still somewhere\x01",
            "here on the farm.\x02\x03",

            "We need to get back and\x01",
            "search for them.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2B55")

    label("loc_2AE9")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #78
        0x102,
        (
            "#012FThe monsters are still around\x01",
            "the farm somewhere.\x02\x03",

            "We'd better get back and\x01",
            "look for them.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B55")

    Jump("loc_2C08")

    label("loc_2B58")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BB6")

    ChrTalk(    #79
        0x102,
        (
            "#012FThis is the wrong way...we need to\x01",
            "be making our rounds on the farm.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C08")

    label("loc_2BB6")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #80
        0x102,
        (
            "#012FThat leads off the farm. We need\x01",
            "to make our rounds on the farm.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C08")

    OP_8E(0x0, 0x5E24, 0x14, 0xD1C4, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    Return()

    # Function_34_2A6A end

    SaveToFile()

Try(main)
