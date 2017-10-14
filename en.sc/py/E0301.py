from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0301   ._SN',
        MapName             = 'Event',
        Location            = 'E0301.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60116",
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
        'Tita',                                 # 9
        'Kloe',                                 # 10
        'Agate',                                # 11
        'Scherazard',                           # 12
        'Zin',                                  # 13
        'Kevin',                                # 14
        'Professor Russell',                    # 15
        'Captain Schwarz',                      # 16
        'Nial',                                 # 17
        'Dorothy',                              # 18
        'Clive',                                # 19
        'Antoine',                              # 20
        'Lift',                                 # 21
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
        'ED6_DT07/CH00060 ._CH',             # 00
        'ED6_DT07/CH00040 ._CH',             # 01
        'ED6_DT07/CH00050 ._CH',             # 02
        'ED6_DT07/CH00020 ._CH',             # 03
        'ED6_DT07/CH00070 ._CH',             # 04
        'ED6_DT27/CH03080 ._CH',             # 05
        'ED6_DT07/CH02020 ._CH',             # 06
        'ED6_DT27/CH03580 ._CH',             # 07
        'ED6_DT07/CH02060 ._CH',             # 08
        'ED6_DT06/CH20063 ._CH',             # 09
        'ED6_DT06/CH20064 ._CH',             # 0A
        'ED6_DT07/CH01450 ._CH',             # 0B
        'ED6_DT07/CH01700 ._CH',             # 0C
    )

    AddCharChipPat(
        'ED6_DT07/CH00060P._CP',             # 00
        'ED6_DT07/CH00040P._CP',             # 01
        'ED6_DT07/CH00050P._CP',             # 02
        'ED6_DT07/CH00020P._CP',             # 03
        'ED6_DT07/CH00070P._CP',             # 04
        'ED6_DT27/CH03080P._CP',             # 05
        'ED6_DT07/CH02020P._CP',             # 06
        'ED6_DT27/CH03580P._CP',             # 07
        'ED6_DT07/CH02060P._CP',             # 08
        'ED6_DT06/CH20063P._CP',             # 09
        'ED6_DT06/CH20064P._CP',             # 0A
        'ED6_DT07/CH01450P._CP',             # 0B
        'ED6_DT07/CH01700P._CP',             # 0C
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
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 9,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 8,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 6,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 5,
        ChipIndex           = 0x5,
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
        Unknown3            = 6,
        ChipIndex           = 0x6,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1540,
        Z                   = 3000,
        Y                   = 17550,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 4,
    )

    DeclNpc(
        X                   = -20,
        Z                   = 2500,
        Y                   = 15640,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -2430,
        Z                   = 2500,
        Y                   = 12850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 10,
    )

    DeclNpc(
        X                   = -1830,
        Z                   = 1500,
        Y                   = -7470,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 3,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 11,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    ScpFunction(
        "Function_0_2B2",          # 00, 0
        "Function_1_458",          # 01, 1
        "Function_2_519",          # 02, 2
        "Function_3_74E",          # 03, 3
        "Function_4_772",          # 04, 4
        "Function_5_13FE",         # 05, 5
        "Function_6_1842",         # 06, 6
        "Function_7_24AE",         # 07, 7
        "Function_8_2B42",         # 08, 8
        "Function_9_3033",         # 09, 9
        "Function_10_34D7",        # 0A, 10
        "Function_11_365F",        # 0B, 11
        "Function_12_3A45",        # 0C, 12
        "Function_13_3C13",        # 0D, 13
        "Function_14_3C34",        # 0E, 14
        "Function_15_3C47",        # 0F, 15
        "Function_16_3C5A",        # 10, 16
        "Function_17_3C6D",        # 11, 17
        "Function_18_4120",        # 12, 18
        "Function_19_4197",        # 13, 19
        "Function_20_41C7",        # 14, 20
        "Function_21_41F7",        # 15, 21
        "Function_22_4227",        # 16, 22
        "Function_23_425E",        # 17, 23
        "Function_24_428E",        # 18, 24
        "Function_25_42C5",        # 19, 25
        "Function_26_42F5",        # 1A, 26
        "Function_27_4325",        # 1B, 27
        "Function_28_4355",        # 1C, 28
        "Function_29_451A",        # 1D, 29
    )


    def Function_0_2B2(): pass

    label("Function_0_2B2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2E6")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_2E3")
    SetChrPos(0xA, -60, 3000, 19860, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_2E3")

    Jump("loc_3D6")

    label("loc_2E6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_2FA")
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    Jump("loc_3D6")

    label("loc_2FA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_32E")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_32B")
    SetChrPos(0x8, 3490, 1500, -6210, 90)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)

    label("loc_32B")

    Jump("loc_3D6")

    label("loc_32E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_399")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_35F")
    SetChrPos(0xB, -1920, 1500, -9370, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_35F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_396")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_379")
    SetChrFlags(0x9, 0x10)

    label("loc_379")

    SetChrPos(0x9, 2300, 2500, 14260, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)

    label("loc_396")

    Jump("loc_3D6")

    label("loc_399")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_3D6")
    ClearChrFlags(0x10, 0x80)
    ClearChrFlags(0x11, 0x80)
    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 0)
    SetChrPos(0xB, 3490, 1500, -6210, 90)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_3D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_3EC")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(0, 13)
    Jump("loc_457")

    label("loc_3EC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_402")
    OP_A3(0x10F1)
    SetMapFlags(0x10000000)
    Event(0, 14)
    Jump("loc_457")

    label("loc_402")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_418")
    OP_A3(0x10F2)
    SetMapFlags(0x10000000)
    Event(0, 15)
    Jump("loc_457")

    label("loc_418")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_42E")
    OP_A3(0x10F3)
    SetMapFlags(0x10000000)
    Event(0, 16)
    Jump("loc_457")

    label("loc_42E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_444")
    OP_A3(0x10F4)
    SetMapFlags(0x10000000)
    Event(0, 17)
    Jump("loc_457")

    label("loc_444")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_457")
    OP_A3(0x10F5)
    SetMapFlags(0x10000000)
    Event(0, 29)

    label("loc_457")

    Return()

    # Function_0_2B2 end

    def Function_1_458(): pass

    label("Function_1_458")

    OP_22(0x1C3, 0x0, 0x64)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_471")
    OP_22(0x75, 0x1, 0x5A)
    Jump("loc_482")

    label("loc_471")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_482")
    OP_22(0x125, 0x1, 0x50)

    label("loc_482")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_49C")
    SetMapFlags(0x2000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_49C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 4)), scpexpr(EXPR_END)), "loc_4AF")
    OP_B1("E0301_1")
    Jump("loc_518")

    label("loc_4AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_4C2")
    OP_B1("E0301_3")
    Jump("loc_518")

    label("loc_4C2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_4D5")
    OP_B1("E0301_4")
    Jump("loc_518")

    label("loc_4D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_4E8")
    OP_B1("E0301_5")
    Jump("loc_518")

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_4FB")
    OP_B1("E0301_2")
    Jump("loc_518")

    label("loc_4FB")

    OP_B1("E0301_1")
    LoadEffect(0x0, "map\\\\mp032_00.eff")

    label("loc_518")

    Return()

    # Function_1_458 end

    def Function_2_519(): pass

    label("Function_2_519")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x344, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_74D")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_74D")

    label("loc_531")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_74D")
    OP_8F(0x11, 0xFFFFFFEC, 0x9C4, 0x3764, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0x73A, 0x9C4, 0x3764, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0x73A, 0x9C4, 0x3A5C, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFF8F8, 0x9C4, 0x3A5C, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFF8F8, 0x9C4, 0x3CDC, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_8F(0x11, 0xFFFFFFEC, 0x9C4, 0x3D18, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x7C, 0x0, 0x64)
    PlayEffect(0x0, 0xFF, 0x11, 0, 1200, 500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    Jump("loc_531")

    label("loc_74D")

    Return()

    # Function_2_519 end

    def Function_3_74E(): pass

    label("Function_3_74E")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_771")
    OP_8D(0xFE, -2580, -8230, -860, -6510, 1000)
    Jump("Function_3_74E")

    label("loc_771")

    Return()

    # Function_3_74E end

    def Function_4_772(): pass

    label("Function_4_772")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_13FA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_CBC")

    ChrTalk(    #0
        0x10,
        (
            "#141FYo, Estelle!\x02\x03",

            "Killin' time till the dragon shows up?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x101,
        (
            "#1011FMore or less. How about you?\x01",
            "Putting stuff together for your\x01",
            "latest scoop?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#140FEh, not really. I'm waitin' for the star\x01",
            "of the show, same as you.\x02\x03",

            "Even if it doesn't show up, at least we\x01",
            "got a few nice shots of the Arseille.\x02\x03",

            "#147FWe're just lucky enough to even be\x01",
            "here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x101,
        (
            "#1000FHaha, you must be having a field\x01",
            "day.\x02\x03",

            "You get to cover the fight with the\x01",
            "dragon AND the new, cutting-edge\x01",
            "ship all in one go.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#141FHell, the dragon versus airships\x01",
            "thing alone would make it the story\x01",
            "of the decade.\x02\x03",

            "Every single reporter at the office\x01",
            "raised their hand when we were takin'\x01",
            "volunteers to cover this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x101,
        (
            "#1015FMmm, that figures.\x02\x03",

            "Congrats on getting picked for the job.\x01",
            "Did you guys draw straws or something?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#142FDraw...? No, of course not.\x02\x03",

            "#145FI got picked 'cause I'm a damn\x01",
            "good reporter.\x02\x03",

            "All that effort during the coup is\x01",
            "startin' to pay off.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#1004FWell, hey, more power to you!\x02\x03",

            "So even the Royal Army respects\x01",
            "you now, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10,
        (
            "#141FHey, if you write good stuff, even\x01",
            "the big guys'll come knockin' on\x01",
            "your door.\x02\x03",

            "By the way, if anything interesting's\x01",
            "come your way lately, I'm free to swap\x01",
            "a few stories aaany time you want.\x02\x03",

            "We could always use a few good\x01",
            "editorials to fill our pages.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x101,
        "#1001FHaha... Umm, we'll see.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A6F)
    Jump("loc_13FA")

    label("loc_CBC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1038")

    ChrTalk(    #10
        0x10,
        (
            "#140FSpeakin' of, Estelle. You close at\x01",
            "all to Captain Schwarz?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#1015FI wouldn't exactly call us close...\x02\x03",

            "I guess we've known each other for\x01",
            "a while now, though.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#141FDon't suppose you could introduce me?\x02\x03",

            "We've been getting hounded by readers\x01",
            "for a special edition featuring the 'female\x01",
            "captain of the Royal Guard.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x101,
        "#1004FJ-Julia's kinda...popular, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#140FOh, totally. I'd say she's about as\x01",
            "popular as Her Highness Klaudia.\x02\x03",

            "I've even heard some publishers are\x01",
            "itching to put a whole photo album of\x01",
            "her on the shelves.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #15
        0x101,
        "#1020FPH-PHOTO ALBUM?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x10,
        (
            "#145FIt's just a rumor floatin' around.\x02\x03",

            "Even if they wanted to, there's no way they'd\x01",
            "get permission...and I sure don't wanna be the\x01",
            "guy who's caught taking candid photos of HER.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x101,
        (
            "#1013FUh, yeah, yeah, that's true.\x01",
            "(I'd kind of like to see this album, though.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1A70)
    Jump("loc_13FA")

    label("loc_1038")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_138C")

    ChrTalk(    #18
        0x10,
        (
            "#141FTry to ask Captain Schwarz for that\x01",
            "interview at some point for me, yeah?\x02\x03",

            "The Royal Guard doesn't interact with\x01",
            "the people much, so everyone's got plenty\x01",
            "of questions about 'em.\x02\x03",

            "It'd be nice to get the chance to report\x01",
            "on who she really is.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34D, 6)), scpexpr(EXPR_END)), "loc_1389")

    ChrTalk(    #19
        0x101,
        (
            "#1007FOh, um, about that, Nial...\x02\x03",

            "I'm afraid she just straight-up refused.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #20
        0x10,
        (
            "#143FWHAT?!\x02\x03",

            "Refused? Already?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        (
            "#1016FAhaha, sorry, Nial.\x02\x03",

            "She said something about it being\x01",
            "kind of inconvenient?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x10,
        (
            "#145F*sigh* Right, right...\x02\x03",

            "Damn, she's even more guarded than\x01",
            "I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x101,
        "#1007FI'm sorry. I wish we could've helped.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        (
            "#142FAh, don't worry about it. Not your fault\x01",
            "they keep to themselves the way they\x01",
            "do.\x02\x03",

            "Still, there's gotta be some other way...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x101,
        (
            "#1019F(Just like Nial to not take the hint if\x01",
            "the prize is a hot scoop.)\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x0)
    OP_A2(0x1A74)

    label("loc_1389")

    Jump("loc_13FA")

    label("loc_138C")


    ChrTalk(    #26
        0x10,
        (
            "#145FShe wouldn't even say yes to you, huh?\x02\x03",

            "Figured it'd be easy to get at her through\x01",
            "a friend, too...\x02",
        )
    )

    CloseMessageWindow()

    label("loc_13FA")

    TalkEnd(0xFE)
    Return()

    # Function_4_772 end

    def Function_5_13FE(): pass

    label("Function_5_13FE")

    TalkBegin(0xFE)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_1834")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x34E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1775")

    ChrTalk(    #27
        0x11,
        "#150FYoohooo, Esteeelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x101,
        (
            "#1001FHi, Dorothy. You seem to be doing okay.\x02\x03",

            "Is your camera still treating you good?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#150FYou bet!\x02\x03",

            "This girl's so cute, she looks great\x01",
            "from ANY angle! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x101,
        (
            "#1011FAnd by 'this girl,' you mean...the Arseille?\x02\x03",

            "#1016FOh, Dorothy, you're as you as ever.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#151FHeehee! You too, Estelle.\x02\x03",

            "You're just as full of energy\x01",
            "as always! ㈱\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#1008FHaha... Well, thanks.\x02\x03",

            "#1017FEr, wait...\x02\x03",

            "Were you worried about me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#150FYeah, of course!\x02\x03",

            "#156FI mean, I...well...I took the photo\x01",
            "of Joshua, right?\x02\x03",

            "If that made you all sad, I'd have\x01",
            "to be sad, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x101,
        "#1003FOh, Dorothy... I'm sorry.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x11,
        (
            "#151FNoooo, it's okay!\x02\x03",

            "I'm a reporter, so it's my job to try\x01",
            "and cheer people up! Umm, sort of.\x02\x03",

            "If you're worried about anything else,\x01",
            "talk to me any time! ♪\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x101,
        "#1016FAh-hahaha... I'll, um, keep that in mind!\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A71)
    Jump("loc_1834")

    label("loc_1775")


    ChrTalk(    #37
        0x11,
        (
            "#150FI'm just gonna be taking pictures of\x01",
            "this beauty until the dragon shows up!\x02\x03",

            "#151FAnd theeen I'm gonna pretend to get\x01",
            "interior shots while getting pics of the\x01",
            "lady captain instead!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1834")

    SetChrChipByIndex(0x11, 10)
    SetChrSubChip(0x11, 0)
    TalkEnd(0xFE)
    Return()

    # Function_5_13FE end

    def Function_6_1842(): pass

    label("Function_6_1842")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1EBB")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_18AF"),
        (1, "loc_1E84"),
        (2, "loc_1EB5"),
        (SWITCH_DEFAULT, "loc_1EB8"),
    )


    label("loc_18AF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_1E81")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E17")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18E5")

    ChrTalk(    #38
        0xFE,
        "#020FHey, Estelle.\x02",
    )

    CloseMessageWindow()
    Jump("loc_18FE")

    label("loc_18E5")


    ChrTalk(    #39
        0xFE,
        "#020FHey, everyone.\x02",
    )

    CloseMessageWindow()

    label("loc_18FE")


    ChrTalk(    #40
        0x101,
        "#1011FHi, Schera. So this is where you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x102,
        "#1040FThinking about things?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xFE, 0x102, 400)

    ChrTalk(    #42
        0xFE,
        (
            "#524FMmm, I suppose.\x02\x03",

            "Seeing Esmelas Tower again is\x01",
            "just reminding me of simpler times,\x01",
            "that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x101,
        (
            "#1008FNow that I think about it, we HAVE\x01",
            "done a lot there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1041FHaha. That's true.\x02\x03",

            "That's kind of where it all began.\x01",
            "You know, with our first real job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8E")

    ChrTalk(    #45
        0x107,
        "#560FWow, really?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_1A8E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AB1")

    ChrTalk(    #46
        0x105,
        "#040FReally?\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_1AB1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AED")

    ChrTalk(    #47
        0x106,
        "#051FReally? Never heard that before.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1B11")

    label("loc_1AED")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B11")

    ChrTalk(    #48
        0x108,
        "#070FOh, really?\x02",
    )

    CloseMessageWindow()

    label("loc_1B11")

    TurnDirection(0xFE, 0x101, 400)

    ChrTalk(    #49
        0xFE,
        (
            "#021FIt was. That was back\x01",
            "when you two were freshly-minted\x01",
            "junior bracers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #50
        0x101,
        (
            "#1015FYeah. Some local kids wandered\x01",
            "into the tower.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x102,
        (
            "#1035FIt was our job to go and rescue them.\x02\x03",

            "#1048FOf course, Dad ended up stealing the\x01",
            "spotlight at the very end, as usual.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1C73")

    ChrTalk(    #52
        0x108,
        (
            "#071FHah! Of course he did!\x02\x03",

            "That sounds just like him.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D71")

    label("loc_1C73")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CC7")

    ChrTalk(    #53
        0x106,
        (
            "#051FHah, that figures.\x02\x03",

            "The old man really needs to grow up.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D71")

    label("loc_1CC7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D2B")

    ChrTalk(    #54
        0x105,
        (
            "#045FHaha, I'm not too surprised.\x02\x03",

            "That does sound every bit like\x01",
            "Mr. Bright.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1D71")

    label("loc_1D2B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1D71")

    ChrTalk(    #55
        0x107,
        (
            "#067FHeehee!\x02\x03",

            "That does sound a lot like your dad.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1D71")


    ChrTalk(    #56
        0xFE,
        (
            "#020FYou've both come a long way since then.\x02\x03",

            "This time, it'll be up to you to put an\x01",
            "end to things.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        (
            "#1006FDon't worry, Schera.\x01",
            "We'll make it happen.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E27)
    Jump("loc_1E81")

    label("loc_1E17")


    ChrTalk(    #58
        0xFE,
        (
            "#020FTo think we'd be returning to Esmelas\x01",
            "Tower like this, hmm?\x02\x03",

            "I'm ready. Give the word any time.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1E81")

    Jump("loc_1EB8")

    label("loc_1E84")


    ChrTalk(    #59
        0xB,
        "#020FWould you like me to come with?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_1EB8")

    label("loc_1EB5")

    Jump("loc_1EB8")

    label("loc_1EB8")

    Jump("loc_24AA")

    label("loc_1EBB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 6)), scpexpr(EXPR_END)), "loc_24AA")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x343, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2404")

    ChrTalk(    #60
        0x101,
        "#1011FSchera! So this is where you are.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0xB,
        "#020FHi there, Estelle. Taking a walk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x101,
        (
            "#1000FYup.\x02\x03",

            "Enjoying the wind?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0xB,
        (
            "#021FYes. The weather's lovely, so I'm taking\x01",
            "it easy.\x02\x03",

            "Knowing when to take a breather is part\x01",
            "of our job, too, you know. Short breaks like\x01",
            "these are good for keeping our minds sharp.\x02\x03",

            "Now's the perfect time.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1002FYeah, I know...\x02\x03",

            "Hey, Schera? Do you think\x01",
            "the plan'll work?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0xB,
        (
            "#020FTo be honest, I don't know.\x02\x03",

            "Common sense says there's a very\x01",
            "good chance it'll succeed.\x02\x03",

            "We have twelve patrol ships out on\x01",
            "patrol as we speak, after all.\x02\x03",

            "Hard to imagine even something as\x01",
            "powerful as a dragon getting away from\x01",
            "all that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        (
            "#1015FYeah...I guess you're right.\x02\x03",

            "General Morgan was pretty confident, too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0xB,
        (
            "#027FThat's just how he looks on the surface.\x02\x03",

            "Remember? He was none too happy to\x01",
            "have bracers on board.\x02\x03",

            "And yet he let us on anyway. That can\x01",
            "only mean one thing.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x101,
        (
            "#1002F...He's worried about how this'll turn out,\x01",
            "too?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0xB,
        (
            "#020FExactly.\x02\x03",

            "#525FAnd that, Estelle, is why conserving our\x01",
            "strength right now is a good idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1007FHaha, makes sense.\x02\x03",

            "Guess I'll keep wandering around a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0xB,
        (
            "#021FGood, that's what I like to hear.\x02\x03",

            "It's not every day you get to ride the\x01",
            "Arseille. Enjoy yourself!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x101,
        (
            "#1006FTrue enough.\x02\x03",

            "See you, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0xB,
        "#020FSee you soon, Estelle.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1A1F)
    Jump("loc_24AA")

    label("loc_2404")


    ChrTalk(    #74
        0xB,
        (
            "#020FThe fact that we're on board proves\x01",
            "General Morgan is uneasy.\x02\x03",

            "We need to be ready to act at a\x01",
            "moment's notice.\x02\x03",

            "But until then, I'm going to take it\x01",
            "easy.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_24AA")

    TalkEnd(0xFE)
    Return()

    # Function_6_1842 end

    def Function_7_24AE(): pass

    label("Function_7_24AE")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2B3E")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_251B"),
        (1, "loc_2B17"),
        (2, "loc_2B3B"),
        (SWITCH_DEFAULT, "loc_2B3E"),
    )


    label("loc_251B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_2B14")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2A7A")
    OP_4A(0xA, 255)

    ChrTalk(    #75
        0xA,
        (
            "#552FSo the next Enforcer's that kid, huh?\x02\x03",

            "The one who played us like a cheap\x01",
            "piano back in Grancel.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x101,
        (
            "#1002FYeah...\x02\x03",

            "I wonder if that giant archaism will\x01",
            "show up again.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x102,
        (
            "#1043FThat will largely depend on their strategy.\x01",
            "It's hard to say for sure.\x02\x03",

            "#1043FThat said, Renne won't be an easy fight\x01",
            "even if they don't use it.\x02\x03",

            "#1035FIn a straight, head-on engagement,\x01",
            "she's probably more capable than I am.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    def lambda_26EB():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_26EB)
    Sleep(120)

    def lambda_26FE():
        TurnDirection(0xFE, 0x102, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_26FE)
    TurnDirection(0x101, 0x102, 400)
    Sleep(600)

    ChrTalk(    #78
        0x101,
        (
            "#1020FB-Better than YOU, Joshua...?\x02\x03",

            "You're kidding, right?! And she's got that\x01",
            "archaism to top it off...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #79
        0x102,
        (
            "#1035FI'm not. From what I know of Renne's training, she's\x01",
            "had equal instruction in infiltration and direct assault,\x01",
            "whereas I was trained purely in covert operations.\x02\x03",

            "It should come as no surprise that she's more than\x01",
            "capable of taking out her enemies single-handedly.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_28DD")

    ChrTalk(    #80
        0x108,
        "#072FIn other words, we can't let our guard down.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2972")

    label("loc_28DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_290E")

    ChrTalk(    #81
        0x103,
        "#022FThat does make sense.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2972")

    label("loc_290E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_294E")

    ChrTalk(    #82
        0x109,
        "#1064FThese Enforcers are somethin' else.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2972")

    label("loc_294E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2972")

    ChrTalk(    #83
        0x107,
        "#065FN-No way...\x02",
    )

    CloseMessageWindow()

    label("loc_2972")


    ChrTalk(    #84
        0xA,
        (
            "#051FYeah, well, sounds like a party to me.\x02\x03",

            "Let's knock some sense into that kid\x01",
            "and give her the lecture of the damn century!\x02\x03",

            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0xA, 400)

    ChrTalk(    #85
        0x101,
        "#1006FThanks, Agate. I know you're good for it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x102,
        "#1040FYeah, thanks, Agate.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1E46)
    Jump("loc_2B14")

    label("loc_2A7A")


    ChrTalk(    #87
        0xA,
        (
            "#053FNext up is that girl, huh?\x02\x03",

            "#051FLet's knock some sense into her and\x01",
            "give her the lecture of the damn century!\x02\x03",

            "You need me, just say the word.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2B14")

    Jump("loc_2B3E")

    label("loc_2B17")


    ChrTalk(    #88
        0xA,
        "#050FNeed me to sub in?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_2B3E")

    label("loc_2B3B")

    Jump("loc_2B3E")

    label("loc_2B3E")

    TalkEnd(0xFE)
    Return()

    # Function_7_24AE end

    def Function_8_2B42(): pass

    label("Function_8_2B42")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_302F")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2F4D")
    OP_4A(0x9, 255)

    ChrTalk(    #89
        0x9,
        "#047F...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x101,
        "#1026FWhat's wrong, Kloe?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2BE2")

    ChrTalk(    #91
        0x9,
        (
            "#043FOh. Hey, Estelle...\x02\x03",

            "#047FIt's nothing. I was just thinking.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2C26")

    label("loc_2BE2")


    ChrTalk(    #92
        0x9,
        (
            "#043FOh. Hey, guys...\x02\x03",

            "#047FIt's nothing. I was just thinking.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2C26")


    ChrTalk(    #93
        0x101,
        (
            "#1003FThinking, huh...?\x02\x03",

            "I guess you would be kinda worried.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x9, 0x101, 400)

    ChrTalk(    #94
        0x9,
        "#043FI'm sorry. I know this is a bad time.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x101,
        (
            "#1000FNo, don't worry about it.\x02\x03",

            "Not like I'm one to talk, anyway.\x01",
            "Just a little while ago, I was the\x01",
            "one making everyone worry.\x02\x03",

            "#1007FThough in my case, it was all a\x01",
            "CERTAIN SOMEONE'S fault.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x102,
        (
            "#1048F*sigh* Yes, yes, I throw myself on my\x01",
            "blades in regret, on the hour, every hour.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x9,
        "#048FHaha...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x101,
        (
            "#1008FSo, Kloe? Don't worry about being a\x01",
            "burden or something, okay?\x02\x03",

            "We help each other out when we're in\x01",
            "trouble, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x9,
        (
            "#040FThank you, Estelle.\x02\x03",

            "Still, don't hesitate to call on me\x01",
            "if you need me.\x02\x03",

            "I know my skills in battle are meager,\x01",
            "but I'll do everything I can to help.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x101,
        "#1006FI will.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #101
        0x102,
        "#1040FWe'll be counting on you, Kloe.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #102
        0x9,
        "#041FOkay!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x9, 0x10)
    OP_A2(0x1E26)
    Jump("loc_302F")

    label("loc_2F4D")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FB0"),
        (1, "loc_3002"),
        (2, "loc_302C"),
        (SWITCH_DEFAULT, "loc_302F"),
    )


    label("loc_2FB0")


    ChrTalk(    #103
        0x9,
        (
            "#040FDon't hesitate to call on me\x01",
            "if you need me.\x02\x03",

            "Be careful, all right?\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_302F")

    label("loc_3002")


    ChrTalk(    #104
        0x9,
        "#040FOh, do you need my help?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_302F")

    label("loc_302C")

    Jump("loc_302F")

    label("loc_302F")

    TalkEnd(0xFE)
    Return()

    # Function_8_2B42 end

    def Function_9_3033(): pass

    label("Function_9_3033")

    TalkBegin(0xFE)
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        1,
        (
            "Talk\x01",              # 0
            "Change Party\x01",      # 1
            "Leave\x01",             # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_3099"),
        (1, "loc_34A6"),
        (2, "loc_34D0"),
        (SWITCH_DEFAULT, "loc_34D3"),
    )


    label("loc_3099")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C8, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3459")

    ChrTalk(    #105
        0x8,
        "#060FHi, Estelle!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #106
        0x101,
        "#1011FTita! Why're you out on the deck?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x8, 0x101, 400)

    ChrTalk(    #107
        0x8,
        (
            "#063FI heard Zeiss had been attacked...\x02\x03",

            "I was just wondering if, um, if everyone\x01",
            "was okay.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x101,
        "#1003FI... I see...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x102,
        (
            "#1040FThey'll be fine, don't worry.\x02\x03",

            "Zeiss is located near Leiston Fortress,\x01",
            "and their garrison isn't exactly small.\x02\x03",

            "Kilika's at the guild, too.\x02\x03",

            "She'll get involved if things get really\x01",
            "serious, I'm sure.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #110
        0x101,
        (
            "#1015FThat's a good point, actually.\x02\x03",

            "Thinking that Kilika's there makes ME\x01",
            "feel better.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x8,
        (
            "#560FHeehee, me, too.\x02\x03",

            "#067FYeah, I actually feel a little better now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x102,
        (
            "#1040FIf we can take control of the towers,\x01",
            "the enemy should back off from the cities.\x02\x03",

            "Their activities in the cities are likely little\x01",
            "more than a diversion from the towers.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x101,
        "#1002FIn other words, we've got no time to waste!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #114
        0x108,
        "#070FExactly. We'd best get going.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #115
        0x102,
        (
            "#1040FYes, you're right.\x02\x03",

            "See you later, Tita.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #116
        0x8,
        (
            "#060FOkay.\x02\x03",

            "Be careful, everyone!\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E42)
    Jump("loc_34A3")

    label("loc_3459")


    ChrTalk(    #117
        0x8,
        (
            "#060FI'll be here, so just say\x01",
            "if you need me!\x02\x03",

            "Take care, everyone!\x02",
        )
    )

    CloseMessageWindow()

    label("loc_34A3")

    Jump("loc_34D3")

    label("loc_34A6")


    ChrTalk(    #118
        0x8,
        "#060FOh, can I come with you?\x02",
    )

    CloseMessageWindow()
    Call(0, 12)
    Jump("loc_34D3")

    label("loc_34D0")

    Jump("loc_34D3")

    label("loc_34D3")

    TalkEnd(0xFE)
    Return()

    # Function_9_3033 end

    def Function_10_34D7(): pass

    label("Function_10_34D7")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_35D3")

    ChrTalk(    #119
        0xFE,
        "Hey, bracers!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0xFE,
        (
            "My research has stalled, so I thought\x01",
            "I'd step out to clear my head a bit.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #121
        0xFE,
        (
            "I wonder what's going on with the\x01",
            "tower. Very strange...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #122
        0xFE,
        (
            "I'm worried about my little brother\x01",
            "in Ruan. I hope the town's safe.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x3)
    Jump("loc_365B")

    label("loc_35D3")


    ChrTalk(    #123
        0xFE,
        (
            "I wonder what's going on with the\x01",
            "tower. Very strange...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0xFE,
        (
            "I'm worried about my little brother\x01",
            "in Ruan. I hope the town's safe.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_365B")

    TalkEnd(0xFE)
    Return()

    # Function_10_34D7 end

    def Function_11_365F(): pass

    label("Function_11_365F")

    TalkBegin(0xFE)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x217, 6)), scpexpr(EXPR_END)), "loc_36BD")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #125
        0xFE,
        "Fumyaaa... Nyaon.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36BA")

    ChrTalk(    #126
        0x105,
        "#040FWell, look who's sunbathing.\x02",
    )

    CloseMessageWindow()

    label("loc_36BA")

    Jump("loc_3A41")

    label("loc_36BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C9, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_383D")
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #127
        0xFE,
        "Nyaa!\x02",
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #128
        0x101,
        "#1004FAntoine!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_374E")

    ChrTalk(    #129
        0x107,
        (
            "#067FHeehee! Surprised?\x02\x03",

            "Ray brought him on-board.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3790")

    label("loc_374E")


    ChrTalk(    #130
        0x102,
        (
            "#1044FDid someone from the central factory\x01",
            "bring him aboard?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3790")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #131
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x101,
        (
            "#1011FWell, look at you! Never thought we'd\x01",
            "meet again under these circumstances!\x02\x03",

            "#1000FIt's good to see you again, Antoine.\x01",
            "Who's a good kitty?\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1E4C)
    Jump("loc_386D")

    label("loc_383D")


    ChrTalk(    #133
        0x101,
        "#1001FWhat are you doing out here, anyway?\x02",
    )

    CloseMessageWindow()

    label("loc_386D")

    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #134
        0xFE,
        "Nyao?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0xFE,
        "Nyayayaa～!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #136
        0x102,
        (
            "#1041FHaha, it looks like someone's trying\x01",
            "to tell us something.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A0B")

    ChrTalk(    #137
        0x105,
        "#044FI think he wants to give us something.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #138
        0xFE,
        "Nyao-n!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #139
        0x105,
        (
            "#041FYou're giving us this book?\x01",
            "(You have...a book...?)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #140
        "\x07\x00Received #579i.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_59()
    OP_3E(0x243, 1)
    OP_A2(0x10BE)

    ChrTalk(    #141
        0x105,
        "#048FHeehee, thank you, Antoine!\x02",
    )

    CloseMessageWindow()
    OP_22(0x192, 0x0, 0x64)

    ChrTalk(    #142
        0xFE,
        "Mya～uun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #143
        0x101,
        "#1016FWell, this is special...\x02",
    )

    CloseMessageWindow()
    Jump("loc_3A41")

    label("loc_3A0B")


    ChrTalk(    #144
        0x101,
        (
            "#1016FDo we know anyone who can\x01",
            "talk to animals?\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A41")

    TalkEnd(0xFE)
    Return()

    # Function_11_365F end

    def Function_12_3A45(): pass

    label("Function_12_3A45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3A91")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x443, 1)), scpexpr(EXPR_END)), "loc_3A73")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    Jump("loc_3A8E")

    label("loc_3A73")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xFFFF)

    label("loc_3A8E")

    Jump("loc_3B0F")

    label("loc_3A91")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_3AB4")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)
    Jump("loc_3B0F")

    label("loc_3AB4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3AD5")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x2, 0xFF, 0x5, 0x6, 0x4, 0x8, 0x7, 0xFFFF)
    Jump("loc_3B0F")

    label("loc_3AD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3AF6")
    OP_C9(0x1, 0x4, 0x0, 0x1, 0x7, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x8, 0xFFFF)
    Jump("loc_3B0F")

    label("loc_3AF6")

    OP_C9(0x1, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x4, 0x7, 0x8, 0xFFFF)

    label("loc_3B0F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Fade(1000)
    SetChrFlags(0xB, 0x80)
    SetChrFlags(0xA, 0x80)
    SetChrFlags(0x8, 0x80)
    SetChrFlags(0x9, 0x80)
    SetChrFlags(0xC, 0x80)
    SetChrFlags(0xD, 0x80)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x440, 1)), scpexpr(EXPR_END)), "loc_3B45")
    Jump("loc_3C12")

    label("loc_3B45")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C3, 6)), scpexpr(EXPR_END)), "loc_3B79")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3B76")
    SetChrPos(0xA, -60, 3000, 19860, 0)
    ClearChrFlags(0xA, 0x80)
    OP_43(0xA, 0x0, 0x6, 0x2)

    label("loc_3B76")

    Jump("loc_3C12")

    label("loc_3B79")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C2, 1)), scpexpr(EXPR_END)), "loc_3B83")
    Jump("loc_3C12")

    label("loc_3B83")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C1, 2)), scpexpr(EXPR_END)), "loc_3BB7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BB4")
    SetChrPos(0x8, 3490, 1500, -6210, 90)
    ClearChrFlags(0x8, 0x80)
    OP_43(0x8, 0x0, 0x6, 0x2)

    label("loc_3BB4")

    Jump("loc_3C12")

    label("loc_3BB7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 1)), scpexpr(EXPR_END)), "loc_3C12")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3BE8")
    SetChrPos(0xB, -1920, 1500, -9370, 270)
    ClearChrFlags(0xB, 0x80)
    OP_43(0xB, 0x0, 0x6, 0x2)

    label("loc_3BE8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_LSS), scpexpr(EXPR_END)), "loc_3C12")
    SetChrPos(0x9, 2300, 2500, 14260, 90)
    ClearChrFlags(0x9, 0x80)
    OP_43(0x9, 0x0, 0x6, 0x2)

    label("loc_3C12")

    Return()

    # Function_12_3A45 end

    def Function_13_3C13(): pass

    label("Function_13_3C13")

    EventBegin(0x0)
    Call(0, 28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3C0, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C27")
    OP_A2(0x10F0)
    Jump("loc_3C2A")

    label("loc_3C27")

    OP_A2(0x10F1)

    label("loc_3C2A")

    NewScene("ED6_DT21/R0303   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_3C13 end

    def Function_14_3C34(): pass

    label("Function_14_3C34")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R3104   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_3C34 end

    def Function_15_3C47(): pass

    label("Function_15_3C47")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R2401   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_3C47 end

    def Function_16_3C5A(): pass

    label("Function_16_3C5A")

    EventBegin(0x0)
    Call(0, 28)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/R1402   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_3C5A end

    def Function_17_3C6D(): pass

    label("Function_17_3C6D")

    EventBegin(0x0)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(70, 2500, 10950, 0)
    OP_67(0, 8380, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(414, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_6F(0x1, 0)
    OP_70(0x1, 0x3B)
    OP_73(0x1)
    Sleep(500)

    def lambda_3CE6():
        OP_6D(600, 2500, 15570, 6500)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3CE6)

    def lambda_3CFE():
        OP_67(0, 6000, -10000, 6500)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3CFE)

    def lambda_3D16():
        OP_6E(262, 6500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_3D16)
    OP_43(0x101, 0x1, 0x0, 0x12)
    OP_43(0x102, 0x1, 0x0, 0x13)
    OP_43(0xB, 0x1, 0x0, 0x14)
    OP_43(0xA, 0x1, 0x0, 0x15)
    OP_43(0x8, 0x1, 0x0, 0x16)
    OP_43(0xC, 0x1, 0x0, 0x17)
    OP_43(0xD, 0x1, 0x0, 0x18)
    OP_43(0x9, 0x1, 0x0, 0x19)
    OP_43(0xF, 0x1, 0x0, 0x1A)
    OP_43(0xE, 0x1, 0x0, 0x1B)
    WaitChrThread(0x102, 0x2)

    ChrTalk(    #145
        0x101,
        "#1000Fど、どこ……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #146
        0x102,
        (
            "#1030F前方甲板から\x01",
            "一番よく見える方向……\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0xD, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)
    OP_8C(0xD, 270, 400)
    Sleep(500)

    ChrTalk(    #147
        0xD,
        "#1060F……あれや！\x02",
    )

    CloseMessageWindow()

    def lambda_3DFC():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3DFC)

    def lambda_3E0A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3E0A)
    Sleep(50)

    def lambda_3E1D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_3E1D)

    def lambda_3E2B():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3E2B)
    Sleep(40)

    def lambda_3E3E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_3E3E)

    def lambda_3E4C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xC, 1, lambda_3E4C)
    Sleep(50)

    def lambda_3E5F():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E5F)

    def lambda_3E6D():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3E6D)
    Sleep(40)

    def lambda_3E80():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3E80)

    def lambda_3E8E():
        OP_6D(-1820, 2500, 15470, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3E8E)

    def lambda_3EA6():
        OP_6C(340000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3EA6)
    Sleep(3500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #148
        "\x07\x00◆浮遊都市が出現するムービー\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_77(0xFF, 0xFF, 0x80, 0x0, 0x0)
    OP_6D(600, 2500, 15570, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6E(262, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #149
        0x101,
        "#1000Fな、な、な……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #150
        0x9,
        (
            "#040Fまさかあれが……\x01",
            "……あの巨大な都市が……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #151
        0x102,
        "#1030Fうん……間違いない……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #152
        0xD,
        (
            "#1060F《輝く環》……\x01",
            "オーリオールっちゅう事か！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #153
        0xE,
        "#100F──いかん。\x02",
    )

    CloseMessageWindow()
    TurnDirection(0xE, 0xF, 400)
    Sleep(600)

    ChrTalk(    #154
        0xE,
        (
            "#100Fユリア大尉！\x01",
            "急いで艦を降ろすんじゃ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #155
        0xF,
        "#170F……え……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #156
        0xE,
        (
            "#100Fカシウスが伝えた\x01",
            "緊急指令があったじゃろ！\x02\x03",

            "急がんと手遅れになるぞ！\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #157
        0xF,
        "#170F！！！\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #158
        "\x07\x00◆浮遊都市から波が拡散して導力が停止していくムービー\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/C5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3C6D end

    def Function_18_4120(): pass

    label("Function_18_4120")

    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFDDA, 0xBB8, 0x4588, 0xFA0, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 90, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    OP_8C(0xFE, 270, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_18_4120 end

    def Function_19_4197(): pass

    label("Function_19_4197")

    Sleep(500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x23A, 0xBB8, 0x4394, 0xFA0, 0x0)
    Return()

    # Function_19_4197 end

    def Function_20_41C7(): pass

    label("Function_20_41C7")

    Sleep(1000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3C0, 0xBB8, 0x401A, 0xFA0, 0x0)
    Return()

    # Function_20_41C7 end

    def Function_21_41F7(): pass

    label("Function_21_41F7")

    Sleep(1500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF8D0, 0xBB8, 0x4114, 0xFA0, 0x0)
    Return()

    # Function_21_41F7 end

    def Function_22_4227(): pass

    label("Function_22_4227")

    Sleep(2000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4EC, 0x9C4, 0x39F8, 0xFA0, 0x0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_22_4227 end

    def Function_23_425E(): pass

    label("Function_23_425E")

    Sleep(2500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFEA2, 0x9C4, 0x3C3C, 0xFA0, 0x0)
    Return()

    # Function_23_425E end

    def Function_24_428E(): pass

    label("Function_24_428E")

    Sleep(3000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFF830, 0x9C4, 0x384A, 0xFA0, 0x0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_24_428E end

    def Function_25_42C5(): pass

    label("Function_25_42C5")

    Sleep(3500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFBB4, 0x9C4, 0x3462, 0xFA0, 0x0)
    Return()

    # Function_25_42C5 end

    def Function_26_42F5(): pass

    label("Function_26_42F5")

    Sleep(4000)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x3A2, 0x9C4, 0x2F8A, 0xFA0, 0x0)
    Return()

    # Function_26_42F5 end

    def Function_27_4325(): pass

    label("Function_27_4325")

    Sleep(4500)
    SetChrPos(0xFE, 100, 2500, 7780, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0xFFFFFF74, 0x9C4, 0x30D4, 0xFA0, 0x0)
    Return()

    # Function_27_4325 end

    def Function_28_4355(): pass

    label("Function_28_4355")

    OP_6D(-1900, -9600, -11180, 0)
    OP_67(0, 3300, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x4)
    OP_A1(0x14, 0x4)
    SetChrPos(0x14, 0, -7600, -7600, 0)
    SetChrPos(0x101, -550, -7600, -8150, 270)
    SetChrPos(0x102, 550, -7600, -8150, 270)
    SetChrPos(0xF8, -550, -7600, -7050, 270)
    SetChrPos(0xF9, 550, -7600, -7050, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)

    def lambda_445C():
        OP_67(0, 4700, -10000, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_445C)

    def lambda_4474():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_4474)

    def lambda_448F():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_448F)

    def lambda_44AA():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_44AA)

    def lambda_44C5():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_44C5)

    def lambda_44E0():
        OP_91(0xFE, 0x0, 0xFFFFB1E0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_44E0)
    ClearMapFlags(0x100000)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    Return()

    # Function_28_4355 end

    def Function_29_451A(): pass

    label("Function_29_451A")

    EventBegin(0x0)
    OP_67(0, 4700, -10000, 0)
    OP_6D(-550, -9330, -8150, 0)
    OP_67(0, 3370, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(48000, 0)
    OP_6E(262, 0)
    OP_72(0x4, 0x4)
    OP_A1(0x14, 0x4)
    SetChrPos(0x14, 0, -17600, -7600, 0)
    SetChrPos(0x101, -550, -17600, -8150, 270)
    SetChrPos(0x102, 550, -17600, -8150, 270)
    SetChrPos(0xF8, -550, -17600, -7050, 270)
    SetChrPos(0xF9, 550, -17600, -7050, 270)
    SetChrFlags(0x101, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrFlags(0xF8, 0x4)
    SetChrFlags(0xF9, 0x4)
    SetChrFlags(0x101, 0x20)
    SetChrFlags(0x102, 0x20)
    SetChrFlags(0xF8, 0x20)
    SetChrFlags(0xF9, 0x20)

    def lambda_45F7():
        OP_6D(-550, -9330, -8150, 6000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_45F7)

    def lambda_460F():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_460F)

    def lambda_462A():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_462A)

    def lambda_4645():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4645)

    def lambda_4660():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_4660)

    def lambda_467B():
        OP_91(0xFE, 0x0, 0x4E20, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_467B)
    SetMapFlags(0x100000)
    OP_22(0x68, 0x0, 0x64)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(2000)
    OP_23(0x1C3)
    OP_23(0x75)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0313   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_29_451A end

    SaveToFile()

Try(main)
