from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'E0811   ._SN',
        MapName             = 'Event',
        Location            = 'E0811.x',
        MapIndex            = 1,
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
        'Estelle',                              # 9
        'Joshua',                               # 10
        'Josette',                              # 11
        'Kyle',                                 # 12
        'Don',                                  # 13
        '結社艇',                               # 14
        '結社艇のライト',                       # 15
        '空賊艇',                               # 16
        '空賊艇のライト',                       # 17
        'Tita',                                 # 18
        'Kloe',                                 # 19
        'Agate',                                # 20
        'Scherazard',                           # 21
        'Zin',                                  # 22
        'Father Kevin',                         # 23
        'Professor Russell',                    # 24
        'Captain Schwarz',                      # 25
        'Target',                               # 26
        'Target',                               # 27
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
        'ED6_DT27/CH03010 ._CH',             # 00
        'ED6_DT27/CH03100 ._CH',             # 01
        'ED6_DT26/CH20370 ._CH',             # 02
        'ED6_DT26/CH20400 ._CH',             # 03
        'ED6_DT07/CH02120 ._CH',             # 04
        'ED6_DT27/CH03015 ._CH',             # 05
        'ED6_DT26/CH20401 ._CH',             # 06
        'ED6_DT27/CH03101 ._CH',             # 07
        'ED6_DT26/CH20398 ._CH',             # 08
        'ED6_DT07/CH00060 ._CH',             # 09
        'ED6_DT07/CH00040 ._CH',             # 0A
        'ED6_DT07/CH00050 ._CH',             # 0B
        'ED6_DT07/CH00020 ._CH',             # 0C
        'ED6_DT07/CH00070 ._CH',             # 0D
        'ED6_DT27/CH03080 ._CH',             # 0E
        'ED6_DT07/CH02020 ._CH',             # 0F
        'ED6_DT27/CH03580 ._CH',             # 10
        'ED6_DT07/CH00061 ._CH',             # 11
        'ED6_DT07/CH00041 ._CH',             # 12
        'ED6_DT07/CH00051 ._CH',             # 13
        'ED6_DT07/CH00021 ._CH',             # 14
        'ED6_DT07/CH00071 ._CH',             # 15
        'ED6_DT27/CH03081 ._CH',             # 16
        'ED6_DT27/CH03001 ._CH',             # 17
        'ED6_DT27/CH03011 ._CH',             # 18
        'ED6_DT26/CH20327 ._CH',             # 19
        'ED6_DT26/CH20398 ._CH',             # 1A
        'ED6_DT27/CH03000 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT27/CH03010P._CP',             # 00
        'ED6_DT27/CH03100P._CP',             # 01
        'ED6_DT26/CH20370P._CP',             # 02
        'ED6_DT26/CH20400P._CP',             # 03
        'ED6_DT07/CH02120P._CP',             # 04
        'ED6_DT27/CH03015P._CP',             # 05
        'ED6_DT26/CH20401P._CP',             # 06
        'ED6_DT27/CH03101P._CP',             # 07
        'ED6_DT26/CH20398P._CP',             # 08
        'ED6_DT07/CH00060P._CP',             # 09
        'ED6_DT07/CH00040P._CP',             # 0A
        'ED6_DT07/CH00050P._CP',             # 0B
        'ED6_DT07/CH00020P._CP',             # 0C
        'ED6_DT07/CH00070P._CP',             # 0D
        'ED6_DT27/CH03080P._CP',             # 0E
        'ED6_DT07/CH02020P._CP',             # 0F
        'ED6_DT27/CH03580P._CP',             # 10
        'ED6_DT07/CH00061P._CP',             # 11
        'ED6_DT07/CH00041P._CP',             # 12
        'ED6_DT07/CH00051P._CP',             # 13
        'ED6_DT07/CH00021P._CP',             # 14
        'ED6_DT07/CH00071P._CP',             # 15
        'ED6_DT27/CH03081P._CP',             # 16
        'ED6_DT27/CH03001P._CP',             # 17
        'ED6_DT27/CH03011P._CP',             # 18
        'ED6_DT26/CH20327P._CP',             # 19
        'ED6_DT26/CH20398P._CP',             # 1A
        'ED6_DT27/CH03000P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 27,
        ChipIndex           = 0x1B,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x184,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C4,
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
        Unknown3            = 9,
        ChipIndex           = 0x9,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 11,
        ChipIndex           = 0xB,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1CC,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1CC,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -100290,
        Y                   = 5150,
        Z                   = -94850,
        Range               = -98290,
        Unknown_10          = 0x1BEE,
        Unknown_14          = 0xFFFE954E,
        Unknown_18          = 0x0,
        Unknown_1C          = 6,
    )


    ScpFunction(
        "Function_0_40A",          # 00, 0
        "Function_1_57B",          # 01, 1
        "Function_2_581",          # 02, 2
        "Function_3_632",          # 03, 3
        "Function_4_1777",         # 04, 4
        "Function_5_1791",         # 05, 5
        "Function_6_17D5",         # 06, 6
        "Function_7_1855",         # 07, 7
        "Function_8_19BD",         # 08, 8
        "Function_9_1C2F",         # 09, 9
        "Function_10_22D7",        # 0A, 10
        "Function_11_2316",        # 0B, 11
        "Function_12_244F",        # 0C, 12
        "Function_13_247C",        # 0D, 13
        "Function_14_24A9",        # 0E, 14
        "Function_15_338D",        # 0F, 15
        "Function_16_33EF",        # 10, 16
        "Function_17_3431",        # 11, 17
        "Function_18_34D3",        # 12, 18
        "Function_19_3592",        # 13, 19
        "Function_20_35FC",        # 14, 20
        "Function_21_3666",        # 15, 21
        "Function_22_37A5",        # 16, 22
        "Function_23_38E4",        # 17, 23
        "Function_24_395D",        # 18, 24
        "Function_25_39D6",        # 19, 25
        "Function_26_3A6D",        # 1A, 26
        "Function_27_3B04",        # 1B, 27
        "Function_28_3C3A",        # 1C, 28
        "Function_29_3D48",        # 1D, 29
        "Function_30_3F7B",        # 1E, 30
        "Function_31_41AE",        # 1F, 31
        "Function_32_44A7",        # 20, 32
        "Function_33_4505",        # 21, 33
        "Function_34_4563",        # 22, 34
        "Function_35_4590",        # 23, 35
        "Function_36_45BD",        # 24, 36
        "Function_37_4728",        # 25, 37
        "Function_38_4919",        # 26, 38
        "Function_39_4B28",        # 27, 39
        "Function_40_4E23",        # 28, 40
        "Function_41_4F0B",        # 29, 41
        "Function_42_5038",        # 2A, 42
        "Function_43_566F",        # 2B, 43
        "Function_44_56DE",        # 2C, 44
        "Function_45_5769",        # 2D, 45
        "Function_46_57AD",        # 2E, 46
        "Function_47_57F8",        # 2F, 47
        "Function_48_5843",        # 30, 48
        "Function_49_588E",        # 31, 49
        "Function_50_58D9",        # 32, 50
        "Function_51_5924",        # 33, 51
        "Function_52_5968",        # 34, 52
        "Function_53_599D",        # 35, 53
        "Function_54_59D2",        # 36, 54
        "Function_55_5A5B",        # 37, 55
    )


    def Function_0_40A(): pass

    label("Function_0_40A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_41B")
    OP_A3(0x10F0)
    Event(0, 3)
    Jump("loc_57A")

    label("loc_41B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_435")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F1)
    Event(0, 9)
    Jump("loc_57A")

    label("loc_435")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 2)), scpexpr(EXPR_END)), "loc_44F")
    OP_A3(0x10F2)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_57A")

    label("loc_44F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 3)), scpexpr(EXPR_END)), "loc_469")
    OP_A3(0x10F3)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x59), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 31)
    Jump("loc_57A")

    label("loc_469")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 4)), scpexpr(EXPR_END)), "loc_47A")
    OP_A3(0x10F4)
    Event(0, 37)
    Jump("loc_57A")

    label("loc_47A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 5)), scpexpr(EXPR_END)), "loc_494")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x56), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F5)
    Event(0, 8)
    Jump("loc_57A")

    label("loc_494")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 6)), scpexpr(EXPR_END)), "loc_4AE")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x50), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F6)
    Event(0, 2)
    Jump("loc_57A")

    label("loc_4AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 7)), scpexpr(EXPR_END)), "loc_4C8")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x51), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F7)
    Event(0, 39)
    Jump("loc_57A")

    label("loc_4C8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 0)), scpexpr(EXPR_END)), "loc_51E")
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_A3(0x10F8)
    Event(0, 41)
    Jump("loc_57A")

    label("loc_51E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21F, 1)), scpexpr(EXPR_END)), "loc_57A")
    OP_76(0xFF, 0x0, 0x1, 0xFFFFFFFF, 0x0, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x1, 0x1, 0xFFFFFFFE, 0xFFFFFFFF, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x2, 0x1, 0xFFFFFFFB, 0xFFFFFFFE, 0x0, 0x0, 0x0)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x5A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x10F9)
    Event(0, 42)

    label("loc_57A")

    Return()

    # Function_0_40A end

    def Function_1_57B(): pass

    label("Function_1_57B")

    OP_71(0x5, 0x4)
    Return()

    # Function_1_57B end

    def Function_2_581(): pass

    label("Function_2_581")

    EventBegin(0x0)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(-213310, -10000, -14980, 0)
    OP_67(0, -2490, -10000, 0)
    OP_6B(43240, 0)
    OP_6C(351000, 0)
    OP_6E(262, 0)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    FadeToBright(2000, 0)

    def lambda_5EE():
        OP_67(0, -3300, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_5EE)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/T1211   ._SN", 103, 0, 0)
    IdleLoop()
    Return()

    # Function_2_581 end

    def Function_3_632(): pass

    label("Function_3_632")

    EventBegin(0x0)
    OP_DB()
    ClearParty()
    AddParty(0x1, 0xF6, 0xFF)
    SetChrFlags(0x102, 0x80)
    OP_71(0x0, 0x4)
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xF, 0x3)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    OP_48()
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 400)
    OP_70(0x3, 0x1C2)
    OP_6D(-289560, 30000, -136650, 0)
    OP_67(0, 2320, -10000, 0)
    OP_6B(12030, 0)
    OP_6C(66000, 0)
    OP_6E(300, 0)
    OP_EB(0xD5, 0x0)
    OP_BB(0x1, 0x1, 0x1)
    OP_BD()
    FadeToBright(2000, 0)

    def lambda_6EA():
        OP_6D(-99550, 5550, -94010, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_6EA)

    def lambda_702():
        OP_6B(2800, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_702)

    def lambda_712():
        OP_6E(334, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_712)
    Sleep(6000)
    OP_72(0x3, 0x20)

    def lambda_72C():
        OP_6C(35000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_72C)
    OP_67(0, 7540, -10000, 4000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x3)
    Sleep(1000)
    SetChrFlags(0xA, 0x4)
    SetChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -99440, 5550, -91440, 0)
    ClearChrFlags(0xA, 0x80)
    OP_8E(0xA, 0xFFFE7B72, 0x15A4, 0xFFFE90F8, 0x7D0, 0x0)
    Sleep(500)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)
    OP_DC()

    ChrTalk(    #0
        0xA,
        "#213Fあれ……？\x02",
    )

    CloseMessageWindow()
    OP_8C(0xA, 90, 400)
    Sleep(500)
    OP_8C(0xA, 180, 400)
    OP_8C(0xA, 270, 400)
    Sleep(500)
    OP_8C(0xA, 180, 400)
    Sleep(500)
    OP_8C(0xA, 90, 400)
    Sleep(200)
    SetChrPos(0x102, -100000, 5550, -89650, 0)
    SetChrFlags(0x102, 0x4)
    ClearChrFlags(0x102, 0x80)
    SetChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 2)
    SetChrSubChip(0x102, 2)
    OP_43(0xA, 0x1, 0x0, 0x5)

    def lambda_832():
        OP_6D(-98020, 5550, -89450, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_832)
    OP_6C(300000, 5000)
    OP_6C(212000, 5000)

    ChrTalk(    #1
        0xA,
        "#210Fなんだ、こっちにいたんだ。\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)

    ChrTalk(    #2
        0x102,
        (
            "#1030F……こちら側の方が\x01",
            "月が良く見えるからね。\x02\x03",

            "風の流れも肌で感じられる。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xA,
        (
            "#210Fあはは、ま～た\x01",
            "カッコ付けちゃってさ。\x02",
        )
    )

    CloseMessageWindow()

    def lambda_92F():
        OP_6D(-99380, 5550, -89630, 3000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_92F)

    def lambda_947():
        OP_6B(2350, 3000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_947)

    def lambda_957():
        OP_8E(0xA, 0xFFFE7D34, 0x15AE, 0xFFFEA296, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_957)
    Sleep(300)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    WaitChrThread(0xA, 0x0)
    OP_8C(0xA, 0, 400)
    WaitChrThread(0x102, 0x1)
    Fade(250)
    SetChrChipByIndex(0xA, 3)
    SetChrSubChip(0xA, 0)
    OP_0D()

    ChrTalk(    #4
        0xA,
        (
            "#210F……よっと。\x02\x03",

            "カッコ付けている\x01",
            "わけじゃないか……\x02\x03",

            "必要なんだよね、それも？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x102,
        (
            "#1030F月明かり、雲の位置、風の流れが\x01",
            "けっこう重要になって来るから。\x02\x03",

            "失敗の可能性は\x01",
            "なるべく下げておきたいんだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0xA,
        "#210Fな、なるべくって……\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0xA, 4)
    Sleep(100)

    ChrTalk(    #7
        0xA,
        (
            "#210Fあんたねえ……\x01",
            "出来るかぎりって言いなよ！\x02\x03",

            "失敗したら死んじゃうんだよ！？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x102,
        (
            "#1030F大丈夫、失敗の可能性は軽微だ。\x02\x03",

            "この程度のミッション、\x01",
            "昔は毎日こなしていたからね。\x02\x03",

            "むしろ危険なのは……\x01",
            "ミッションが成功してからだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xA,
        (
            "#210F………………………………\x02\x03",

            "……ね、ヨシュア。\x02\x03",

            "本当にあんたが\x01",
            "そこまでやる必要あるわけ？\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(100)

    ChrTalk(    #10
        0x102,
        "#1030Fえ……？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xA,
        (
            "#210Fあんたもボクたちと同じ\x01",
            "エレボニア生まれなんだよね。\x02\x03",

            "そりゃあお互い、事情があって　\x01",
            "故郷に帰れないかもしれないけど……\x02\x03",

            "だからといって、この国に\x01",
            "義理立てする必要ないじゃない？\x02\x03",

            "《結社》が何をしようが\x01",
            "放っておけばいいんだよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x102,
        "#1030F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0xA,
        (
            "#210Fね、今ならまだ間に合うよ。\x02\x03",

            "このまま、ボクたちと一緒に\x01",
            "リベールを離れてさ……\x02\x03",

            "どこかの自治州あたりで\x01",
            "パーッと一旗揚げてみない？\x02\x03",

            "空賊稼業が気に喰わなければ\x01",
            "他の仕事を探してもいいんだし。\x02\x03",

            "アニキたちとも話したんだけど\x01",
            "この船のスピードを活かした\x01",
            "運送業なんていいと思うんだよね。\x02",
        )
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 6)
    Sleep(100)

    ChrTalk(    #14
        0x102,
        (
            "#1030F飛行船を使った運送業か……\x02\x03",

            "今後も需要は増えそうだし\x01",
            "なかなか有望なビジネスかもね。\x02\x03",

            "少なくとも空賊よりは\x01",
            "確実に稼げると思うよ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0xA,
        "#210Fそ、それじゃあ！\x02",
    )

    CloseMessageWindow()
    SetChrSubChip(0x102, 5)
    Sleep(100)
    SetChrSubChip(0x102, 4)
    Sleep(100)

    ChrTalk(    #16
        0x102,
        (
            "#1030Fそうだね……\x02\x03",

            "《結社》の計画を潰して\x01",
            "僕が生き残ることが出来たら\x01",
            "考えさせてもらおうかな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0xA,
        "#210F………………………………\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x102,
        (
            "#1030Fああ、心配しなくても\x01",
            "僕たちの契約はこれで終わりだ。\x02\x03",

            "この作戦に協力してくれたら\x01",
            "貸しは帳消しという約束だからね。\x02\x03",

            "いつでも出発してくれて構わない。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0xA,
        "#210F……もういい。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x102,
        "#1030Fえ。\x02",
    )

    CloseMessageWindow()
    Sleep(250)
    Fade(500)
    OP_8C(0xA, 270, 0)
    SetChrSubChip(0xA, 0)
    SetChrChipByIndex(0xA, 1)
    OP_0D()
    Sleep(200)

    ChrTalk(    #21
        0xA,
        (
            "#210Fバカ！\x01",
            "誰が貸し借りの話をしてるのさ！\x02\x03",

            "もういい！\x01",
            "あんたなんか知るもんか！\x02\x03",

            "勝手に危険に飛び込んで\x01",
            "勝手にくたばっちゃえばいいんだ！\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xA, 0xFFFE8E3C, 0x15AE, 0xFFFEA070, 0x1388, 0x0)
    OP_8E(0xA, 0xFFFE8DA6, 0x15AE, 0xFFFE94FE, 0x1388, 0x0)
    OP_8E(0xA, 0xFFFE7BC2, 0x15AE, 0xFFFE910C, 0x1388, 0x0)
    OP_22(0x6A, 0x0, 0x64)
    SetChrFlags(0xA, 0x80)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    Sleep(300)
    SetChrSubChip(0x102, 3)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 2)
    Sleep(100)

    ChrTalk(    #22
        0x102,
        (
            "#1030F………………………………\x02\x03",

            "……ごめん、ジョゼット。\x02",
        )
    )

    CloseMessageWindow()
    SetChrBattleFlags(0xB, 0x20)
    SetChrPos(0xB, -103120, 13050, -91360, 10)
    Sleep(300)

    NpcTalk(    #23
        0xB,
        "青年の声",
        (
            "#3Pまったく……\x01",
            "鈍いフリも楽じゃないねぇ。\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    SetChrSubChip(0x102, 1)
    Sleep(100)
    SetChrSubChip(0x102, 0)
    Sleep(100)
    OP_6F(0x3, 90)
    SetChrPos(0xB, -103120, 9050, -91360, 10)
    SetChrFlags(0xB, 0x4)
    SetChrFlags(0xB, 0x40)
    SetChrFlags(0xB, 0x20)
    ClearChrFlags(0xB, 0x1)
    ClearChrFlags(0xB, 0x80)
    Fade(500)
    ClearChrFlags(0x102, 0x2)
    SetChrChipByIndex(0x102, 65535)
    SetChrSubChip(0x102, 0)
    OP_0D()
    OP_8C(0x102, 270, 400)

    def lambda_128B():
        OP_6D(-100330, 5550, -92350, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_128B)

    def lambda_12A3():
        OP_67(0, 9500, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_12A3)
    OP_6C(144000, 4000)
    Sleep(300)

    ChrTalk(    #24
        0x102,
        "#1030F……キールさん。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0xB,
        (
            "#200Fあいつもいい加減、\x01",
            "ガキっぽさが抜けないんだが……\x02\x03",

            "それでも、今のはやっぱり\x01",
            "お前の言い方が悪いと思うぜ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x102,
        (
            "#1030F……そうだね。\x02\x03",

            "謝るつもりはないけど\x01",
            "済まないとは思っている。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0xB,
        (
            "#200Fやれやれ……\x01",
            "それがお前なりの気遣いだとは\x01",
            "分かっちゃいるんだけどな。\x02\x03",

            "まあ、さっきの話は\x01",
            "真剣に考えておいてくれや。\x02\x03",

            "全てのケリを付けた後、\x01",
            "あの遊撃士の嬢ちゃんの元に\x01",
            "帰るつもりがないんだったらな。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1030Fはは……それは無いよ。\x02\x03",

            "所詮、僕と彼女は\x01",
            "生きている世界が違いすぎる。\x02\x03",

            "もう交わることは無いはずだ。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0xB,
        (
            "#200Fふーん……\x01",
            "ま、いいけどな。\x02\x03",

            "だったら尚更\x01",
            "悪い話じゃないだろう？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x102,
        (
            "#1030Fそうだね……\x01",
            "前向きに考えておくよ。\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0xAB, 0x1, 0x64)
    Sleep(500)
    OP_62(0xB, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(2200)
    OP_23(0xAB)

    ChrTalk(    #31
        0xB,
        "#200F……おいでなすったか！\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    SetChrPos(0xB, -103120, 8900, -91360, 270)
    Sleep(500)

    ChrTalk(    #32
        0xB,
        "#200F兄貴、来たのか！？\x02",
    )

    CloseMessageWindow()
    SetChrPos(0xC, -103120, 6550, -91360, 270)

    NpcTalk(    #33
        0xC,
        "ドルンの声",
        (
            "おお！\x01",
            "小僧の読み通りだ！\x02\x03",

            "北東の方から\x01",
            "ぐんぐん近付いているぜ！\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0xB, -103120, 9050, -91360, 270)
    OP_8C(0xB, 10, 400)

    ChrTalk(    #34
        0xB,
        (
            "#200F聞いての通りだ。\x01",
            "すぐにブリッジに来な。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x102,
        "#1030F分かった。\x02",
    )

    CloseMessageWindow()
    OP_8C(0xB, 270, 400)
    OP_43(0xB, 0x1, 0x0, 0x4)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 90)
    OP_70(0x3, 0xA0)
    OP_A2(0x1C00)
    Sleep(1000)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x00◆このイベントシーンは仮マップです。\x01",
            "　船内に入る時はデバックキーの『Ｊ』で入口付近に接触してください。\x01",
            "　仮エントリーに引っかかり中に入れます。\x02",
        )
    )

    Sleep(1000)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_632 end

    def Function_4_1777(): pass

    label("Function_4_1777")

    OP_8F(0xFE, 0xFFFE6D30, 0x17A2, 0xFFFE9B20, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_4_1777 end

    def Function_5_1791(): pass

    label("Function_5_1791")

    OP_8E(0xFE, 0xFFFE8F54, 0x15AE, 0xFFFE951C, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8EC8, 0x15AE, 0xFFFE9FC6, 0x5DC, 0x0)
    OP_8E(0xFE, 0xFFFE8C52, 0x15AE, 0xFFFEA0FC, 0x5DC, 0x0)
    OP_8C(0xFE, 305, 400)
    Return()

    # Function_5_1791 end

    def Function_6_17D5(): pass

    label("Function_6_17D5")

    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x00◆仮エントリー【⇒空賊艇内部夜用（E0110）】\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_183F")
    NewScene("ED6_DT21/E0111   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_1854")

    label("loc_183F")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1854")
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()

    label("loc_1854")

    Return()

    # Function_6_17D5 end

    def Function_7_1855(): pass

    label("Function_7_1855")

    EventBegin(0x0)
    OP_DB()
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    SetChrFlags(0x102, 0x80)
    OP_A1(0xD, 0x2)
    OP_A1(0xF, 0x3)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    OP_6D(43700, -10000, 9730, 0)
    OP_67(0, 640, -10000, 0)
    OP_6B(43830, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x14)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)

    def lambda_1931():
        OP_6B(32830, 4000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1931)
    FadeToBright(500, 0)
    OP_0D()
    WaitChrThread(0xB, 0x1)
    OP_22(0x7C, 0x0, 0x64)
    OP_6D(116270, -10000, 41470, 0)
    OP_67(0, 1020, -10000, 0)
    OP_6B(18860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    SetMapFlags(0x2000000)
    Sleep(3000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AE(0x1388)
    OP_DC()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_7_1855 end

    def Function_8_19BD(): pass

    label("Function_8_19BD")

    EventBegin(0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    SetChrFlags(0x102, 0x80)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 100000, 4000, 0, 270)
    SetChrPos(0xE, 100000, 4000, 0, 90)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_11(0x38, 0x44, 0x58, 0x4E20, 0xF4240, 0x0)
    OP_6D(1000, 2700, 2800, 0)
    OP_67(0, 680, -10000, 0)
    OP_6B(36240, 0)
    OP_6C(78000, 0)
    OP_6E(559, 0)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x1E)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x1, "C_VIS227._CH")
    OP_C6(0x0, 0x3, -1, 0, 0)
    FadeToBright(500, 0)

    def lambda_1ADB():
        OP_6B(22830, 6000)
        ExitThread()

    QueueWorkItem(0xB, 1, lambda_1ADB)

    def lambda_1AEB():
        OP_8F(0xFE, 0x0, 0xFA0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1AEB)

    def lambda_1B06():
        OP_8F(0xFE, 0x0, 0xFA0, 0x0, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1B06)
    Sleep(6400)
    FadeToDark(100, 0, -1)
    OP_0D()
    Sleep(200)
    OP_22(0x7C, 0x0, 0x64)
    OP_44(0xD, 0x0)
    OP_44(0xE, 0x0)
    SetChrPos(0xD, 10000, 4000, 0, 270)
    SetChrPos(0xE, 10000, 4000, 0, 270)
    OP_6D(116270, -10000, 41470, 0)
    OP_67(0, 1320, -10000, 0)
    OP_6B(19860, 0)
    OP_6C(71000, 0)
    OP_6E(305, 0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    SetMapFlags(0x2000000)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    Sleep(400)

    def lambda_1BD3():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_1BD3)

    def lambda_1BEE():
        OP_8F(0xFE, 0xFFFFD8F0, 0xFA0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_1BEE)
    FadeToBright(100, 0)
    OP_0D()
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_AE(0x1388)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_8_19BD end

    def Function_9_1C2F(): pass

    label("Function_9_1C2F")

    EventBegin(0x0)
    OP_6D(-105420, 5550, -91410, 0)
    OP_67(0, 6080, -10000, 0)
    OP_6B(3470, 0)
    OP_6C(45000, 0)
    OP_6E(283, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x1, 0x3C)
    OP_71(0x1, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0xF, -99500, 0, -91500, 270)
    SetChrPos(0x10, -99500, 0, -91500, 270)
    FadeToBright(1000, 0)

    def lambda_1CEE():
        OP_6D(-95530, 5550, -92450, 5000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_1CEE)

    def lambda_1D06():
        OP_67(0, 6080, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1D06)
    Sleep(1000)
    OP_22(0x6A, 0x0, 0x64)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x3C)
    OP_73(0x1)
    OP_43(0x102, 0x1, 0x0, 0xA)
    Sleep(1700)
    SetChrFlags(0xA, 0x4)
    SetChrBattleFlags(0xA, 0x20)
    SetChrPos(0xA, -99420, 5550, -90790, 180)
    ClearChrFlags(0xA, 0x80)
    SetChrFlags(0xA, 0x40)
    SetChrChipByIndex(0xA, 7)
    OP_8E(0xA, 0xFFFE7BE0, 0x15AE, 0xFFFE9152, 0xFA0, 0x0)
    OP_8E(0xA, 0xFFFE86D0, 0x15AE, 0xFFFE9382, 0xFA0, 0x0)
    SetChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 6)
    SetChrSubChip(0xA, 1)
    WaitChrThread(0x102, 0x2)
    WaitChrThread(0x102, 0x3)

    ChrTalk(    #38
        0x102,
        "#1034F#7PEr...\x02",
    )

    CloseMessageWindow()

    def lambda_1DC4():
        OP_6B(2900, 12000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_1DC4)

    ChrTalk(    #39
        0xA,
        (
            "#214FEven at the very end, you manage to be\x01",
            "SO UN-CUTE!\x02\x03",

            "What's all this 'thank you' business with a face\x01",
            "like you're walking to your execution?!\x02\x03",

            "#215FYou think hearing that'll make me happy?!\x02\x03",

            "You think...those are the words I want\x01",
            "to hear?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x102,
        "#1033F#7PJosette...\x02",
    )

    CloseMessageWindow()
    Fade(250)
    SetChrSubChip(0xA, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #41
        0xA,
        (
            "#413F...Just, promise me.\x02\x03",

            "That you won't do anything too crazy.\x02\x03",

            "That you'll come back alive...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x102,
        (
            "#1033F#7P...\x02\x03",

            "#1035FGiven who I'm about to pick a war with,\x01",
            "I can't guarantee anything.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0xA,
        "#417FBut...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x102,
        (
            "#1031F#7PBut...I will promise this.\x02\x03",

            "Even if I don't succeed at my goal...\x02\x03",

            "#1053FI will come back alive and give you\x01",
            "all my thanks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0xA,
        "#414FAh...!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x3)
    Fade(250)
    SetChrSubChip(0xA, 1)
    OP_0D()

    def lambda_2074():
        OP_6D(-95030, 5550, -92450, 1500)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2074)
    OP_8E(0x102, 0xFFFE89B4, 0x15AE, 0xFFFE9404, 0x1F4, 0x0)
    Sleep(500)
    OP_8C(0x102, 270, 400)
    Sleep(500)

    ChrTalk(    #46
        0x102,
        "#1031F#4PWill that be enough?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0xA,
        "#416F#3PYeah...\x02",
    )

    CloseMessageWindow()
    Fade(500)
    ClearChrFlags(0xA, 0x2)
    SetChrChipByIndex(0xA, 1)
    SetChrSubChip(0xA, 0)
    TurnDirection(0xA, 0x102, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #48
        0xA,
        (
            "#415F#3PDon't forget!\x01",
            "I collect on my promises, buster!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_DB()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    SetChrFlags(0x102, 0x80)
    SetChrFlags(0xA, 0x80)
    OP_22(0x79, 0x1, 0x5A)
    OP_6D(-1880, 5550, -1900, 0)
    OP_67(0, 1380, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(66000, 0)
    OP_6E(861, 0)
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 150000, 6000, 150000, 270)
    SetChrPos(0xE, 150000, 6000, 150000, 270)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x1E)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x1E)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 180000, 0, 0)
    OP_D1(14, 0, 180000, 0, 0)
    OP_43(0xD, 0x0, 0x0, 0xB)
    Sleep(3800)
    OP_1D(0x51)
    FadeToBright(2000, 0)
    Sleep(6000)

    def lambda_2292():
        OP_6D(-19030, 5550, -4550, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2292)

    def lambda_22AA():
        OP_6C(310000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_22AA)
    Sleep(3200)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_9_1C2F end

    def Function_10_22D7(): pass

    label("Function_10_22D7")

    SetChrFlags(0xFE, 0x4)
    SetChrPos(0xFE, -99420, 5550, -90790, 180)
    OP_8E(0xFE, 0xFFFE7BE0, 0x15AE, 0xFFFE9152, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFE88A6, 0x15AE, 0xFFFE93B4, 0x7D0, 0x0)
    Return()

    # Function_10_22D7 end

    def Function_11_2316(): pass

    label("Function_11_2316")


    def lambda_231C():
        OP_D1(254, 0, 230000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_231C)

    def lambda_2336():
        OP_D1(254, 0, 230000, -30000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2336)

    def lambda_2350():
        OP_8F(0xFE, 0x249F0, 0xFA0, 0xC350, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2350)

    def lambda_236B():
        OP_8F(0xFE, 0x249F0, 0xFA0, 0xC350, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_236B)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)
    OP_43(0xD, 0x1, 0x0, 0xC)
    OP_43(0xE, 0x1, 0x0, 0xD)

    def lambda_239E():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_239E)

    def lambda_23B8():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_23B8)

    def lambda_23D2():
        OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_23D2)

    def lambda_23EE():
        OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_23EE)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)

    def lambda_2414():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_2414)

    def lambda_242F():
        OP_8F(0xFE, 0xFFFE7960, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 2, lambda_242F)
    WaitChrThread(0xD, 0x2)
    WaitChrThread(0xE, 0x2)
    Return()

    # Function_11_2316 end

    def Function_12_244F(): pass

    label("Function_12_244F")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_2470")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_12_244F")

    label("loc_2470")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_12_244F end

    def Function_13_247C(): pass

    label("Function_13_247C")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_249D")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_13_247C")

    label("loc_249D")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_13_247C end

    def Function_14_24A9(): pass

    label("Function_14_24A9")

    EventBegin(0x0)
    OP_DB()
    LoadEffect(0x1, "map\\mp091_00.eff")
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFEC, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_71(0x1, 0x4)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 50000, 0, 0, 270)
    SetChrPos(0xE, 50000, 0, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 20000, 0, 50000, 270)
    SetChrPos(0x10, 20000, 0, 50000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_6F(0x3, 360)
    OP_6F(0x4, 360)
    OP_6D(-36160, -10000, -5660, 0)
    OP_67(0, 4150, -10000, 0)
    OP_6B(4740, 0)
    OP_6C(252000, 0)
    OP_6E(1357, 0)
    OP_D0(10000, 0)
    FadeToBright(1000, 0)

    def lambda_2645():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 0, lambda_2645)

    def lambda_2660():
        OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 0, lambda_2660)
    Sleep(4000)
    OP_43(0xF, 0x0, 0x0, 0x19)
    OP_43(0x10, 0x0, 0x0, 0x1A)
    Sleep(9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(31120, -9250, -10030, 0)
    OP_67(0, 3530, -10000, 0)
    OP_6B(4740, 0)
    OP_6C(96000, 0)
    OP_6E(1357, 0)
    OP_D0(340000, 0)
    OP_44(0xD, 0x0)
    OP_44(0xF, 0x0)
    OP_44(0xE, 0x0)
    OP_44(0x10, 0x0)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    SetChrPos(0xF, 60000, 7000, -30000, 270)
    SetChrPos(0x10, 60000, 7000, -30000, 270)
    OP_D1(15, 0, 290000, -25000, 0)
    OP_D1(16, 0, 290000, -25000, 0)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 360)
    OP_70(0x4, 0x1CC)
    OP_43(0xF, 0x0, 0x0, 0x1B)
    OP_43(0x10, 0x0, 0x0, 0x1C)
    FadeToBright(1000, 0)
    Sleep(4500)

    def lambda_27A0():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27A0)

    def lambda_27BB():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_27BB)
    Sleep(100)

    def lambda_27DB():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_27DB)

    def lambda_27F6():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_27F6)
    Sleep(100)

    def lambda_2816():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2816)

    def lambda_2831():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2831)
    Sleep(100)

    def lambda_2851():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2851)

    def lambda_286C():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_286C)
    Sleep(100)

    def lambda_288C():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_288C)

    def lambda_28A7():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_28A7)
    Sleep(100)

    def lambda_28C7():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_28C7)

    def lambda_28E2():
        OP_8F(0xFE, 0xFFFE7960, 0x3E8, 0xFFFF7B30, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_28E2)
    Sleep(4000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x102, 0xFF)
    OP_6D(-49540, -6000, 10420, 0)
    OP_6C(337000, 0)
    OP_67(0, 2080, -10000, 0)
    OP_6E(1357, 0)
    OP_6B(4740, 0)
    OP_D0(370000, 0)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)
    OP_44(0xF, 0x0)
    OP_44(0xF, 0x1)
    OP_44(0x10, 0x0)
    OP_44(0x10, 0x1)
    SetChrPos(0xD, 0, -1000, 0, 270)
    SetChrPos(0xE, 0, -1000, 0, 270)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 40000, 4000, 30000, 270)
    SetChrPos(0x10, 40000, 4000, 30000, 270)
    OP_D1(15, 0, 260000, 0, 0)
    OP_D1(16, 0, 260000, 0, 0)
    OP_43(0xD, 0x0, 0x0, 0x15)
    OP_43(0xE, 0x0, 0x0, 0x16)
    OP_43(0xF, 0x0, 0x0, 0x1D)
    OP_43(0x10, 0x0, 0x0, 0x1E)
    Sleep(300)
    FadeToBright(1000, 0)
    Sleep(4700)

    def lambda_2A36():
        OP_6D(-76150, -4350, -6420, 4400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2A36)

    def lambda_2A4E():
        OP_6C(224000, 4400)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2A4E)

    def lambda_2A5E():
        OP_D0(350000, 4400)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_2A5E)

    def lambda_2A6E():
        OP_D1(254, 0, 270000, -15000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2A6E)

    def lambda_2A88():
        OP_D1(254, 0, 270000, -15000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2A88)

    def lambda_2AA2():
        OP_D1(254, 0, 270000, -45000, 6000)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2AA2)

    def lambda_2ABC():
        OP_D1(254, 0, 270000, -45000, 6000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2ABC)
    WaitChrThread(0x102, 0x0)
    OP_44(0xD, 0x0)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x0)
    OP_44(0xE, 0x1)

    def lambda_2AEB():
        OP_D1(254, 0, 270000, -45000, 3000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_2AEB)

    def lambda_2B05():
        OP_D1(254, 0, 270000, -45000, 3000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_2B05)
    Sleep(100)

    def lambda_2B24():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2B24)

    def lambda_2B3F():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B3F)
    Sleep(100)

    def lambda_2B5F():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2B5F)

    def lambda_2B7A():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2B7A)
    Sleep(100)

    def lambda_2B9A():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2B9A)

    def lambda_2BB5():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2BB5)
    Sleep(100)

    def lambda_2BD5():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2BD5)

    def lambda_2BF0():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2BF0)
    Sleep(100)

    def lambda_2C10():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C10)

    def lambda_2C2B():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C2B)
    Sleep(100)

    def lambda_2C4B():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C4B)

    def lambda_2C66():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x3E80, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2C66)
    Sleep(100)

    def lambda_2C86():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_2C86)

    def lambda_2CA1():
        OP_8F(0xFE, 0xFFFD19D0, 0xFA0, 0x13880, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_2CA1)
    Sleep(2000)
    OP_44(0xD, 0x1)
    OP_44(0xD, 0x3)
    OP_44(0xE, 0x1)
    OP_44(0xE, 0x3)
    SetChrPos(0xD, -200000, -2000, 110000, 270)
    SetChrPos(0xE, -200000, -2000, 110000, 270)
    OP_D1(13, 0, 270000, 10000, 0)
    OP_D1(14, 0, 270000, 10000, 0)
    Sleep(2000)
    Fade(1000)
    OP_6D(-223070, -10000, 89110, 0)
    OP_67(0, 4680, -10000, 0)
    OP_6C(273000, 0)
    OP_D0(370000, 0)
    OP_0D()
    OP_43(0x102, 0x0, 0x0, 0xF)
    WaitChrThread(0xF, 0x0)
    WaitChrThread(0xF, 0x1)
    OP_44(0x102, 0x0)
    OP_89(0x102, -187360, 5630, 81990, 316)
    Fade(1000)
    OP_6D(-187360, 5630, 81990, 0)
    OP_67(0, 3240, -10000, 0)
    OP_6B(2300, 0)
    OP_6C(174000, 0)
    OP_6E(429, 0)
    OP_D0(360000, 0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #49
        0x102,
        "#1035F#6P#40W...\x02",
    )

    CloseMessageWindow()
    Sleep(100)
    Fade(500)
    OP_6B(2000, 500)
    OP_0D()

    ChrTalk(    #50
        0x102,
        "#1032F#6PNow!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_DB()

    def lambda_2E36():
        OP_6D(-192600, 5630, 84510, 2000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_2E36)

    def lambda_2E4E():
        OP_67(0, 2960, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_2E4E)

    def lambda_2E66():
        OP_6C(248000, 2000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_2E66)

    def lambda_2E76():
        OP_6B(2800, 2000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_2E76)
    WaitChrThread(0xA, 0x0)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 0)
    SetChrFlags(0x102, 0x40)
    SetChrFlags(0x102, 0x2)

    def lambda_2E9F():
        OP_99(0xFE, 0x0, 0x7, 0x3E8)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2E9F)
    OP_8E(0x102, 0xFFFD189A, 0x15FE, 0x14230, 0x2710, 0x0)
    OP_44(0x102, 0x1)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 8)
    Sleep(200)
    OP_7D(0x0, 0x102, 0x32, 0x1F4)
    OP_22(0xA3, 0x0, 0x64)
    SetChrFlags(0x102, 0x4)

    def lambda_2EE8():
        OP_99(0xFE, 0x8, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2EE8)

    def lambda_2EF8():
        OP_96(0xFE, 0xFFFD0FF8, 0x14D2, 0x151C6, 0x4E2, 0x1388)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2EF8)
    OP_22(0xA3, 0x0, 0x64)
    WaitChrThread(0x102, 0x1)

    def lambda_2F20():
        OP_99(0xFE, 0x10, 0x12, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2F20)
    WaitChrThread(0x102, 0x0)
    WaitChrThread(0x102, 0x1)
    OP_22(0xA4, 0x0, 0x64)

    def lambda_2F3F():
        OP_D1(254, 0, 270000, -4000, 100)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2F3F)

    def lambda_2F59():
        OP_D1(254, 0, 270000, -4000, 100)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2F59)
    SetChrPos(0x102, -193320, 5330, 86470, 316)
    SetChrChipByIndex(0x102, 26)
    SetChrSubChip(0x102, 8)
    Sleep(100)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_2F98():
        OP_D1(254, 0, 270000, 2000, 400)
        ExitThread()

    QueueWorkItem(0xF, 3, lambda_2F98)

    def lambda_2FB2():
        OP_D1(254, 0, 270000, 2000, 400)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_2FB2)

    def lambda_2FCC():
        OP_99(0xFE, 0x9, 0xA, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_2FCC)

    def lambda_2FDC():
        OP_96(0xFE, 0xFFFCD966, 0xDCA, 0x1AB62, 0xBB8, 0x7D0)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_2FDC)
    FadeToDark(1000, 0, -1)
    OP_0D()
    ClearMapFlags(0x10)
    OP_44(0x102, 0x0)
    OP_44(0x102, 0x1)
    OP_44(0x102, 0x2)
    OP_44(0x102, 0x3)
    ClearChrBattleFlags(0x102, 0x20)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_44(0xD, 0x1)
    OP_44(0xE, 0x1)
    SetChrPos(0xD, 136000, 1000, 50000, 270)
    SetChrPos(0xE, 136000, 1000, 50000, 270)
    OP_D1(13, 0, 260000, 10000, 0)
    OP_D1(14, 0, 260000, 10000, 0)
    SetChrPos(0x102, 0, 5000, 0, 270)
    SetChrPos(0x19, -350, 5900, 0, 270)
    ClearChrFlags(0x19, 0x80)
    SetChrPos(0x1A, -24650, 5900, 0, 270)
    ClearChrFlags(0x1A, 0x80)
    OP_6D(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(1500, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)
    FadeToBright(1000, 0)
    OP_43(0x102, 0x0, 0x0, 0x12)

    def lambda_310B():
        OP_9E(0xFE, 0xA, 0xA, 0x1388, 0xBB8)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_310B)

    def lambda_3125():
        OP_6B(3260, 3750)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_3125)

    def lambda_3135():
        OP_6D(-10900, 5000, -1600, 3750)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3135)

    def lambda_314D():
        OP_67(0, 2040, -10000, 3750)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_314D)

    def lambda_3165():
        OP_6C(246000, 3750)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_3165)

    def lambda_3175():
        OP_8F(0xFE, 0xFFFA7220, 0x3E8, 0xFFFE7960, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3175)

    def lambda_3190():
        OP_8F(0xFE, 0xFFFA7220, 0x3E8, 0xFFFE7960, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_3190)
    Sleep(2500)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(2000)
    OP_82(0x1, 0x0)
    Fade(500)
    OP_22(0xD6, 0x0, 0x64)
    OP_44(0x102, 0xFF)
    ClearChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x8000)
    SetChrChipByIndex(0x102, 25)
    SetChrSubChip(0x102, 0)
    OP_8C(0x102, 270, 0)
    OP_7D(0x1, 0x102, 0x0, 0x0)
    SetChrPos(0x19, 100000, 0, 0, 270)
    SetChrPos(0x1A, 101000, 0, 0, 270)
    OP_43(0x102, 0x0, 0x0, 0x11)
    PlayEffect(0x1, 0x1, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    OP_D1(13, 0, 270000, 10000, 0)
    OP_D1(14, 0, 270000, 10000, 0)
    SetChrPos(0xD, 40000, 1000, 0, 270)
    SetChrPos(0xE, 40000, 1000, 0, 270)
    OP_6D(-500, 6100, 0, 0)
    OP_67(0, 2960, -10000, 0)
    OP_6B(2100, 0)
    OP_6C(225000, 0)
    OP_6E(430, 0)

    def lambda_32D5():
        OP_8F(0xFE, 0xFFF9E580, 0x3E8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_32D5)

    def lambda_32F0():
        OP_8F(0xFE, 0xFFF9E580, 0x3E8, 0x0, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_32F0)

    def lambda_330B():
        OP_6D(2880, 10000, 6720, 4000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_330B)

    def lambda_3323():
        OP_67(0, 1320, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_3323)

    def lambda_333B():
        OP_6C(268000, 4500)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_333B)
    Sleep(15)
    WaitChrThread(0xA, 0x2)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0x102, 0x8000)
    OP_82(0x1, 0x0)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    OP_DC()
    SetMapFlags(0x2000000)
    SetMapFlags(0x10)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/E0110   ._SN", 104, 0, 0)
    IdleLoop()
    Return()

    # Function_14_24A9 end

    def Function_15_338D(): pass

    label("Function_15_338D")

    SetChrChipByIndex(0x102, 5)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x102, 0x1000)
    SetChrBattleFlags(0x102, 0x20)
    OP_8C(0x102, 316, 0)

    label("loc_33AD")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_33EE")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA50), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x2), scpexpr(EXPR_PUSH_LONG, 0x15FE), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xF, 0x3), scpexpr(EXPR_PUSH_LONG, 0x7C6), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("loc_33AD")

    label("loc_33EE")

    Return()

    # Function_15_338D end

    def Function_16_33EF(): pass

    label("Function_16_33EF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_3430")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC1C), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x988), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0xBCC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_16_33EF")

    label("loc_3430")

    Return()

    # Function_16_33EF end

    def Function_17_3431(): pass

    label("Function_17_3431")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_34D2")
    OP_51(0x102, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x9C4), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x102, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3E8), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x19, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x1, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x1), scpexpr(EXPR_PUSH_LONG, 0xBB8), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x2, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_ADD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1A, 0x3, (scpexpr(EXPR_GET_CHR_WORK, 0xD, 0x3), scpexpr(EXPR_PUSH_LONG, 0x5DC), scpexpr(EXPR_SUB), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_17_3431")

    label("loc_34D2")

    Return()

    # Function_17_3431 end

    def Function_18_34D3(): pass

    label("Function_18_34D3")

    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    OP_99(0x102, 0x14, 0x17, 0x7D0)
    SetChrSubChip(0x102, 12)
    Sleep(200)
    OP_22(0x84, 0x0, 0x64)
    SetChrSubChip(0x102, 13)
    PlayEffect(0x1, 0x1, 0x19, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0x1A, 0, 0, 0, 0)
    Sleep(80)
    SetChrSubChip(0x102, 14)
    OP_7D(0x0, 0x102, 0x32, 0xC8)
    Return()

    # Function_18_34D3 end

    def Function_19_3592(): pass

    label("Function_19_3592")

    Sleep(500)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0xFFFFEC78, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFD8F0, 0x82C8, 0x4650, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0xFFFFEC78, 0x30C0, 0x3E80, 0x0)
    OP_8F(0xFE, 0xFFFCF220, 0x7D0, 0x5C8, 0x36B0, 0x0)
    Return()

    # Function_19_3592 end

    def Function_20_35FC(): pass

    label("Function_20_35FC")

    Sleep(500)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0xFFFFEC78, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFD8F0, 0x82C8, 0x4650, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0xFFFFEC78, 0x30C0, 0x3E80, 0x0)
    OP_8F(0xFE, 0xFFFCF220, 0x7D0, 0x5C8, 0x36B0, 0x0)
    Return()

    # Function_20_35FC end

    def Function_21_3666(): pass

    label("Function_21_3666")


    def lambda_366C():
        OP_D1(254, 0, 270000, 60000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_366C)

    def lambda_3686():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3686)
    Sleep(400)

    def lambda_36A7():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36A7)
    Sleep(300)

    def lambda_36C8():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36C8)
    Sleep(200)

    def lambda_36E9():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_36E9)
    Sleep(100)

    def lambda_370A():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_370A)
    Sleep(4600)

    def lambda_372B():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_372B)
    Sleep(300)

    def lambda_374C():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_374C)
    Sleep(200)

    def lambda_376D():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_376D)
    Sleep(100)

    def lambda_378E():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_378E)
    Return()

    # Function_21_3666 end

    def Function_22_37A5(): pass

    label("Function_22_37A5")


    def lambda_37AB():
        OP_D1(254, 0, 270000, 60000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_37AB)

    def lambda_37C5():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37C5)
    Sleep(400)

    def lambda_37E6():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_37E6)
    Sleep(300)

    def lambda_3807():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3807)
    Sleep(200)

    def lambda_3828():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3828)
    Sleep(100)

    def lambda_3849():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3849)
    Sleep(4600)

    def lambda_386A():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_386A)
    Sleep(300)

    def lambda_388B():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_388B)
    Sleep(200)

    def lambda_38AC():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38AC)
    Sleep(100)

    def lambda_38CD():
        OP_97(0xFE, 0xFFFF63C0, 0x0, 0xFFFD40E0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_38CD)
    Return()

    # Function_22_37A5 end

    def Function_23_38E4(): pass

    label("Function_23_38E4")

    OP_8F(0xFE, 0x5EEC, 0x0, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0x0, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFEC78, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0x0, 0x4060, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD05A8, 0xFFFFD120, 0xD98, 0x4E20, 0x0)
    Return()

    # Function_23_38E4 end

    def Function_24_395D(): pass

    label("Function_24_395D")

    OP_8F(0xFE, 0x5EEC, 0x0, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFF5380, 0x0, 0x55AA, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFEC6E0, 0x0, 0x690, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFE2AA0, 0xFFFFEC78, 0x82C8, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD8E60, 0x0, 0x4060, 0x4E20, 0x0)
    OP_8F(0xFE, 0xFFFD05A8, 0xFFFFD120, 0xD98, 0x4E20, 0x0)
    Return()

    # Function_24_395D end

    def Function_25_39D6(): pass

    label("Function_25_39D6")

    OP_8F(0xFE, 0x0, 0x0, 0x4E20, 0x36B0, 0x0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFE2B40, 0x0, 0x0)

    def lambda_3A10():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3A10)

    def lambda_3A20():
        OP_D1(254, 0, 270000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3A20)
    WaitChrThread(0xFE, 0x3)

    def lambda_3A3F():
        OP_D1(254, 0, 270000, -25000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3A3F)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x4E20, 0x36B0, 0x0)
    Return()

    # Function_25_39D6 end

    def Function_26_3A6D(): pass

    label("Function_26_3A6D")

    OP_8F(0xFE, 0x0, 0x0, 0x4E20, 0x36B0, 0x0)
    OP_98(0x0, 0xFE)
    OP_98(0x1, 0xFFFF63C0, 0x0, 0xFFFF63C0)
    OP_98(0x1, 0xFFFE2B40, 0x0, 0x0)

    def lambda_3AA7():
        OP_98(0x2, 0xFE, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3AA7)

    def lambda_3AB7():
        OP_D1(254, 0, 270000, 15000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3AB7)
    WaitChrThread(0xF, 0x3)

    def lambda_3AD6():
        OP_D1(254, 0, 270000, -25000, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3AD6)
    WaitChrThread(0xFE, 0x1)
    OP_8F(0xFE, 0xFFFB6C20, 0x0, 0x4E20, 0x36B0, 0x0)
    Return()

    # Function_26_3A6D end

    def Function_27_3B04(): pass

    label("Function_27_3B04")

    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x88B8, 0xBB8, 0xFFFFB1E0)
    OP_98(0x1, 0x7530, 0x3E8, 0x5DC0)

    def lambda_3B2A():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3B2A)
    Sleep(2000)

    def lambda_3B3F():
        OP_D1(254, 6000, 240000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B3F)

    def lambda_3B59():
        OP_6D(29550, -10000, -1500, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3B59)

    def lambda_3B71():
        OP_D0(370000, 5000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_3B71)
    WaitChrThread(0xFE, 0x3)
    OP_44(0xFE, 0x1)

    def lambda_3B8A():
        OP_D1(254, 6000, 240000, 45000, 2500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3B8A)

    def lambda_3BA4():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BA4)
    Sleep(100)

    def lambda_3BC4():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BC4)
    Sleep(100)

    def lambda_3BE4():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3BE4)
    Sleep(100)

    def lambda_3C04():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C04)
    Sleep(100)

    def lambda_3C24():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C24)
    Return()

    # Function_27_3B04 end

    def Function_28_3C3A(): pass

    label("Function_28_3C3A")

    OP_98(0x0, 0xFE)
    OP_98(0x1, 0x88B8, 0xBB8, 0xFFFFB1E0)
    OP_98(0x1, 0x7530, 0x3E8, 0x5DC0)

    def lambda_3C60():
        OP_98(0x2, 0xFE, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3C60)
    Sleep(2000)

    def lambda_3C75():
        OP_D1(254, 6000, 240000, 25000, 5000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C75)
    WaitChrThread(0xFE, 0x3)
    OP_44(0xFE, 0x1)

    def lambda_3C98():
        OP_D1(254, 6000, 240000, 45000, 2500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3C98)

    def lambda_3CB2():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2AF8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CB2)
    Sleep(100)

    def lambda_3CD2():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CD2)
    Sleep(100)

    def lambda_3CF2():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x3A98, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3CF2)
    Sleep(100)

    def lambda_3D12():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x4E20, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D12)
    Sleep(100)

    def lambda_3D32():
        OP_8F(0xFE, 0xFFFE7960, 0x2328, 0xFFFF5FD8, 0x6D60, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D32)
    Return()

    # Function_28_3C3A end

    def Function_29_3D48(): pass

    label("Function_29_3D48")


    def lambda_3D4E():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D4E)
    Sleep(400)

    def lambda_3D6F():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D6F)
    Sleep(300)

    def lambda_3D90():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3D90)
    Sleep(200)

    def lambda_3DB1():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DB1)
    Sleep(100)

    def lambda_3DD2():
        OP_D1(254, 0, 270000, 60000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3DD2)

    def lambda_3DEC():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3DEC)
    Sleep(7500)

    def lambda_3E0D():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E0D)
    Sleep(200)

    def lambda_3E2E():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E2E)
    Sleep(200)

    def lambda_3E4F():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E4F)
    Sleep(2000)

    def lambda_3E70():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_3E70)

    def lambda_3E8A():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x35E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3E8A)
    Sleep(100)

    def lambda_3EAA():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x39D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EAA)
    Sleep(100)

    def lambda_3ECA():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x41A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3ECA)
    Sleep(100)

    def lambda_3EEA():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x4970, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3EEA)
    Sleep(100)

    def lambda_3F0A():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x5528, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F0A)
    Sleep(100)

    def lambda_3F2A():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F2A)
    Sleep(4600)

    def lambda_3F4A():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 1, lambda_3F4A)

    def lambda_3F65():
        OP_8F(0xFE, 0xFFFD19D0, 0xFFFFF830, 0x186A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_3F65)
    Return()

    # Function_29_3D48 end

    def Function_30_3F7B(): pass

    label("Function_30_3F7B")


    def lambda_3F81():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3F81)
    Sleep(400)

    def lambda_3FA2():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0xFA0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FA2)
    Sleep(300)

    def lambda_3FC3():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FC3)
    Sleep(200)

    def lambda_3FE4():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_3FE4)
    Sleep(100)

    def lambda_4005():
        OP_D1(254, 0, 270000, 60000, 6000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_4005)

    def lambda_401F():
        OP_97(0xFE, 0xFFFFD8F0, 0x4E20, 0xFFFC0860, 0x55F0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_401F)
    Sleep(7500)

    def lambda_4040():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4040)
    Sleep(200)

    def lambda_4061():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4061)
    Sleep(200)

    def lambda_4082():
        OP_97(0xFE, 0xFFFEEE90, 0x0, 0x2BF20, 0x2EE0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4082)
    Sleep(2000)

    def lambda_40A3():
        OP_D1(254, 0, 270000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_40A3)

    def lambda_40BD():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x35E8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40BD)
    Sleep(100)

    def lambda_40DD():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x39D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40DD)
    Sleep(100)

    def lambda_40FD():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x41A0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_40FD)
    Sleep(100)

    def lambda_411D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x4970, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_411D)
    Sleep(100)

    def lambda_413D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x5528, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_413D)
    Sleep(100)

    def lambda_415D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x61A8, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_415D)
    Sleep(4600)

    def lambda_417D():
        OP_8F(0xFE, 0xFFFD19D0, 0x0, 0x13880, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_417D)

    def lambda_4198():
        OP_8F(0xFE, 0xFFFD19D0, 0xFFFFF830, 0x186A0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4198)
    Return()

    # Function_30_3F7B end

    def Function_31_41AE(): pass

    label("Function_31_41AE")

    EventBegin(0x0)
    OP_DB()
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF1, 0x0, 0x0, 0x0, 0x0)
    SetChrFlags(0x102, 0x80)
    OP_72(0x4, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    OP_A1(0xF, 0x3)
    OP_A1(0x10, 0x4)
    SetChrPos(0xD, 0, 3000, 0, 270)
    SetChrPos(0xE, 0, 3000, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    SetChrPos(0xF, 110000, 4000, -20000, 270)
    SetChrPos(0x10, 110000, 4000, -20000, 270)
    ClearChrFlags(0xF, 0x100)
    ClearChrFlags(0x10, 0x100)
    OP_D1(15, 0, 270000, 0, 0)
    OP_D1(16, 0, 270000, 0, 0)
    OP_71(0x1, 0x4)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    OP_71(0x3, 0x20)
    OP_6F(0x3, 360)
    OP_70(0x3, 0x1CC)
    OP_71(0x4, 0x20)
    OP_6F(0x4, 360)
    OP_70(0x4, 0x1CC)
    OP_6D(42110, -10000, -9480, 0)
    OP_67(0, 3620, -10000, 0)
    OP_6B(7610, 0)
    OP_6C(105000, 0)
    OP_6E(1076, 0)
    OP_D0(370000, 0)
    FadeToBright(1000, 0)

    def lambda_434F():
        OP_8F(0xFE, 0x186A0, 0xFA0, 0xFFFFB1E0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xF, 0, lambda_434F)

    def lambda_436A():
        OP_8F(0xFE, 0x186A0, 0xFA0, 0xFFFFB1E0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_436A)
    WaitChrThread(0xF, 0x0)

    def lambda_438A():
        OP_6D(21040, -10000, 44720, 4000)
        ExitThread()

    QueueWorkItem(0xA, 0, lambda_438A)

    def lambda_43A2():
        OP_67(0, 3620, -10000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 1, lambda_43A2)

    def lambda_43BA():
        OP_6C(24000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 2, lambda_43BA)

    def lambda_43CA():
        OP_D0(360000, 4000)
        ExitThread()

    QueueWorkItem(0xA, 3, lambda_43CA)
    OP_43(0xF, 0x0, 0x0, 0x20)
    OP_43(0x10, 0x0, 0x0, 0x21)
    OP_43(0xF, 0x1, 0x0, 0x22)
    OP_43(0x10, 0x1, 0x0, 0x23)
    StopSound(0x186A0, 0x493E0, 0x2710)
    Sleep(1000)

    def lambda_4408():
        OP_D1(254, 0, 260000, 30000, 2400)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4408)

    def lambda_4422():
        OP_D1(254, 0, 260000, 30000, 2400)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_4422)
    WaitChrThread(0xD, 0x3)

    def lambda_4441():
        OP_D1(254, 0, 270000, 15000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 3, lambda_4441)

    def lambda_445B():
        OP_D1(254, 0, 270000, 15000, 5000)
        ExitThread()

    QueueWorkItem(0xE, 3, lambda_445B)

    def lambda_4475():
        OP_6B(9610, 5000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_4475)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0610   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_31_41AE end

    def Function_32_44A7(): pass

    label("Function_32_44A7")


    def lambda_44AD():
        OP_D1(254, 0, 290000, -40000, 3500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_44AD)
    OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)

    def lambda_44DC():
        OP_D1(254, 0, 310000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_44DC)
    OP_8F(0xFE, 0xFFFFB1E0, 0x4E20, 0x493E0, 0x5DC0, 0x0)
    Return()

    # Function_32_44A7 end

    def Function_33_4505(): pass

    label("Function_33_4505")


    def lambda_450B():
        OP_D1(254, 0, 290000, -40000, 3500)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_450B)
    OP_97(0xFE, 0x186A0, 0xC350, 0x15F90, 0x5DC0, 0x0)

    def lambda_453A():
        OP_D1(254, 0, 310000, 0, 4000)
        ExitThread()

    QueueWorkItem(0xFE, 3, lambda_453A)
    OP_8F(0xFE, 0xFFFFB1E0, 0x4E20, 0x493E0, 0x5DC0, 0x0)
    Return()

    # Function_33_4505 end

    def Function_34_4563(): pass

    label("Function_34_4563")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_4584")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_34_4563")

    label("loc_4584")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_34_4563 end

    def Function_35_4590(): pass

    label("Function_35_4590")

    Jc((scpexpr(EXPR_GET_CHR_WORK, 0xFE, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_GTR), scpexpr(EXPR_END)), "loc_45B1")
    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))
    Sleep(15)
    Jump("Function_35_4590")

    label("loc_45B1")

    OP_51(0xFE, 0x2, (scpexpr(EXPR_PUSH_LONG, 0x7D0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_35_4590 end

    def Function_36_45BD(): pass

    label("Function_36_45BD")

    EventBegin(0x0)
    OP_DB()
    OP_71(0x1, 0x4)
    OP_72(0x0, 0x4)
    SetChrFlags(0x102, 0x4)
    SetChrPos(0x102, 6180, 15930, 17690, 0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_A1(0xD, 0x2)
    SetChrPos(0xD, 4780, 14000, 10550, 45)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 700)
    OP_70(0x2, 0x30C)
    OP_6D(6550, 15930, 18080, 0)
    OP_67(0, 6750, -10000, 0)
    OP_6B(2780, 0)
    OP_6C(124000, 0)
    OP_6E(438, 0)
    FadeToBright(1000, 0)

    def lambda_4664():
        OP_6D(7530, 15930, 13960, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4664)

    def lambda_467C():
        OP_67(0, 6750, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_467C)
    OP_6E(778, 4000)

    def lambda_469D():
        OP_6D(-53670, 15930, -95210, 10000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_469D)

    def lambda_46B5():
        OP_67(0, 5450, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_46B5)

    def lambda_46CD():
        OP_6B(4780, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_46CD)

    def lambda_46DD():
        OP_6C(67000, 5000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_46DD)

    def lambda_46ED():
        OP_6E(834, 10000)
        ExitThread()

    QueueWorkItem(0xD, 2, lambda_46ED)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_DC()
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_36_45BD end

    def Function_37_4728(): pass

    label("Function_37_4728")

    EventBegin(0x0)
    OP_DB()
    OP_11(0x38, 0x44, 0x58, 0x186A0, 0x7A120, 0x0)
    OP_76(0x6, 0x0, 0x1, 0xFFFFFFF6, 0x0, 0x0, 0x0, 0x0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_72(0x5, 0x4)
    OP_A1(0xD, 0x2)
    OP_A1(0xE, 0x5)
    SetChrPos(0xD, 0, 0, 0, 270)
    SetChrPos(0xE, 0, 0, 0, 270)
    ClearChrFlags(0xD, 0x100)
    ClearChrFlags(0xE, 0x100)
    OP_D1(13, 0, 270000, 0, 0)
    OP_D1(14, 0, 270000, 0, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x2, 0x20)
    OP_B0(0x2, 0x28)
    OP_6F(0x2, 800)
    OP_70(0x2, 0x384)
    OP_71(0x5, 0x20)
    OP_B0(0x5, 0x28)
    OP_6F(0x5, 800)
    OP_70(0x5, 0x384)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 6)
    ClearChrFlags(0x102, 0x80)
    ClearChrFlags(0x102, 0x1)
    SetChrFlags(0x102, 0x2)
    SetChrFlags(0x102, 0x1000)
    SetChrBattleFlags(0x102, 0x20)
    SetChrPos(0x102, 810, 3380, -2950, 180)
    OP_6D(-6990, 3340, -40, 0)
    OP_67(0, 1430, -10000, 0)
    OP_6B(2760, 0)
    OP_6C(100000, 0)
    OP_6E(438, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)

    def lambda_487B():
        OP_6D(-7310, 3340, 410, 8000)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_487B)

    def lambda_4893():
        OP_6C(300000, 8000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_4893)

    def lambda_48A3():
        OP_6B(2260, 8000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_48A3)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 1)
    WaitChrThread(0x102, 0x0)
    Sleep(1000)
    OP_43(0xD, 0x0, 0x0, 0x26)

    def lambda_48DD():
        OP_6C(280000, 4000)
        ExitThread()

    QueueWorkItem(0x102, 1, lambda_48DD)
    Sleep(3000)
    SetChrChipByIndex(0x102, 5)
    SetChrSubChip(0x102, 2)
    Sleep(2000)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F2)
    NewScene("ED6_DT21/E0110   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_37_4728 end

    def Function_38_4919(): pass

    label("Function_38_4919")


    def lambda_491F():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_491F)

    def lambda_493A():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_493A)
    Sleep(400)

    def lambda_495A():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_495A)

    def lambda_4975():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4975)
    Sleep(400)

    def lambda_4995():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4995)

    def lambda_49B0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_49B0)
    Sleep(300)

    def lambda_49D0():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_49D0)

    def lambda_49EB():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_49EB)
    Sleep(300)

    def lambda_4A0B():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A0B)

    def lambda_4A26():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A26)
    Sleep(200)

    def lambda_4A46():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A46)

    def lambda_4A61():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A61)
    Sleep(200)

    def lambda_4A81():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4A81)

    def lambda_4A9C():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x36B0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4A9C)
    Sleep(100)

    def lambda_4ABC():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4ABC)

    def lambda_4AD7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x4650, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4AD7)
    Sleep(100)

    def lambda_4AF7():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4AF7)

    def lambda_4B12():
        OP_8F(0xFE, 0xFFFCF2C0, 0x0, 0x0, 0x5DC0, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4B12)
    Return()

    # Function_38_4919 end

    def Function_39_4B28(): pass

    label("Function_39_4B28")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_4B4D")
    Call(0, 54)
    Call(0, 55)
    RemoveParty(0x0, 0xFF)

    label("loc_4B4D")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    OP_6D(220, -15000, 60940, 0)
    OP_67(0, -3800, -10000, 0)
    OP_6B(1220, 0)
    OP_6C(0, 0)
    OP_6E(667, 0)
    OP_71(0x1, 0x4)
    OP_71(0x3, 0x4)
    OP_A1(0xD, 0x2)
    SetChrPos(0xD, -38450, -5000, 63740, 45)
    OP_71(0x2, 0x20)
    OP_6F(0x2, 680)
    OP_70(0x2, 0x30C)
    OP_72(0x5, 0x4)
    OP_A1(0xE, 0x5)
    SetChrPos(0xE, -38450, -5000, 63740, 45)
    OP_71(0x5, 0x20)
    OP_6F(0x5, 680)
    OP_70(0x5, 0x30C)
    OP_22(0x79, 0x1, 0x4B)
    FadeToBright(2000, 0)

    def lambda_4C0E():
        OP_6B(2000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_4C0E)
    OP_43(0xD, 0x0, 0x0, 0x28)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4C69")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Tita")

    AnonymousTalk(    #51 op#A op#5
        "\x07\x00#068F#4S#18AEsteeeeelle...!!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4D9C")

    label("loc_4C69")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CA5")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Kloe")

    AnonymousTalk(    #52 op#A op#5
        "\x07\x00#046F#4S#12AEstelle!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4D9C")

    label("loc_4CA5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CE7")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Scherazade")

    AnonymousTalk(    #53 op#A op#5
        "\x07\x00#024F#4S#18AESTELLE!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4D9C")

    label("loc_4CE7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D25")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Agate")

    AnonymousTalk(    #54 op#A op#5
        "\x07\x00#054F#4S#13AESTELLE!!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4D9C")

    label("loc_4D25")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D64")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Olivier")

    AnonymousTalk(    #55 op#A op#5
        "\x07\x00#530F#4S#10AEstelle!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Jump("loc_4D9C")

    label("loc_4D64")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D9C")
    SetMessageWindowPos(-1, 320, -1, -1)
    SetChrName("Zin")

    AnonymousTalk(    #56 op#A op#5
        "\x07\x00#076F#4S#10AEstelle!\x05\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_4D9C")

    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(500)
    FadeToDark(3000, 0, -1)
    Sleep(300)
    OP_24(0x79, 0x46)
    Sleep(300)
    OP_24(0x79, 0x41)
    Sleep(300)
    OP_24(0x79, 0x3C)
    Sleep(300)
    OP_24(0x79, 0x37)
    Sleep(300)
    OP_24(0x79, 0x32)
    Sleep(300)
    OP_24(0x79, 0x2D)
    Sleep(300)
    OP_24(0x79, 0x28)
    Sleep(300)
    OP_24(0x79, 0x23)
    Sleep(300)
    OP_23(0x79)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(2000)
    OP_DC()
    ClearMapFlags(0x2000000)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/C5400   ._SN", 111, 0, 0)
    IdleLoop()
    Return()

    # Function_39_4B28 end

    def Function_40_4E23(): pass

    label("Function_40_4E23")


    def lambda_4E29():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E29)

    def lambda_4E44():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x7530, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4E44)
    Sleep(500)

    def lambda_4E64():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E64)

    def lambda_4E7F():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x88B8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4E7F)
    Sleep(500)

    def lambda_4E9F():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4E9F)

    def lambda_4EBA():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0x9C40, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4EBA)
    Sleep(500)

    def lambda_4EDA():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4EDA)

    def lambda_4EF5():
        OP_90(0xFE, 0x61A80, 0x186A0, 0x7A120, 0xAFC8, 0x0)
        ExitThread()

    QueueWorkItem(0xE, 1, lambda_4EF5)
    Return()

    # Function_40_4E23 end

    def Function_41_4F0B(): pass

    label("Function_41_4F0B")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_DB()
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_6D(5080, 2500, 55830, 0)
    OP_67(0, 4010, -10000, 0)
    OP_6B(8300, 0)
    OP_6C(47000, 0)
    OP_6E(337, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x1)
    SetChrPos(0xD, 20000, 0, 55000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_B0(0x1, 0x1E)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 330)
    OP_70(0x1, 0x1AE)
    FadeToBright(2000, 0)

    def lambda_4FB9():
        OP_6D(24700, 2500, 55500, 8000)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_4FB9)

    def lambda_4FD1():
        OP_67(0, 8240, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 2, lambda_4FD1)

    def lambda_4FE9():
        OP_6C(317000, 8000)
        ExitThread()

    QueueWorkItem(0x0, 3, lambda_4FE9)

    def lambda_4FF9():
        OP_6E(447, 8000)
        ExitThread()

    QueueWorkItem(0xD, 1, lambda_4FF9)
    Sleep(2000)
    Sleep(2000)
    Sleep(2000)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10FF)
    OP_A2(0x10F0)
    NewScene("ED6_DT21/E0310   ._SN", 106, 0, 0)
    IdleLoop()
    Return()

    # Function_41_4F0B end

    def Function_42_5038(): pass

    label("Function_42_5038")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_6D(16329, 4250, 57660, 0)
    OP_67(0, 8380, -10000, 0)
    OP_6B(5340, 0)
    OP_6C(57000, 0)
    OP_6E(476, 0)
    OP_22(0x1C3, 0x0, 0x64)
    OP_A1(0xD, 0x1)
    SetChrPos(0xD, 20000, 0, 55000, 0)
    OP_22(0x125, 0x1, 0x46)
    OP_B0(0x1, 0x14)
    OP_71(0x1, 0x20)
    OP_6F(0x1, 330)
    OP_70(0x1, 0x1AE)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_6D(22780, 500, 70340, 0)
    OP_67(0, 9440, -10000, 0)
    OP_6B(2620, 0)
    OP_6C(57000, 0)
    OP_6E(375, 0)
    OP_43(0x8, 0x1, 0x0, 0x2C)
    OP_43(0x9, 0x1, 0x0, 0x2D)
    OP_43(0x14, 0x1, 0x0, 0x2E)
    OP_43(0x13, 0x1, 0x0, 0x2F)
    OP_43(0x11, 0x1, 0x0, 0x30)
    OP_43(0x15, 0x1, 0x0, 0x31)
    OP_43(0x16, 0x1, 0x0, 0x32)
    OP_43(0x12, 0x1, 0x0, 0x33)
    OP_43(0x18, 0x1, 0x0, 0x34)
    OP_43(0x17, 0x1, 0x0, 0x35)
    OP_48()
    OP_0D()
    WaitChrThread(0x9, 0x2)
    Sleep(300)
    WaitChrThread(0x8, 0x1)

    ChrTalk(    #57
        0x8,
        "#1002F#6PWh-Where...?!\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x102, 0x1)

    ChrTalk(    #58
        0x9,
        "#1043F#5PBest seen from the foredeck...\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x16, 0x1)
    Sleep(500)
    OP_20(0x7D0)
    OP_62(0x16, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x16, 270, 600)
    Sleep(400)

    ChrTalk(    #59
        0x16,
        "#1069F#2PThere!\x02",
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(200)
    OP_1D(0x82)
    Sleep(500)

    def lambda_5221():
        OP_6D(-23010, 2450, 64140, 5000)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5221)

    def lambda_5239():
        OP_6C(81000, 5000)
        ExitThread()

    QueueWorkItem(0x8, 3, lambda_5239)

    def lambda_5249():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5249)

    def lambda_5257():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_5257)
    Sleep(50)

    def lambda_526A():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_526A)

    def lambda_5278():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x13, 1, lambda_5278)
    Sleep(50)

    def lambda_528B():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_528B)

    def lambda_5299():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x15, 1, lambda_5299)
    Sleep(50)

    def lambda_52AC():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_52AC)

    def lambda_52BA():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_52BA)
    Sleep(50)

    def lambda_52CD():
        OP_8C(0xFE, 270, 600)
        ExitThread()

    QueueWorkItem(0x17, 1, lambda_52CD)
    Sleep(3500)
    OP_43(0x16, 0x3, 0x0, 0x2B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x8, 0x2)
    OP_44(0x8, 0x3)
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    OP_0D()
    SoundLoad(451)
    SoundLoad(879)
    SoundLoad(882)
    SoundLoad(883)
    SoundLoad(880)
    SoundLoad(881)
    PlayMovie(0x0, "ED6_DT41.dat", 0x0, 0x1)

    label("loc_5329")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5343")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5340")
    Jump("loc_5343")

    label("loc_5340")

    Jump("loc_5329")

    label("loc_5343")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    Sleep(2000)
    OP_C4(0x1, 0x10)
    OP_6D(19920, 2450, 67640, 0)
    OP_67(0, 6610, -10000, 0)
    OP_6B(3590, 0)
    OP_6C(129000, 0)
    OP_6E(262, 0)
    LoadEffect(0x1, "map\\mp092_00.eff")
    PlayEffect(0x1, 0xFF, 0xFF, -40000, 8000, 10000, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_C4(0x0, 0x2)
    OP_7E(0x44C, 0xFC72, 0xFF88, 0x6E, 0x1)
    OP_22(0x1C3, 0x0, 0x64)
    OP_22(0x125, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    OP_DC()

    ChrTalk(    #60
        0x8,
        "#1020F#6PWh-Wh-Wh-Wha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#043F#6PThat's... It must be...\x01",
            "That flying city...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x9,
        "#1042F#6PYes, it must be.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x16,
        "#1069F#6PThat's it! That's the Aureole!\x02",
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #64
        0x17,
        "#102F#6P...Hells.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x17, 0x18, 600)
    Sleep(300)

    ChrTalk(    #65
        0x17,
        (
            "#105F#4PCaptain Schwarz!\x01",
            "Land the ship! NOW!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x18, 0x17, 500)
    Sleep(300)

    ChrTalk(    #66
        0x18,
        "#173F#6PPardon, Professor?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x17,
        (
            "#105F#4PYou have emergency orders\x01",
            "from Cassius, right?!\x02\x03",

            "If you don't hurry, it'll be\x01",
            "too late for all of us!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x18,
        "#177F#6P#3SV-Very well!\x02",
    )

    CloseMessageWindow()
    OP_DB()
    OP_43(0x16, 0x3, 0x0, 0x2B)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_C4(0x0, 0x10)
    FadeToBright(1, 0)
    OP_0D()
    SoundLoad(451)
    SoundLoad(886)
    SoundLoad(884)
    SoundLoad(887)
    SoundLoad(888)
    SoundLoad(885)
    PlayMovie(0x0, "ED6_DT42.dat", 0x0, 0x1)

    label("loc_562A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5644")
    Sleep(100)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x2D), scpexpr(EXPR_END)), "loc_5641")
    Jump("loc_5644")

    label("loc_5641")

    Jump("loc_562A")

    label("loc_5644")

    FadeToDark(1000, 0, -1)
    OP_0D()
    PlayMovie(0x1, "", 0x0, 0x0)
    OP_C4(0x1, 0x10)
    OP_DC()
    SetMapFlags(0x2000000)
    OP_A2(0x10F4)
    NewScene("ED6_DT21/C5413   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_42_5038 end

    def Function_43_566F(): pass

    label("Function_43_566F")

    OP_24(0x1C3, 0x5A)
    OP_24(0x125, 0x41)
    Sleep(200)
    OP_24(0x1C3, 0x50)
    OP_24(0x125, 0x3C)
    Sleep(200)
    OP_24(0x1C3, 0x46)
    OP_24(0x125, 0x37)
    Sleep(200)
    OP_24(0x1C3, 0x3C)
    OP_24(0x125, 0x32)
    Sleep(200)
    OP_24(0x1C3, 0x32)
    OP_24(0x125, 0x2D)
    Sleep(200)
    OP_24(0x1C3, 0x28)
    OP_24(0x125, 0x28)
    Sleep(200)
    OP_24(0x1C3, 0x1E)
    OP_24(0x125, 0x1E)
    Sleep(200)
    OP_24(0x1C3, 0x14)
    OP_24(0x125, 0x14)
    Sleep(200)
    OP_23(0x1C3)
    OP_23(0x125)
    Return()

    # Function_43_566F end

    def Function_44_56DE(): pass

    label("Function_44_56DE")

    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    SetChrChipByIndex(0xFE, 23)
    OP_8E(0xFE, 0x5082, 0x992, 0x11288, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 27)
    SetChrSubChip(0xFE, 0)
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

    # Function_44_56DE end

    def Function_45_5769(): pass

    label("Function_45_5769")

    Sleep(500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 24)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4BDC, 0x992, 0x10DC4, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 0)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_45_5769 end

    def Function_46_57AD(): pass

    label("Function_46_57AD")

    Sleep(1000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x5320, 0x992, 0x10E32, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 12)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_46_57AD end

    def Function_47_57F8(): pass

    label("Function_47_57F8")

    Sleep(1500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 19)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x5546, 0x992, 0x10914, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 11)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_47_57F8 end

    def Function_48_5843(): pass

    label("Function_48_5843")

    Sleep(2000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 17)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4EE8, 0x992, 0x10892, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 9)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 45, 400)
    Return()

    # Function_48_5843 end

    def Function_49_588E(): pass

    label("Function_49_588E")

    Sleep(2500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 21)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x54E2, 0x992, 0x1027A, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 13)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_49_588E end

    def Function_50_58D9(): pass

    label("Function_50_58D9")

    Sleep(3000)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 22)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4894, 0x992, 0x10716, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 14)
    SetChrSubChip(0xFE, 0)
    OP_8C(0xFE, 315, 400)
    Return()

    # Function_50_58D9 end

    def Function_51_5924(): pass

    label("Function_51_5924")

    Sleep(3500)
    SetChrBattleFlags(0xFE, 0x20)
    SetChrChipByIndex(0xFE, 18)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4862, 0x992, 0x10216, 0xFA0, 0x0)
    SetChrChipByIndex(0xFE, 10)
    SetChrSubChip(0xFE, 0)
    Return()

    # Function_51_5924 end

    def Function_52_5968(): pass

    label("Function_52_5968")

    Sleep(4000)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4E8E, 0x992, 0x1034C, 0xFA0, 0x0)
    Return()

    # Function_52_5968 end

    def Function_53_599D(): pass

    label("Function_53_599D")

    Sleep(4500)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 20050, 2450, 63530, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x4F10, 0x992, 0xFEA6, 0xFA0, 0x0)
    Return()

    # Function_53_599D end

    def Function_54_59D2(): pass

    label("Function_54_59D2")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    RemoveParty(0x9, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_5A4E"),
        (1, "loc_5A54"),
        (SWITCH_DEFAULT, "loc_5A5A"),
    )


    label("loc_5A4E")

    OP_A2(0x1200)
    Jump("loc_5A5A")

    label("loc_5A54")

    OP_A2(0x1201)
    Jump("loc_5A5A")

    label("loc_5A5A")

    Return()

    # Function_54_59D2 end

    def Function_55_5A5B(): pass

    label("Function_55_5A5B")

    ClearMapFlags(0x1)
    OP_6D(-551720, -10000, -227160, 0)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_55_5A5B end

    SaveToFile()

Try(main)
