from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4105   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4105.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60221",
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
        'Dorothy',                              # 9
        'Nial',                                 # 10
        'Lt. Colonel Cid',                      # 11
        'Finella',                              # 12
        'Carnero',                              # 13
        'Tiffany',                              # 14
        'Mechanic Payton',                      # 15
        'Village Old Man',                      # 16
        'Passenger Town Gentleman',             # 17
        'Village Middle-Aged Man',              # 18
        'Village Middle-Aged Woman',            # 19
        'Village Old Woman',                    # 20
        'Village Young Woman',                  # 21
        'Passenger Student',                    # 22
        'Passenger Noble Girl',                 # 23
        'Passenger Old Man',                    # 24
        'Passenger Town Gentleman',             # 25
        'Passenger Town Lady',                  # 26
        'Passenger Town Young Woman',           # 27
        'Prince Olivert',                       # 28
        'Major Vander',                         # 29
        'Princess Klaudia',                     # 30
        'Brig. General Bright',                 # 31
        'Chancellor Osborne',                   # 32
        'Secretary Lechter',                    # 33
        'Captain Schwarz',                      # 34
        'Scherazard',                           # 35
        'Target Camera',                        # 36
        'Gretna',                               # 37
        'Gretna Shadow',                        # 38
        'Grancel City - East Block',            # 39
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
        'ED6_DT07/CH02070 ._CH',             # 00
        'ED6_DT07/CH02060 ._CH',             # 01
        'ED6_DT07/CH01540 ._CH',             # 02
        'ED6_DT07/CH01450 ._CH',             # 03
        'ED6_DT07/CH01550 ._CH',             # 04
        'ED6_DT07/CH01000 ._CH',             # 05
        'ED6_DT07/CH01010 ._CH',             # 06
        'ED6_DT07/CH01020 ._CH',             # 07
        'ED6_DT07/CH01030 ._CH',             # 08
        'ED6_DT07/CH01040 ._CH',             # 09
        'ED6_DT07/CH01050 ._CH',             # 0A
        'ED6_DT07/CH01040 ._CH',             # 0B
        'ED6_DT07/CH01480 ._CH',             # 0C
        'ED6_DT07/CH01490 ._CH',             # 0D
        'ED6_DT07/CH01200 ._CH',             # 0E
        'ED6_DT07/CH01230 ._CH',             # 0F
        'ED6_DT07/CH01150 ._CH',             # 10
        'ED6_DT27/CH03590 ._CH',             # 11
        'ED6_DT27/CH03260 ._CH',             # 12
        'ED6_DT27/CH03570 ._CH',             # 13
        'ED6_DT27/CH03210 ._CH',             # 14
        'ED6_DT27/CH03670 ._CH',             # 15
        'ED6_DT07/CH02090 ._CH',             # 16
        'ED6_DT27/CH03950 ._CH',             # 17
        'ED6_DT26/CH20805 ._CH',             # 18
        'ED6_DT07/CH00020 ._CH',             # 19
        'ED6_DT26/CH20808 ._CH',             # 1A
    )

    AddCharChipPat(
        'ED6_DT07/CH02070P._CP',             # 00
        'ED6_DT07/CH02060P._CP',             # 01
        'ED6_DT07/CH01540P._CP',             # 02
        'ED6_DT07/CH01450P._CP',             # 03
        'ED6_DT07/CH01550P._CP',             # 04
        'ED6_DT07/CH01000P._CP',             # 05
        'ED6_DT07/CH01010P._CP',             # 06
        'ED6_DT07/CH01020P._CP',             # 07
        'ED6_DT07/CH01030P._CP',             # 08
        'ED6_DT07/CH01040P._CP',             # 09
        'ED6_DT07/CH01050P._CP',             # 0A
        'ED6_DT07/CH01040P._CP',             # 0B
        'ED6_DT07/CH01480P._CP',             # 0C
        'ED6_DT07/CH01490P._CP',             # 0D
        'ED6_DT07/CH01200P._CP',             # 0E
        'ED6_DT07/CH01230P._CP',             # 0F
        'ED6_DT07/CH01150P._CP',             # 10
        'ED6_DT27/CH03590P._CP',             # 11
        'ED6_DT27/CH03260P._CP',             # 12
        'ED6_DT27/CH03570P._CP',             # 13
        'ED6_DT27/CH03210P._CP',             # 14
        'ED6_DT27/CH03670P._CP',             # 15
        'ED6_DT07/CH02090P._CP',             # 16
        'ED6_DT27/CH03950P._CP',             # 17
        'ED6_DT26/CH20805P._CP',             # 18
        'ED6_DT07/CH00020P._CP',             # 19
        'ED6_DT26/CH20808P._CP',             # 1A
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
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x101,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 58770,
        Z                   = 250,
        Y                   = 137000,
        Direction           = 281,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67350,
        Z                   = 0,
        Y                   = 145020,
        Direction           = 360,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 67340,
        Z                   = 0,
        Y                   = 146190,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 72500,
        Z                   = -10000,
        Y                   = 163540,
        Direction           = 76,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Unknown3            = 7,
        ChipIndex           = 0x7,
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
        Unknown3            = 8,
        ChipIndex           = 0x8,
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
        InitFunctionIndex   = 6,
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
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 6,
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
        Unknown3            = 18,
        ChipIndex           = 0x12,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 20,
        ChipIndex           = 0x14,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 21,
        ChipIndex           = 0x15,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 23,
        ChipIndex           = 0x17,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 24,
        ChipIndex           = 0x18,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 22,
        ChipIndex           = 0x16,
        NpcIndex            = 0x1C1,
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
        Unknown3            = 25,
        ChipIndex           = 0x19,
        NpcIndex            = 0x1C1,
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
        NpcIndex            = 0x80,
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
        NpcIndex            = 0x1C5,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 51050,
        Z                   = 0,
        Y                   = 83440,
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


    ScpFunction(
        "Function_0_562",          # 00, 0
        "Function_1_5A7",          # 01, 1
        "Function_2_5E2",          # 02, 2
        "Function_3_5F8",          # 03, 3
        "Function_4_2991",         # 04, 4
        "Function_5_2A13",         # 05, 5
        "Function_6_2AA4",         # 06, 6
        "Function_7_2B1A",         # 07, 7
        "Function_8_2B64",         # 08, 8
        "Function_9_2BA0",         # 09, 9
        "Function_10_2BEF",        # 0A, 10
        "Function_11_2C1D",        # 0B, 11
        "Function_12_2C93",        # 0C, 12
        "Function_13_2D09",        # 0D, 13
        "Function_14_4487",        # 0E, 14
        "Function_15_44CD",        # 0F, 15
        "Function_16_4549",        # 10, 16
        "Function_17_45B9",        # 11, 17
        "Function_18_461F",        # 12, 18
        "Function_19_46AC",        # 13, 19
        "Function_20_46EF",        # 14, 20
    )


    def Function_0_562(): pass

    label("Function_0_562")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_58A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_58A")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x21), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)

    label("loc_58A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_5A6")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_5A6")

    Return()

    # Function_0_562 end

    def Function_1_5A7(): pass

    label("Function_1_5A7")

    OP_16(0x2, 0xFA0, 0xFFFF5808, 0x7148, 0x23005F)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D1")
    OP_B1("t4105_7")
    Jump("loc_5DA")

    label("loc_5D1")

    OP_B1("t4105_3")

    label("loc_5DA")

    OP_82(0x81, 0x0)
    OP_64(0x0, 0x1)
    Return()

    # Function_1_5A7 end

    def Function_2_5E2(): pass

    label("Function_2_5E2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_5F7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_5E2")

    label("loc_5F7")

    Return()

    # Function_2_5E2 end

    def Function_3_5F8(): pass

    label("Function_3_5F8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetMapFlags(0x2000000)
    OP_1D(0xE)
    SetChrFlags(0x109, 0x80)
    OP_82(0x81, 0x0)
    OP_22(0x79, 0x0, 0x64)
    OP_71(0x409, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_6F(0xA, 161)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x20, 62500, -3000, 165990, 90)
    SetChrPos(0x21, 62320, -3000, 166860, 90)
    SetChrPos(0x22, 56810, 250, 137480, 90)
    SetChrPos(0x2C, 87000, 5500, 130500, 90)
    SetChrPos(0x2D, 87000, -1100, 130500, 90)
    OP_A1(0x2D, 0xB)
    OP_A1(0x2C, 0xA)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_71(0x80A, 0x0)
    ExitThread()
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    OP_48()
    OP_6D(88320, 1550, 192380, 0)
    OP_67(0, 7600, -10000, 0)
    OP_6B(3920, 0)
    OP_6C(212000, 0)
    OP_6E(448, 0)
    OP_11(0xFF, 0xFF, 0xFF, 0x0, 0x829D8, 0x0)

    def lambda_728():
        OP_6D(91660, 1550, 130380, 9000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_728)

    def lambda_740():
        OP_67(0, 6060, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_740)

    def lambda_758():
        OP_6B(6820, 9000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_758)

    def lambda_768():
        OP_6C(308000, 9000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_768)

    def lambda_778():
        OP_6E(310, 9000)
        ExitThread()

    QueueWorkItem(0x2C, 3, lambda_778)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_792():
        OP_8F(0xFE, 0x153D8, 0xFFFFE9EE, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_792)

    def lambda_7AD():
        OP_8F(0xFE, 0x153D8, 0xFFFFEC14, 0x1FDC4, 0x2BC, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 0, lambda_7AD)
    Sleep(2000)
    OP_72(0x200A, 0x0)
    ExitThread()
    OP_D8(0xA, 0x1F4)
    OP_6F(0xA, 261)
    OP_70(0xA, 0x19A)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x2C, 0x0)
    WaitChrThread(0x2D, 0x0)
    OP_23(0x79)
    OP_22(0xC8, 0x0, 0x64)
    OP_7C(0x0, 0x64, 0xBB8, 0x64)
    Sleep(100)
    Fade(500)
    OP_6D(86890, -650, 129970, 0)
    OP_67(0, 9270, -10000, 0)
    OP_6B(6120, 0)
    OP_6C(134000, 0)
    OP_6E(230, 0)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x3C)
    OP_0D()
    Sleep(100)
    OP_22(0x76, 0x0, 0x64)
    OP_71(0x864, 0x0)
    ExitThread()
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_71(0x805, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    Sleep(300)
    OP_48()
    StopSound(0xEA60, 0x29810, 0x32C8)

    def lambda_8D0():
        OP_6D(87200, 750, 129500, 13000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_8D0)

    def lambda_8E8():
        OP_67(0, 6610, -10000, 13000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_8E8)

    def lambda_900():
        OP_6B(3770, 13000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_900)

    def lambda_910():
        OP_6C(135000, 13000)
        ExitThread()

    QueueWorkItem(0x11, 3, lambda_910)

    def lambda_920():
        OP_6E(260, 13000)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_920)
    OP_43(0x17, 0x0, 0x0, 0x6)
    OP_43(0x1F, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x1B, 0x0, 0x0, 0xC)
    Sleep(500)
    OP_43(0x18, 0x0, 0x0, 0xB)
    OP_43(0x1D, 0x0, 0x0, 0x6)
    Sleep(1000)
    Sleep(700)
    Sleep(1000)
    OP_43(0x1C, 0x0, 0x0, 0x7)
    Sleep(5000)
    OP_43(0x109, 0x0, 0x0, 0x4)
    OP_43(0x10, 0x1, 0x0, 0x5)
    Sleep(7000)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1E, 0x80)
    OP_44(0x11, 0x0)
    OP_44(0x11, 0x1)
    OP_44(0x11, 0x2)
    OP_44(0x11, 0x3)
    OP_44(0x10, 0x0)
    Fade(1000)
    OP_6D(83460, 1500, 142720, 0)
    OP_67(0, 5180, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(135000, 0)
    OP_6E(320, 0)
    OP_44(0x11, 0x0)

    def lambda_A08():
        OP_6B(2500, 4000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_A08)
    OP_0D()
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10, 0x1)
    WaitChrThread(0x11, 0x1)

    ChrTalk(    #0
        0x10,
        (
            "#151F#2PAhhh... It's so lovely to be back here again.\x02\x03",

            "The Republic was a wonderful place, too,\x01",
            "but you can't beat the air here in Liberl.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x109,
        (
            "#1060F#6PYou wouldn't believe all that stuff happened\x01",
            "half a year ago looking at Grancel now, either.\x01",
            "It's all completely back to normal.\x02\x03",

            "The people here sure are strong for what's\x01",
            "usually such a peaceful country.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x10,
        (
            "#157F#2PWell, it's a country ruled by a queen!\x02\x03",

            "#150FEveryone knows women are tough in\x01",
            "the face of adversity.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x109,
        (
            "#1066F#6PI'm not sure whether you're a perfect\x01",
            "example of that or the opposite...\x02\x03",

            "#1075FYou're right about the air here, though.\x01",
            "It IS nice.\x02\x03",

            "#1060FNostalgic, almost. Makes me feel a little\x01",
            "homesick.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10,
        (
            "#150F#2PYour home's in Arteria, right?\x02\x03",

            "The place with all the reeeally big churches\x01",
            "and stuff?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x109,
        (
            "#1060F#6PNah. I'm not actually from Arteria.\x02\x03",

            "Not many people are.\x02\x03",

            "It's actually pretty darn small--like, smaller than\x01",
            "most states around the continent.\x02\x03",

            "It's where the High Seat of the Septian Church \x01",
            "is, so lots of pilgrims and clergymen gather there,\x01",
            "but few are actually born there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#151F#2POh, really? Huh...\x02\x03",

            "#153FSo where are you from, then?\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, 75890, 0, 143270, 90)

    NpcTalk(    #7
        0x11,
        "Man's Voice",
        "#1PDoooroooooothyyyyyyyyy...\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(100)
    OP_62(0x10, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x11, 69890, 0, 143270, 90)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)

    def lambda_F4E():
        OP_6D(78880, 1500, 141980, 3000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_F4E)

    def lambda_F66():
        OP_67(0, 4760, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_F66)

    def lambda_F7E():
        OP_6B(2500, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_F7E)

    def lambda_F8E():
        OP_6C(224000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_F8E)

    def lambda_F9E():
        OP_6E(327, 3000)
        ExitThread()

    QueueWorkItem(0x10, 3, lambda_F9E)

    def lambda_FAE():
        OP_8E(0xFE, 0x134E8, 0x5DC, 0x22EA2, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_FAE)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)
    OP_8C(0x109, 270, 400)
    Sleep(200)
    OP_8C(0x10, 270, 400)
    Sleep(500)
    OP_8E(0x10, 0x13BDC, 0x5DC, 0x22F2E, 0x3E8, 0x0)
    WaitChrThread(0x11, 0x0)

    ChrTalk(    #8
        0x10,
        (
            "#153F#6POh, Nial!\x02\x03",

            "#151FI'm home! Did you miss me?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x11,
        (
            "#147F#2PDid I miss you?\x02\x01",

            "#144FOf course I MISSED you! What in Aidios'\x01",
            "name have you been DOING?!\x02\x03",

            "I sent you to Bose! How did you end up in \x01",
            "Calvard?!\x02\x03",

            "You were definitely on the west-bound liner!\x01",
            "I'm sure of it!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#154F#6PI really don't know...\x02\x03",

            "#153FOh, wait! I might actually know!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #11
        0x11,
        "#142F#2PGo on, then. Spit it out.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        (
            "#155F#6PI bet I'm a sleepwalker.\x02\x03",

            "After I got on the right airship, I fell asleep\x01",
            "and then sleepwalked onto the wrong one!\x02\x03",

            "To think that all of this could turn out to be\x01",
            "part of some elaborate murder plot.\x02\x03",

            "#151FWowie! All of a sudden, I feel like I've walked\x01",
            "right into a mystery novel!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0xC, 0xD, 0xFA, 0x2)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1300)

    ChrTalk(    #13
        0x11,
        "#144F#2P#3SSleepwalkers don't change airships, you idiot!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Sleep(300)

    ChrTalk(    #14
        0x11,
        (
            "#145F#2P#2S#40W*pant* *pant* \x01",
            "#40WUgh... I'm all out of breath now...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#154F#6PA-Are you all right?\x02\x03",

            "I really do think you should cut down on your\x01",
            "smoking... You're not as young as you used to \x01",
            "be, you know.\x02\x03",

            "#150FOh, right... Your 30th birthday was last Friday,\x01",
            "too, wasn't it?\x02\x03",

            "#151FHappy birthday! I bought a cake over in Calvard\x01",
            "and had a big celebration for it, too!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x11,
        (
            "#145F#2PHow is it that you can remember useless crap like\x01",
            "that and not the things that actually matter?\x02\x03",

            "#142FI bet you were just looking for an excuse to eat\x01",
            "cake all by yourself, weren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x10,
        (
            "#151F#6PYou should've seen it, Nial! It was made with\x01",
            "Eastern matcha, so it was unlike any cake I'd\x01",
            "ever seen!\x02\x03",

            "That perfect blend of sweetness and bitterness \x01",
            "was just SUBLIME.\x02\x03",

            "#150FI took looots and loooooots of cute pictures of it,\x01",
            "so I'll show you them all later.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x11,
        (
            "#144F#2P#3SYou brought me PICTURES OF A CAKE?!\x01",
            "At least bring back a souvenir!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #19
        0x109,
        (
            "#1068F#6P(M-Man...)\x02\x03",

            "(They always FELT like they could go into business\x01",
            "as a comedy duo and actually make money off it,\x01",
            "but they're even more of a crackup now.)\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x11, 0x0, 2000, 0x26, 0x27, 0xFA, 0x2)
    Sleep(1000)

    ChrTalk(    #20
        0x11,
        "#143F#2PWait a second...\x02",
    )

    CloseMessageWindow()

    def lambda_17DD():
        OP_6D(78920, 1500, 142630, 1500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_17DD)

    def lambda_17F5():
        OP_67(0, 5000, -10000, 1500)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17F5)

    def lambda_180D():
        OP_8E(0xFE, 0x13C68, 0x5DC, 0x23424, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_180D)
    OP_8C(0x10, 0, 400)
    OP_8C(0x11, 45, 400)
    WaitChrThread(0x109, 0x2)
    OP_8C(0x109, 225, 400)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #21
        0x109,
        (
            "#1066F#6PHaha... Nice to see you again, Nial.\x02\x03",

            "You're lookin' same old, same old...though\x01",
            "maybe you're not so happy about that.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x11,
        (
            "#144F#5PWh-What are you doing here?!\x02\x03",

            "Please, PLEASE tell me she didn't end up going\x01",
            "to Arteria and causing trouble there, too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x109,
        (
            "#1061F#6PHaha. Your wish is my command.\x02\x03",

            "#1062FWe just ran into one another on that airship\x01",
            "by total coincidence, that's all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#143F#5PO-Oh, good... You had me worried for a minute.\x02\x03",

            "#145FI was scared stiff she'd gone and smashed\x01",
            "some super expensive stained glass windows\x01",
            "in the cathedral there or who knows what...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x109,
        "#1068F#6PI'm so sorry for what you have to put up with...\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10, 270, 400)
    Sleep(300)

    ChrTalk(    #26
        0x10,
        "#151F#6PPshaw! You're too much of a worrywart.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#145F#5PWhose fault do you think that is...?\x02\x03",

            "#141FStill, it's good to see you again, Father.\x02\x03",

            "What brings you to Liberl? Somethin' else happen\x01",
            "here?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x109,
        (
            "#1060F#6POh, just a bit of work-related business I've gotta\x01",
            "take care of.\x02\x03",

            "It's not part of a major investigation, so don't go\x01",
            "getting your hopes up. Nothing of interest's gonna\x01",
            "happen.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x11,
        (
            "#147F#5PHaha... I'll be the judge of that.\x02\x03",

            "#141FAnyway, so where're you staying for the time\x01",
            "being? Grancel Cathedral?\x02\x03",

            "I'll have to drop by and say hi some time when\x01",
            "I get the chance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x109,
        "#1066F#6PHaha... Go for it.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 90, 400)
    Sleep(300)

    ChrTalk(    #31
        0x11,
        (
            "#144F#2PIn the meantime, I'm dragging your butt right\x01",
            "back to the office, Dorothy!\x02\x03",

            "You're going to tell us aaaaaall about what the\x01",
            "hell you've been doing these past two weeks!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10, 0x0, 2000, 0x8, 0x9, 0xFA, 0x2)
    OP_22(0xF, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #32
        0x10,
        (
            "#151F#6PHeehee. You bet'cha!\x02\x03",

            "I snapped photos of every meal I had while I was\x01",
            "over in Calvard, so I'm sure if we develop them,\x01",
            "I'll be able to remember everything!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        "#145F#2PI'm not talking about your gourmet report!\x02",
    )

    CloseMessageWindow()

    def lambda_1F12():

        label("loc_1F12")

        TurnDirection(0x109, 0x11, 0)
        OP_48()
        Jump("loc_1F12")

    QueueWorkItem2(0x109, 3, lambda_1F12)
    OP_8C(0x11, 270, 400)
    Sleep(100)

    def lambda_1F2F():
        OP_6D(77110, 1500, 143410, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1F2F)

    def lambda_1F47():
        OP_67(0, 4760, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1F47)

    def lambda_1F5F():
        OP_8E(0xFE, 0xF5AA, 0x0, 0x22E2A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1F5F)
    Sleep(500)

    def lambda_1F7F():
        OP_8E(0xFE, 0xFA00, 0x0, 0x22E2A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1F7F)
    Sleep(1500)
    OP_9F(0x11, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    Sleep(100)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x10, 0x0)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x10, 0x80)
    OP_44(0x109, 0x3)
    Sleep(500)

    def lambda_1FD7():
        OP_6D(78920, 1500, 142630, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1FD7)

    def lambda_1FEF():
        OP_67(0, 5020, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1FEF)
    Sleep(1500)
    OP_62(0x109, 0x0, 2000, 0x10, 0x13, 0xFA, 0x1)
    OP_22(0x31, 0x0, 0x64)
    Sleep(1500)

    ChrTalk(    #34
        0x109,
        (
            "#1068F#5PWhew... Seeing those two together really\x01",
            "makes it sink in that I'm back here.\x02\x03",

            "#1060FThinking about it, I wonder how all the others \x01",
            "here are doing?\x02\x03",

            "I know Estelle and Joshua are abroad at the \x01",
            "moment, but I've got no idea what the others \x01",
            "are up to.\x02",
        )
    )

    CloseMessageWindow()
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x12, 62480, 0, 142870, 90)

    NpcTalk(    #35
        0x12,
        "Man's Voice",
        "#1PIs that you, Father Graham?\x02",
    )

    CloseMessageWindow()
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_219F():
        OP_6D(74460, 1500, 142940, 2500)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_219F)

    def lambda_21B7():
        OP_67(0, 4300, -10000, 2500)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_21B7)
    OP_9F(0x12, 0xFF, 0xFF, 0xFF, 0xFF, 0x64)

    def lambda_21DA():
        OP_8E(0xFE, 0x104F0, 0x0, 0x22E34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_21DA)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #36
        0x109,
        "#1064F#2PLieutenant Colonel Cid!\x02",
    )

    CloseMessageWindow()

    def lambda_222A():
        OP_6D(74110, 1500, 142270, 2000)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_222A)

    def lambda_2242():
        OP_67(0, 5410, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_2242)

    def lambda_225A():
        OP_6B(2420, 2000)
        ExitThread()

    QueueWorkItem(0x11, 2, lambda_225A)

    def lambda_226A():
        OP_8E(0xFE, 0x122F0, 0x5DC, 0x23064, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_226A)
    Sleep(400)

    def lambda_228A():
        OP_8E(0xFE, 0x12A5C, 0x5DC, 0x23122, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_228A)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x109, 0x0)
    Sleep(500)

    ChrTalk(    #37
        0x12,
        (
            "#701F#2PIt's good to see you again.\x02\x03",

            "I'm pleased to see you've been keeping well\x01",
            "since we last met at that banquet.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x109,
        (
            "#1060F#6PThe same to you, sir.\x02\x03",

            "I gotta say, I wasn't expecting you to\x01",
            "be the army representative who came\x01",
            "to meet me, though.\x02\x03",

            "I figured it'd be Julia.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x12,
        (
            "#701F#2PIt may have been, but she's currently out on \x01",
            "another mission, so unfortunately you'll have\x01",
            "to make do with me.\x02\x03",

            "I didn't have anything better to do, so I came\x01",
            "in her place. \x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #40
        0x109,
        (
            "#1061F#6PThere's no need to be so modest!\x02\x03",

            "#1062FA little bird told me that you're going to be \x01",
            "promoted to full-on colonel soon, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x12,
        (
            "#703F#2PI shouldn't be surprised that your people have\x01",
            "such a good information network, but I still am.\x02\x03",

            "#701FHeh. Still, I'm afraid I still feel the position is too\x01",
            "much responsibility for me as I am.\x02\x03",

            "Brigadier General Bright still has plenty of work\x01",
            "left in him, too. I wouldn't want to take any of it\x01",
            "from him.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x109,
        (
            "#1066F#6PPoor Cassius is still getting worked to the bone,\x01",
            "huh?\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #43
        0x109,
        (
            "#1063F#6PAnyway, getting down to business...\x01",
            "It's in Grancel Cathedral, right?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x12,
        (
            "#703F#2PThat's correct. It's being kept underneath it\x01",
            "to be more specific, although I imagine you're\x01",
            "already aware of that much.\x02\x03",

            "#700FI hear laymen like myself can't even enter it\x01",
            "without the knights' permission.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x109,
        (
            "#1060F#6PPretty much. It's a...special place, you see.\x02\x03",

            "I'll fill you in on the details when we get there.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        (
            "#703F#2PAll right, then.\x02\x03",

            "#701FWell, we may as well head there right away.\x01",
            "There's someone I want you to meet in the\x01",
            "cathedral.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x109,
        "#1064F#6PHuh? Who?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x12,
        (
            "#701F#2PLet's just say...someone who's been assisting\x01",
            "with this case.\x02\x03",

            "They'll be apprising you of the details on what\x01",
            "you're dealing with here.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x109, 0x0)
    OP_A2(0x2504)
    NewScene("ED6_DT21/T4101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_5F8 end

    def Function_4_2991(): pass

    label("Function_4_2991")

    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    OP_8E(0xFE, 0x143E8, 0x60E, 0x209B8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142C6, 0x5DC, 0x233F2, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_4_2991 end

    def Function_5_2A13(): pass

    label("Function_5_2A13")

    Sleep(1500)
    OP_51(0xFE, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x10), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearChrFlags(0xFE, 0x80)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    Sleep(300)
    OP_8C(0xFE, 225, 400)
    Sleep(500)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8E(0xFE, 0x143E8, 0x60E, 0x209B8, 0xBB8, 0x0)
    OP_8E(0xFE, 0x142DA, 0x5DC, 0x22EA2, 0x7D0, 0x0)
    Return()

    # Function_5_2A13 end

    def Function_6_2AA4(): pass

    label("Function_6_2AA4")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14BD6, 0x60E, 0x1FD88, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14244, 0x60E, 0x207C4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x14244, 0x5DC, 0x22EB6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1095A, 0x0, 0x22EB6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_6_2AA4 end

    def Function_7_2B1A(): pass

    label("Function_7_2B1A")

    OP_43(0x1C, 0x1, 0x0, 0x8)
    Sleep(1000)
    OP_43(0x1E, 0x1, 0x0, 0x9)
    WaitChrThread(0x1C, 0x1)
    WaitChrThread(0x1E, 0x1)
    Sleep(300)
    OP_43(0x1C, 0x1, 0x0, 0xA)
    Sleep(300)
    OP_8E(0x1E, 0x14316, 0x60E, 0x2076A, 0x7D0, 0x0)
    OP_43(0x1E, 0x1, 0x0, 0xA)
    Return()

    # Function_7_2B1A end

    def Function_8_2B64(): pass

    label("Function_8_2B64")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x144D8, 0x60E, 0x1FDC4, 0x7D0, 0x0)
    OP_8C(0xFE, 90, 400)
    Return()

    # Function_8_2B64 end

    def Function_9_2BA0(): pass

    label("Function_9_2BA0")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 87560, 1600, 130400, 270)
    OP_8E(0xFE, 0x14988, 0x60E, 0x1FDCD, 0xBB8, 0x0)
    OP_62(0xFE, 0x0, 1600, 0x26, 0x27, 0xC8, 0x0)
    Sleep(1000)
    OP_63(0xFE)
    Return()

    # Function_9_2BA0 end

    def Function_10_2BEF(): pass

    label("Function_10_2BEF")

    OP_8E(0xFE, 0x14438, 0x5DC, 0x22EF2, 0x7D0, 0x0)
    OP_8E(0xFE, 0x109BE, 0x0, 0x22FB0, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_10_2BEF end

    def Function_11_2C1D(): pass

    label("Function_11_2C1D")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 93860, 1650, 131620, 0)
    OP_8E(0xFE, 0x16EA4, 0x672, 0x20814, 0x7D0, 0x0)
    OP_8E(0xFE, 0x145E6, 0x60E, 0x2083C, 0x7D0, 0x0)
    OP_8E(0xFE, 0x145E6, 0x5DC, 0x231A4, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10892, 0x0, 0x231A4, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_11_2C1D end

    def Function_12_2C93(): pass

    label("Function_12_2C93")

    ClearChrFlags(0xFE, 0x80)
    SetChrFlags(0xFE, 0x40)
    SetChrBattleFlags(0xFE, 0x20)
    OP_89(0xFE, 90830, 1550, 127810, 0)
    OP_8E(0xFE, 0x14D16, 0x60E, 0x1F342, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x60E, 0x1FDA6, 0x7D0, 0x0)
    OP_8E(0xFE, 0x142B2, 0x5DC, 0x22DDA, 0x7D0, 0x0)
    OP_8E(0xFE, 0x1095A, 0x0, 0x22EB6, 0x7D0, 0x0)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_12_2C93 end

    def Function_13_2D09(): pass

    label("Function_13_2D09")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    OP_72(0x40A, 0x0)
    ExitThread()
    OP_A1(0x2C, 0xA)
    SetChrPos(0x2C, 87000, -5650, 130500, 90)
    OP_72(0x40B, 0x0)
    ExitThread()
    OP_A1(0x2D, 0xB)
    SetChrPos(0x2D, 87000, -5100, 130500, 90)
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x409, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_6F(0xA, 60)
    ClearChrFlags(0x27, 0x80)
    ClearChrFlags(0x28, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x22, 0x80)
    SetChrPos(0x20, 82820, 1500, 143000, 180)
    SetChrPos(0x21, 81500, 1500, 143000, 270)
    SetChrPos(0x22, 80600, 1500, 143000, 90)
    SetChrPos(0x27, 79280, 1500, 143000, 90)
    SetChrPos(0x28, 78180, 1500, 143000, 90)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    OP_11(0xDC, 0xF0, 0xC8, 0xEA60, 0x41EB0, 0x0)
    OP_6D(82000, 1500, 142420, 0)
    OP_67(0, 10640, -10000, 0)
    OP_6B(3620, 0)
    OP_6C(30000, 0)
    OP_6E(590, 0)

    def lambda_2E4B():
        OP_67(0, 8640, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_2E4B)

    def lambda_2E63():
        OP_6B(2900, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_2E63)

    def lambda_2E73():
        OP_6C(45000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_2E73)
    FadeToBright(3000, 0)
    OP_0D()
    WaitChrThread(0x2B, 0x0)
    Fade(1000)
    OP_6D(82600, 1500, 140480, 0)
    OP_67(0, 4860, -10000, 0)
    OP_6B(3860, 0)
    OP_6C(135000, 0)
    OP_6E(262, 0)
    OP_22(0x75, 0x0, 0x64)
    OP_0D()
    Sleep(300)
    OP_22(0xA6, 0x0, 0x64)
    Sleep(1000)
    SetMessageWindowPos(300, 100, -1, -1)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #49
        "\x07\x05Thank you all for waiting.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #50
        (
            "\x07\x05The Calabria international airliner, bound for\x01",
            "the Principality of Remiferia, will be departing\x01",
            "momentarily.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetChrName("Woman's Voice")

    AnonymousTalk(    #51
        "\x07\x05Please mind your footing when boarding.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x76, 0x0, 0x64)
    OP_71(0x80A, 0x0)
    ExitThread()
    OP_6F(0xA, 60)
    OP_70(0xA, 0x1)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_71(0x805, 0x0)
    ExitThread()
    OP_6F(0x5, 100)
    OP_70(0x5, 0x0)
    OP_73(0x5)
    Sleep(300)
    OP_22(0x6, 0x0, 0x64)
    OP_6F(0xA, 411)
    OP_70(0xA, 0x1C2)
    OP_73(0xA)
    OP_4A(0x20, 255)
    OP_4A(0x21, 255)
    OP_4A(0x22, 255)
    OP_43(0x20, 0x3, 0x0, 0xE)
    OP_43(0x21, 0x3, 0x0, 0xF)
    OP_43(0x22, 0x3, 0x0, 0x10)
    Sleep(3000)

    def lambda_3069():
        OP_6D(85600, 1500, 140480, 2000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3069)

    def lambda_3081():
        OP_8E(0xFE, 0x143D4, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x27, 1, lambda_3081)
    Sleep(300)

    def lambda_30A1():
        OP_8E(0xFE, 0x13E70, 0x5DC, 0x22E34, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_30A1)
    WaitChrThread(0x27, 0x1)
    Sleep(300)
    OP_8C(0x27, 0, 400)

    def lambda_30CD():
        OP_8C(0x28, 0, 400)
        ExitThread()

    QueueWorkItem(0x28, 2, lambda_30CD)
    Sleep(500)
    SetChrChipByIndex(0x27, 26)
    SetChrSubChip(0x27, 0)
    OP_22(0x8F, 0x0, 0x64)
    OP_99(0x27, 0x0, 0x5, 0x3E8)
    Sleep(500)
    OP_99(0x27, 0x6, 0x7, 0x3E8)
    SetChrChipByIndex(0x27, 23)
    SetChrSubChip(0x27, 0)
    Sleep(500)
    OP_8C(0x27, 180, 400)
    Sleep(300)

    def lambda_3121():
        OP_6D(86500, 1500, 133000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3121)

    def lambda_3139():
        OP_67(0, 4500, -10000, 7000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_3139)
    OP_43(0x27, 0x3, 0x0, 0x11)
    Sleep(50)
    OP_43(0x28, 0x3, 0x0, 0x12)
    WaitChrThread(0x27, 0x3)
    WaitChrThread(0x28, 0x3)
    OP_6F(0xA, 450)
    OP_70(0xA, 0x19B)
    Sleep(400)
    OP_22(0x7, 0x0, 0x64)
    Sleep(450)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xA)
    Sleep(300)
    OP_22(0xE2, 0x0, 0x64)
    Sleep(1500)
    OP_22(0x78, 0x0, 0x64)
    OP_B0(0x5, 0x32)
    OP_6F(0x5, 0)
    OP_70(0x5, 0x64)
    Sleep(1300)
    OP_22(0x76, 0x0, 0x64)
    OP_B0(0xA, 0x1E)
    OP_6F(0xA, 1)
    OP_70(0xA, 0x3C)
    OP_73(0xA)
    Sleep(500)
    OP_23(0x75)
    Fade(1000)
    OP_6D(85600, 1500, 131100, 0)
    OP_67(0, 12800, -10000, 0)
    OP_6B(4160, 0)
    OP_6C(135000, 0)
    OP_6E(314, 0)
    Sleep(500)

    def lambda_3227():
        OP_8F(0xFE, 0x153D8, 0xFFFFEDD6, 0x1FDC4, 0x12C, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 0, lambda_3227)
    OP_22(0x77, 0x1, 0x64)
    OP_6F(0xA, 61)
    OP_70(0xA, 0xA0)
    OP_73(0xA)
    OP_71(0x200A, 0x0)
    ExitThread()
    OP_6F(0xA, 161)
    OP_70(0xA, 0x104)
    WaitChrThread(0x2C, 0x0)

    def lambda_3271():
        OP_6D(113780, 3500, 131100, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3271)

    def lambda_3289():
        OP_67(0, 9800, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_3289)

    def lambda_32A1():
        OP_6C(90000, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 2, lambda_32A1)

    def lambda_32B1():
        OP_6B(4460, 8000)
        ExitThread()

    QueueWorkItem(0x2B, 3, lambda_32B1)

    def lambda_32C1():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_32C1)

    def lambda_32DC():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x64, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_32DC)
    Sleep(200)

    def lambda_32FC():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_32FC)

    def lambda_3317():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0xC8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3317)
    Sleep(200)

    def lambda_3337():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3337)

    def lambda_3352():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1F4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3352)
    Sleep(200)

    def lambda_3372():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3372)

    def lambda_338D():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x320, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_338D)
    Sleep(200)

    def lambda_33AD():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_33AD)

    def lambda_33C8():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_33C8)
    Sleep(200)

    def lambda_33E8():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_33E8)

    def lambda_3403():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x4B0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3403)
    Sleep(200)

    def lambda_3423():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3423)

    def lambda_343E():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_343E)
    Sleep(200)

    def lambda_345E():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_345E)

    def lambda_3479():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3479)
    Sleep(200)

    def lambda_3499():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3499)

    def lambda_34B4():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x9C4, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_34B4)
    Sleep(200)

    def lambda_34D4():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_34D4)

    def lambda_34EF():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_34EF)
    Sleep(200)

    def lambda_350F():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_350F)

    def lambda_352A():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1194, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_352A)
    Sleep(200)

    def lambda_354A():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_354A)

    def lambda_3565():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1770, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3565)
    Sleep(200)

    def lambda_3585():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_3585)

    def lambda_35A0():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_35A0)
    Sleep(200)

    def lambda_35C0():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_35C0)

    def lambda_35DB():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x2710, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_35DB)
    Sleep(200)

    def lambda_35FB():
        OP_8F(0xFE, 0x26548, 0xFFFFFD76, 0x1FDC4, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x2C, 1, lambda_35FB)

    def lambda_3616():
        OP_8F(0xFE, 0x26548, 0xFFFFFBB4, 0x1FDC4, 0x32C8, 0x0)
        ExitThread()

    QueueWorkItem(0x2D, 1, lambda_3616)
    Sleep(2800)
    OP_43(0x23, 0x3, 0x0, 0x13)
    WaitChrThread(0x2B, 0x0)
    Sleep(1000)
    Fade(500)
    OP_44(0x2B, 0xFF)
    OP_6D(69400, -10000, 159000, 0)
    OP_67(0, 5910, -10000, 0)
    OP_6B(2000, 0)
    OP_6C(219000, 0)
    OP_6E(414, 0)
    ClearChrFlags(0x29, 0x80)
    ClearChrFlags(0x23, 0x80)
    ClearChrFlags(0x24, 0x80)
    ClearChrFlags(0x25, 0x80)
    ClearChrFlags(0x2A, 0x80)
    ClearChrFlags(0x26, 0x80)
    SetChrPos(0x29, 71330, -10000, 158970, 180)
    SetChrPos(0x23, 70590, -10000, 160050, 180)
    SetChrPos(0x24, 69700, -10000, 159590, 180)
    SetChrPos(0x25, 70420, -10000, 161960, 180)
    SetChrPos(0x2A, 71370, -10000, 162100, 180)
    SetChrPos(0x26, 69960, -10000, 162900, 180)
    OP_0D()
    Sleep(1000)

    ChrTalk(    #52
        0x29,
        "#173F#6PS-So that was the Blood and Iron Chancellor...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x2A,
        (
            "#025F#6PI can't believe he actually went out of his way\x01",
            "to use a civilian airship when he probably has a\x01",
            "private one of his own.\x02\x03",

            "#022FI'd heard rumors about how out of the ordinary\x01",
            "he is, but he lives up to all of them.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3835():
        OP_6D(69400, -10000, 159730, 1000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_3835)

    def lambda_384D():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x23, 2, lambda_384D)
    Sleep(100)

    def lambda_3860():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_3860)
    Sleep(100)

    def lambda_3873():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_3873)
    WaitChrThread(0x2B, 0x0)
    Sleep(300)

    ChrTalk(    #54
        0x23,
        (
            "#1545F#5PHaha... He keeps me on my toes, to put it playfully\x01",
            "enough.\x02\x03",

            "#1540FHim aside, thanks for coming all this way to see me\x01",
            "off, Schera.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x2A,
        (
            "#021F#6PI was lucky I just happened to have business\x01",
            "here at the right time.\x02\x03",

            "#524FIt feels like this is going to be the last chance\x01",
            "we get to see one another for a while, after all.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x23,
        (
            "#1541F#5PRather unfortunate, as my dream is and always\x01",
            "was to live away my days in the lap of luxury\x01",
            "surrounded by women as beautiful as you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x2A,
        (
            "#025F#6P*sigh* Well, good luck with that.\x02\x03",

            "#022FChanging the subject, though...who was the\x01",
            "young man at the chancellor's side?\x02\x03",

            "He didn't strike me as your ordinary guy...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x26,
        "#1122F#11POh? You could tell?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x2A,
        (
            "#025F#5PBut of course.\x02\x03",

            "#524FI'd say I'm used to running into people\x01",
            "who are out of the ordinary at this point.\x01",
            "We've sure fought enough of them.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x23,
        (
            "#1551F#5PHis name's Lechter Arundel. He's a secretary\x01",
            "who was sent here by the Imperial government.\x02\x03",

            "#1540FApparently, he was the one who planned out all\x01",
            "the details of the chancellor's visit to Liberl.\x02\x03",

            "#1545FI can't pretend to know much regarding his\x01",
            "background, but he's exceptionally skilled at\x01",
            "what he does.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x25,
        (
            "#1169F#12PActually...\x02\x03",

            "#1163F...I know a little.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x26, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x29, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x24, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x2A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_3DD7():
        TurnDirection(0xFE, 0x25, 400)
        ExitThread()

    QueueWorkItem(0x2A, 1, lambda_3DD7)

    ChrTalk(    #62
        0x29,
        "#173F#5PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x2A,
        "#023F#6POh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x23,
        "#1543F#5PIs that true?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #65
        0x25,
        "#1167F#12PYes...\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #66
        (
            "\x07\x05Klaudia explained that Lechter once attended the same academy as her and had\x01",
            "served at its Student Council president.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #67
        (
            "\x07\x05She also mentioned about his sudden disappearance after the academy festival\x01",
            "two years ago.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_59()
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Sleep(500)

    ChrTalk(    #68
        0x24,
        "#270F#5PUnbelievable...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x29,
        "#172F#5PTh-Then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x23,
        (
            "#1551F#5PSomeone connected to the chancellor had visited\x01",
            "Liberl first?\x02\x03",

            "#1542FThen he's very likely to have had his own veritable\x01",
            "information network established here long before I\x01",
            "even came up with the idea.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x26,
        (
            "#1125F#12PI think it's safe for us to assume that's the case.\x02\x03",

            "#1128FWhich also means that it's safe to assume he\x01",
            "knows every detail about all that's happened\x01",
            "here since.\x02\x03",

            "#1122FFrom the coup d'etat to the crisis regarding the\x01",
            "Aureole... All of it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x23,
        "#1551F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x2A,
        "#025F#6PThis man gets more unbelievable by the minute...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x25,
        (
            "#1169F#12PHe actually gave me a message to pass on to you\x01",
            "earlier, too.\x02\x03",

            "#1162F'Watch your back, so you don't get swallowed up\x01",
            "by that monster when you get tired of dancing.'\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x24,
        "#276F#5P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x23,
        (
            "#1544F#5PHe sure knows how to sting where it hurts,\x01",
            "doesn't he?\x02\x03",

            "#1547FHaha. I feel like I can see a whole new world\x01",
            "of pleasure opening up before my eyes.\x02",
        )
    )

    CloseMessageWindow()
    OP_20(0x7D0)
    Sleep(1000)

    ChrTalk(    #77
        0x23,
        (
            "#1545F#5PHe should know better. Getting outdone at\x01",
            "every turn like this is really not my style.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x25,
        "#1164F#12PWhat do you mean?\x02",
    )

    CloseMessageWindow()

    def lambda_438D():
        OP_6D(69400, -10000, 159000, 1200)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_438D)

    def lambda_43A5():
        OP_6C(206000, 1200)
        ExitThread()

    QueueWorkItem(0x2B, 1, lambda_43A5)
    TurnDirection(0x23, 0x29, 400)

    def lambda_43BC():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x2A, 2, lambda_43BC)

    def lambda_43CA():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x24, 2, lambda_43CA)
    WaitChrThread(0x2B, 0x0)
    Sleep(300)

    ChrTalk(    #79
        0x23,
        (
            "#1541F#12PCaptain Schwarz?\x02\x03",

            "#1540FI have a little favor I'd like to ask for when\x01",
            "we're in the air...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_444C():
        TurnDirection(0xFE, 0x23, 300)
        ExitThread()

    QueueWorkItem(0x29, 2, lambda_444C)

    def lambda_445A():
        OP_6B(1800, 3000)
        ExitThread()

    QueueWorkItem(0x2B, 0, lambda_445A)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_21()
    Sleep(1000)
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/E0810   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_2D09 end

    def Function_14_4487(): pass

    label("Function_14_4487")


    def lambda_448D():
        OP_8E(0xFE, 0x14384, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_448D)
    WaitChrThread(0x20, 0x1)

    def lambda_44AD():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x20, 1, lambda_44AD)
    WaitChrThread(0x20, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_14_4487 end

    def Function_15_44CD(): pass

    label("Function_15_44CD")

    SetChrFlags(0xFE, 0x40)
    Sleep(300)
    OP_8C(0xFE, 90, 400)
    Sleep(300)

    def lambda_44E9():
        OP_8E(0xFE, 0x1444C, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_44E9)
    WaitChrThread(0xFE, 0x1)

    def lambda_4509():
        OP_8E(0xFE, 0x1444C, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4509)
    WaitChrThread(0xFE, 0x1)

    def lambda_4529():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4529)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_15_44CD end

    def Function_16_4549(): pass

    label("Function_16_4549")

    SetChrFlags(0xFE, 0x40)
    Sleep(1300)

    def lambda_4559():
        OP_8E(0xFE, 0x14384, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4559)
    WaitChrThread(0xFE, 0x1)

    def lambda_4579():
        OP_8E(0xFE, 0x14384, 0x60E, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4579)
    WaitChrThread(0xFE, 0x1)

    def lambda_4599():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_4599)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_16_4549 end

    def Function_17_45B9(): pass

    label("Function_17_45B9")


    def lambda_45BF():
        OP_8E(0xFE, 0x143D4, 0x60E, 0x20BB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45BF)
    WaitChrThread(0xFE, 0x1)

    def lambda_45DF():
        OP_8E(0xFE, 0x14DFC, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45DF)
    WaitChrThread(0xFE, 0x1)

    def lambda_45FF():
        OP_8E(0xFE, 0x154A0, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_45FF)
    WaitChrThread(0xFE, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_17_45B9 end

    def Function_18_461F(): pass

    label("Function_18_461F")

    OP_8C(0x28, 90, 400)

    def lambda_462C():
        OP_8E(0xFE, 0x143D4, 0x5DC, 0x22E98, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_462C)
    WaitChrThread(0x28, 0x1)

    def lambda_464C():
        OP_8E(0xFE, 0x143D4, 0x60E, 0x20BB6, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_464C)
    WaitChrThread(0xFE, 0x1)

    def lambda_466C():
        OP_8E(0xFE, 0x14DFC, 0x672, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_466C)
    WaitChrThread(0xFE, 0x1)

    def lambda_468C():
        OP_8E(0xFE, 0x154A0, 0x5DC, 0x1FDC4, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x28, 1, lambda_468C)
    WaitChrThread(0x28, 0x1)
    SetChrFlags(0xFE, 0x80)
    Return()

    # Function_18_461F end

    def Function_19_46AC(): pass

    label("Function_19_46AC")

    OP_24(0x77, 0x5A)
    Sleep(300)
    OP_24(0x77, 0x50)
    Sleep(300)
    OP_24(0x77, 0x46)
    Sleep(300)
    OP_24(0x77, 0x3C)
    Sleep(300)
    OP_24(0x77, 0x32)
    Sleep(300)
    OP_24(0x77, 0x28)
    Sleep(300)
    OP_24(0x77, 0x1E)
    Sleep(300)
    OP_23(0x77)
    Return()

    # Function_19_46AC end

    def Function_20_46EF(): pass

    label("Function_20_46EF")

    Sleep(2000)
    OP_C8(0x200, 0x46, "C_PLAC04._CH", 0x0, 0x3E8)
    Return()

    # Function_20_46EF end

    SaveToFile()

Try(main)
