from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'P0310   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'P0310.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60183",
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
        'Sealing Stone 2',                      # 9
        'Kevin',                                # 10
        'Ries',                                 # 11
        'Tita',                                 # 12
        'Julia',                                # 13
        'Mueller',                              # 14
        'Josette',                              # 15
        'Joshua',                               # 16
        'Kloe',                                 # 17
        'Sieg',                                 # 18
        'Olivier',                              # 19
        'Zin',                                  # 20
        'Anelace',                              # 21
        'Scherazard',                           # 22
        'Agate',                                # 23
        'Estelle',                              # 24
        'Richard',                              # 25
        'Renne',                                # 26
        'Celeste',                              # 27
        'Gilbert',                              # 28
        'Dummy Julia',                          # 29
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


    AddCharChip(
        'ED6_DT07/CH02891 ._CH',             # 00
        'ED6_DT27/CH03080 ._CH',             # 01
        'ED6_DT27/CH03470 ._CH',             # 02
        'ED6_DT26/CH20743 ._CH',             # 03
        'ED6_DT27/CH03580 ._CH',             # 04
        'ED6_DT27/CH03570 ._CH',             # 05
        'ED6_DT26/CH20742 ._CH',             # 06
        'ED6_DT26/CH20741 ._CH',             # 07
        'ED6_DT27/CH03210 ._CH',             # 08
        'ED6_DT07/CH02323 ._CH',             # 09
        'ED6_DT27/CH03260 ._CH',             # 0A
        'ED6_DT07/CH00070 ._CH',             # 0B
        'ED6_DT07/CH01630 ._CH',             # 0C
        'ED6_DT27/CH03240 ._CH',             # 0D
        'ED6_DT06/CH20053 ._CH',             # 0E
        'ED6_DT27/CH03000 ._CH',             # 0F
        'ED6_DT26/CH20740 ._CH',             # 10
        'ED6_DT27/CH03510 ._CH',             # 11
        'ED6_DT27/CH03750 ._CH',             # 12
        'ED6_DT26/CH20500 ._CH',             # 13
        'ED6_DT26/CH20454 ._CH',             # 14
        'ED6_DT26/CH20621 ._CH',             # 15
        'ED6_DT07/CH02895 ._CH',             # 16
    )

    AddCharChipPat(
        'ED6_DT07/CH02891P._CP',             # 00
        'ED6_DT27/CH03080P._CP',             # 01
        'ED6_DT27/CH03470P._CP',             # 02
        'ED6_DT26/CH20743P._CP',             # 03
        'ED6_DT27/CH03580P._CP',             # 04
        'ED6_DT27/CH03570P._CP',             # 05
        'ED6_DT26/CH20742P._CP',             # 06
        'ED6_DT26/CH20741P._CP',             # 07
        'ED6_DT27/CH03210P._CP',             # 08
        'ED6_DT07/CH02323P._CP',             # 09
        'ED6_DT27/CH03260P._CP',             # 0A
        'ED6_DT07/CH00070P._CP',             # 0B
        'ED6_DT07/CH01630P._CP',             # 0C
        'ED6_DT27/CH03240P._CP',             # 0D
        'ED6_DT06/CH20053P._CP',             # 0E
        'ED6_DT27/CH03000P._CP',             # 0F
        'ED6_DT26/CH20740P._CP',             # 10
        'ED6_DT27/CH03510P._CP',             # 11
        'ED6_DT27/CH03750P._CP',             # 12
        'ED6_DT26/CH20500P._CP',             # 13
        'ED6_DT26/CH20454P._CP',             # 14
        'ED6_DT26/CH20621P._CP',             # 15
        'ED6_DT07/CH02895P._CP',             # 16
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
        X                   = -1910,
        Z                   = 2000,
        Y                   = 90260,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -470,
        Z                   = 2000,
        Y                   = 90150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3630,
        Z                   = 200,
        Y                   = 97420,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1090,
        Z                   = 2200,
        Y                   = 93560,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1630,
        Z                   = 250,
        Y                   = 97420,
        Direction           = 90,
        Unknown2            = 0,
        Unknown3            = 196627,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3400,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 315,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 1300,
        Z                   = 100,
        Y                   = 98950,
        Direction           = 45,
        Unknown2            = 0,
        Unknown3            = 7,
        ChipIndex           = 0x7,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -2200,
        Z                   = 2000,
        Y                   = 91600,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 9,
        ChipIndex           = 0x9,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1930,
        Z                   = 2000,
        Y                   = 86990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 230,
        Z                   = 2000,
        Y                   = 87070,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 11,
        ChipIndex           = 0xB,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -920,
        Z                   = 2000,
        Y                   = 88300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 12,
        ChipIndex           = 0xC,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 120,
        Z                   = 2000,
        Y                   = 88300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 13,
        ChipIndex           = 0xD,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3150,
        Z                   = 2000,
        Y                   = 87000,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 14,
        ChipIndex           = 0xE,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1920,
        Z                   = 2000,
        Y                   = 88740,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 15,
        ChipIndex           = 0xF,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1040,
        Z                   = 100,
        Y                   = 99020,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 16,
        ChipIndex           = 0x10,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -3010,
        Z                   = 2000,
        Y                   = 88790,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 17,
        ChipIndex           = 0x11,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -210,
        Z                   = 2500,
        Y                   = 91540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -1230,
        Z                   = 2000,
        Y                   = 85800,
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
        X                   = -1090,
        Z                   = 2200,
        Y                   = 93300,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 19,
        ChipIndex           = 0x13,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclActor(
        TriggerX            = -1120,
        TriggerZ            = 2000,
        TriggerY            = 93910,
        TriggerRange        = 1000,
        ActorX              = -1120,
        ActorZ              = 3300,
        ActorY              = 93910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_426",          # 00, 0
        "Function_1_56E",          # 01, 1
        "Function_2_68D",          # 02, 2
        "Function_3_6A3",          # 03, 3
        "Function_4_9EF",          # 04, 4
        "Function_5_A18",          # 05, 5
        "Function_6_A41",          # 06, 6
        "Function_7_AF8",          # 07, 7
        "Function_8_F40",          # 08, 8
        "Function_9_10CB",         # 09, 9
        "Function_10_1116",        # 0A, 10
        "Function_11_1158",        # 0B, 11
        "Function_12_119A",        # 0C, 12
        "Function_13_11E1",        # 0D, 13
        "Function_14_203D",        # 0E, 14
        "Function_15_2946",        # 0F, 15
        "Function_16_30C6",        # 10, 16
        "Function_17_3D2D",        # 11, 17
        "Function_18_46CF",        # 12, 18
        "Function_19_472C",        # 13, 19
        "Function_20_4A47",        # 14, 20
        "Function_21_54E4",        # 15, 21
    )


    def Function_0_426(): pass

    label("Function_0_426")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_44C")
    OP_A3(0x2504)
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 21)
    Jump("loc_56D")

    label("loc_44C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_472")
    OP_A3(0x2504)
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 20)
    Jump("loc_56D")

    label("loc_472")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 3)), scpexpr(EXPR_END)), "loc_491")
    OP_A3(0x250B)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 19)
    Jump("loc_56D")

    label("loc_491")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 2)), scpexpr(EXPR_END)), "loc_4B0")
    OP_A3(0x250A)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x9D), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 17)
    Jump("loc_56D")

    label("loc_4B0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 1)), scpexpr(EXPR_END)), "loc_4CF")
    OP_A3(0x2509)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 16)
    Jump("loc_56D")

    label("loc_4CF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A1, 0)), scpexpr(EXPR_END)), "loc_4EE")
    OP_A3(0x2508)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 15)
    Jump("loc_56D")

    label("loc_4EE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 7)), scpexpr(EXPR_END)), "loc_50D")
    OP_A3(0x2507)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x99), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 14)
    Jump("loc_56D")

    label("loc_50D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 6)), scpexpr(EXPR_END)), "loc_52C")
    OP_A3(0x2506)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xD5), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 13)
    Jump("loc_56D")

    label("loc_52C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 5)), scpexpr(EXPR_END)), "loc_542")
    OP_A3(0x2505)
    SetMapFlags(0x10000000)
    Event(0, 8)
    Jump("loc_56D")

    label("loc_542")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_558")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    Event(0, 6)
    Jump("loc_56D")

    label("loc_558")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 2)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_56D")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_56D")

    Return()

    # Function_0_426 end

    def Function_1_56E(): pass

    label("Function_1_56E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x585, 0)), scpexpr(EXPR_END)), "loc_581")
    OP_B1("P0310_1")
    Jump("loc_5B8")

    label("loc_581")

    OP_B1("P0310_2")
    OP_76(0xFF, 0x12, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)
    OP_76(0xFF, 0x15, 0x2, 0x4, 0x8, 0x0, 0x0, 0x0)

    label("loc_5B8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C2, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5CC")
    OP_71(0x402, 0x0)
    ExitThread()
    OP_72(0x1017, 0x0)
    ExitThread()

    label("loc_5CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4C3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_688")
    ClearChrFlags(0x10, 0x80)
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    SetChrPos(0x10, -1120, 3200, 93910, 0)
    LoadEffect(0x7, "map\\mp253_00.eff")
    LoadEffect(0x6, "map\\mp253_01.eff")
    PlayEffect(0x7, 0x7, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x6, 0x6, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Jump("loc_68C")

    label("loc_688")

    OP_64(0x0, 0x1)

    label("loc_68C")

    Return()

    # Function_1_56E end

    def Function_2_68D(): pass

    label("Function_2_68D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_6A2")
    OP_99(0xFE, 0x0, 0x7, 0x3E8)
    Jump("Function_2_68D")

    label("loc_6A2")

    Return()

    # Function_2_68D end

    def Function_3_6A3(): pass

    label("Function_3_6A3")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, 160, 150, 9100, 180)
    SetChrPos(0x10F, 160, 150, 9100, 180)
    SetChrPos(0x107, 160, 150, 9100, 180)
    OP_6D(1370, 0, -5520, 0)
    OP_67(0, 6840, -10000, 0)
    OP_6B(2990, 0)
    OP_6C(45000, 0)
    OP_6E(267, 0)
    FadeToBright(2000, 0)

    def lambda_72E():
        OP_6D(620, 0, 6230, 4000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_72E)

    def lambda_746():
        OP_67(0, 5990, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_746)

    def lambda_75E():
        OP_6B(2990, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_75E)

    def lambda_76E():
        OP_6E(267, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 1, lambda_76E)
    Sleep(3000)
    OP_72(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 0)
    OP_70(0x16, 0xF)
    OP_73(0x16)
    Sleep(300)

    def lambda_79F():
        OP_8E(0xFE, 0xFFFFFF88, 0x0, 0x11A8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_79F)
    Sleep(500)
    OP_43(0x10F, 0x0, 0x0, 0x4)
    Sleep(500)
    OP_43(0x107, 0x0, 0x0, 0x5)
    Sleep(1000)
    OP_71(0x1016, 0x0)
    ExitThread()
    OP_6F(0x16, 15)
    OP_70(0x16, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    OP_62(0x10F, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x10F)
    Sleep(500)

    ChrTalk(    #0
        0x10F,
        (
            "#1446F#5PThere are no signs of life in here at all...\x02\x03",

            "#1440FThis ship must have been abandoned for\x01",
            "at least a few days, if not more.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x107,
        (
            "#063FThe orbal power seems to be completely down,\x01",
            "too.\x02\x03",

            "Makes me wonder if there was some kind of\x01",
            "problem with the engines.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0x109,
        (
            "#1065F#6PHmm... Well, we're not gonna figure anything\x01",
            "out standing here. Let's take a look around.\x02\x03",

            "#1063FThere might be some kind of clue around that'll\x01",
            "help us discover what happened.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2613)
    OP_28(0x29, 0x1, 0x200)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_3_6A3 end

    def Function_4_9EF(): pass

    label("Function_4_9EF")

    OP_8F(0xFE, 0xFFFFFFC4, 0x0, 0x1D60, 0x7D0, 0x0)
    OP_8F(0xFE, 0xFFFFFB82, 0x0, 0x1540, 0x7D0, 0x0)
    Return()

    # Function_4_9EF end

    def Function_5_A18(): pass

    label("Function_5_A18")

    OP_8F(0xFE, 0xFFFFFFC4, 0x0, 0x1D60, 0x7D0, 0x0)
    OP_8F(0xFE, 0x15E, 0x0, 0x17E8, 0x7D0, 0x0)
    Return()

    # Function_5_A18 end

    def Function_6_A41(): pass

    label("Function_6_A41")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrFlags(0x109, 0x80)
    SetChrFlags(0x10F, 0x80)
    SetChrFlags(0x107, 0x80)
    OP_6D(150, 2150, 50240, 0)
    OP_67(0, 5840, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_72(0x402, 0x0)
    ExitThread()
    OP_22(0x9C, 0x0, 0x64)
    OP_0D()
    OP_72(0x1017, 0x0)
    ExitThread()
    OP_6F(0x17, 0)
    OP_70(0x17, 0xF)
    OP_73(0x17)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_71(0x1017, 0x0)
    ExitThread()
    OP_A2(0x2616)
    OP_A2(0x2504)
    NewScene("ED6_DT21/P0312   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_6_A41 end

    def Function_7_AF8(): pass

    label("Function_7_AF8")

    EventBegin(0x0)
    FadeToDark(1000, 0, -1)
    OP_0D()
    Sleep(500)
    SetChrPos(0x109, -1000, 2000, 94980, 180)
    SetChrPos(0x10F, -70, 2000, 94000, 270)
    SetChrPos(0x107, -1930, 2000, 93500, 45)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    SetChrChipByIndex(0x10F, 65535)
    SetChrSubChip(0x10F, 0)
    SetChrChipByIndex(0x107, 65535)
    SetChrSubChip(0x107, 0)
    OP_6D(-410, 2000, 94840, 0)
    OP_67(0, 6770, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(245, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Fade(250)
    SetChrChipByIndex(0x109, 21)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)
    OP_8F(0x10, 0xFFFFFC18, 0xC80, 0x17188, 0x1F4, 0x0)
    Sleep(1000)

    ChrTalk(    #3
        0x109,
        "#1067F#5P...Another one of these, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x107,
        (
            "#560F#6PWow... It's so pretty...\x02\x03",

            "What is it, though?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10F,
        (
            "#1446F#2PIt's called a sealing stone.\x02\x03",

            "#1448FThis is just like that stone you were\x01",
            "imprisoned in, as it so happens.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x107,
        (
            "#064F#6PIt was this pretty?\x02\x03",

            "#066FIt's still weird to think about, but at the\x01",
            "same time, it's kinda nice, too...\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_82(0x7, 0x0)
    OP_82(0x6, 0x0)
    SetChrFlags(0x10, 0x80)
    Sleep(1000)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05Found \x1F\x53\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x353, 1)
    Sleep(500)
    Fade(500)
    SetChrChipByIndex(0x109, 65535)
    SetChrSubChip(0x109, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #8
        0x109,
        (
            "#1065F#5PIf that idea we had about not being able to\x01",
            "proceed without freeing whoever's in these\x01",
            "is true, there's only one thing to do.\x02\x03",

            "#1840FReady to head back to the base and unlock\x01",
            "this little guy?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10F,
        "#1448F#2POf course.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x107,
        "#560F#6PO-Okay!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2619)
    OP_28(0x29, 0x1, 0x800)
    OP_64(0x0, 0x1)
    OP_6D(-1090, 2000, 91550, 0)
    OP_67(0, 7500, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, -1090, 2000, 91550, 180)
    SetChrPos(0x1, -1090, 2000, 91550, 180)
    SetChrPos(0x2, -1090, 2000, 91550, 180)
    OP_69(0x0, 0x0)
    Sleep(500)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_7_AF8 end

    def Function_8_F40(): pass

    label("Function_8_F40")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x109, -1100, 2000, 83500, 0)
    SetChrPos(0x10F, -1100, 2000, 83500, 0)
    SetChrPos(0x107, -1100, 2000, 83500, 0)
    SetChrPos(0x10E, -1100, 2000, 83500, 0)
    OP_9F(0x109, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10F, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x107, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_9F(0x10E, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    OP_6D(-900, 2000, 84250, 0)
    OP_67(0, 7380, -10000, 0)
    OP_6B(3200, 0)
    OP_6C(45000, 0)
    OP_6E(254, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_1013():
        OP_6D(740, 1600, 94700, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1013)

    def lambda_102B():
        OP_67(0, 5310, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_102B)

    def lambda_1043():
        OP_6B(3310, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 2, lambda_1043)

    def lambda_1053():
        OP_6C(32000, 4000)
        ExitThread()

    QueueWorkItem(0x10F, 3, lambda_1053)

    def lambda_1063():
        OP_6E(275, 4000)
        ExitThread()

    QueueWorkItem(0x107, 2, lambda_1063)
    OP_43(0x10E, 0x0, 0x0, 0x9)
    Sleep(800)
    OP_43(0x109, 0x0, 0x0, 0xA)
    Sleep(1000)
    OP_43(0x10F, 0x0, 0x0, 0xB)
    Sleep(1000)
    OP_43(0x107, 0x0, 0x0, 0xC)
    WaitChrThread(0x10E, 0x0)
    WaitChrThread(0x109, 0x0)
    WaitChrThread(0x10F, 0x0)
    WaitChrThread(0x107, 0x0)
    WaitChrThread(0x109, 0x2)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0311   ._SN", 100, 0, 0)
    IdleLoop()
    EventEnd(0x0)
    Return()

    # Function_8_F40 end

    def Function_9_10CB(): pass

    label("Function_9_10CB")


    def lambda_10D1():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_10D1)
    OP_8E(0xFE, 0xFFFFFACE, 0x7D0, 0x1631E, 0x7D0, 0x0)
    OP_8C(0xFE, 315, 400)
    Sleep(500)
    OP_8C(0xFE, 45, 400)
    Sleep(500)
    OP_8C(0xFE, 0, 400)
    Sleep(1000)
    Return()

    # Function_9_10CB end

    def Function_10_1116(): pass

    label("Function_10_1116")


    def lambda_111C():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_111C)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFF786, 0x7D0, 0x15C84, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_10_1116 end

    def Function_11_1158(): pass

    label("Function_11_1158")


    def lambda_115E():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_115E)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFFFFFF42, 0x7D0, 0x15AAE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_11_1158 end

    def Function_12_119A(): pass

    label("Function_12_119A")


    def lambda_11A0():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0xFE, 1, lambda_11A0)
    OP_8E(0xFE, 0xFFFFFBF0, 0x7D0, 0x14EC4, 0x7D0, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    OP_8E(0xFE, 0xFFFFF9CA, 0x7D0, 0x155AE, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_119A end

    def Function_13_11E1(): pass

    label("Function_13_11E1")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mpU70_03.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(5820, 0, 105730, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)

    def lambda_1314():
        OP_6D(500, 2000, 93390, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1314)

    def lambda_132C():
        OP_67(0, 5470, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_132C)

    def lambda_1344():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1344)

    def lambda_1354():
        OP_6E(315, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1354)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #11
        0x14,
        "#176F#5P...All right. Everyone is now in position.\x02",
    )

    CloseMessageWindow()

    def lambda_13B0():
        OP_6D(1000, 2000, 93000, 800)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_13B0)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x18, 90, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(30)

    ChrTalk(    #12
        0x18,
        "#1162F#6PIf you would, Celeste?\x02",
    )

    CloseMessageWindow()

    def lambda_1403():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_1403)
    Sleep(100)

    def lambda_1416():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1416)
    Sleep(100)

    def lambda_1429():
        OP_8C(0xFE, 45, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1429)
    Sleep(100)
    OP_8C(0x21, 45, 400)
    Sleep(300)

    ChrTalk(    #13
        0x22,
        (
            "#1615F#5P#12COf course.\x02\x03",

            "#1610FPlease focus your minds, everyone.\x02\x03",

            "Focus on the image of this ship taking\x01",
            "flight into the sky.\x02\x03",

            "That is all you need to do.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x11,
        "#1078F#6PGot it.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x1F,
        "#1016F#6PAhaha... This is gonna be easy.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x12,
        (
            "#1932F#12PIt's not a sight I've had the pleasure of seeing\x01",
            "before, but I can easily imagine how beautiful\x01",
            "it must be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #17
        0x23,
        (
            "#1224F#11PC-Come to think of it...\x02\x03",

            "#1223FI was in this ship when I was being transported\x01",
            "to a cell in Leiston Fortress...\x02\x03",

            "#1228F*sigh* That was when my life really started to go\x01",
            "off the rails...\x02",
        )
    )

    CloseMessageWindow()

    def lambda_1675():
        OP_6D(1000, 2000, 92000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1675)

    def lambda_168D():
        OP_67(0, 5180, -10000, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_168D)

    def lambda_16A5():
        OP_6B(3080, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_16A5)

    def lambda_16B5():
        OP_6E(323, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_16B5)
    OP_8C(0x22, 180, 400)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #18
        0x22,
        (
            "#1615F#5P#12CIf you are going to remain on board, sir, I would\x01",
            "kindly ask that you cooperate.\x02\x03",

            "#1610FFor this ship to fly again, everyone on board it\x01",
            "must be thinking of the same thing.\x02\x03",

            "...If you're not willing to participate, you could\x01",
            "always climb off and remain in the garden.#0C\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(500)

    def lambda_180E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_180E)
    Sleep(50)

    def lambda_1821():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1821)
    Sleep(50)
    SetChrFlags(0x18, 0x20)

    def lambda_1839():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1839)
    Sleep(50)

    def lambda_184C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_184C)
    Sleep(50)

    def lambda_185F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_185F)
    Sleep(50)

    def lambda_1872():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1872)
    Sleep(50)

    def lambda_1885():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1885)
    Sleep(50)

    def lambda_1898():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1898)
    Sleep(50)

    def lambda_18AB():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_18AB)
    Sleep(50)

    def lambda_18BE():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_18BE)
    Sleep(50)
    OP_62(0x23, 0x0, 2000, 0x28, 0x2B, 0x64, 0x3)
    Sleep(500)

    ChrTalk(    #19
        0x23,
        (
            "#1224F#12PN-No, I can cooperate! For realsies!\x02\x03",

            "#1228F*whine* How did I ever get myself into this\x01",
            "mess in the first place...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x1F,
        "#1007F#5P*sigh*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x21,
        "#1306F#5PHeehee. Well, aren't you being a good boy?\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_20(0x7D0)

    def lambda_19C3():
        OP_6D(1000, 2000, 93000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_19C3)

    def lambda_19DB():
        OP_67(0, 5470, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_19DB)

    def lambda_19F3():
        OP_6B(3000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_19F3)

    def lambda_1A03():
        OP_6E(315, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1A03)
    OP_8C(0x22, 0, 400)
    Sleep(50)

    def lambda_1A1F():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1A1F)
    Sleep(50)

    def lambda_1A32():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_1A32)
    Sleep(50)

    def lambda_1A45():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_1A45)
    Sleep(50)

    def lambda_1A58():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_1A58)
    Sleep(50)

    def lambda_1A6B():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_1A6B)
    Sleep(50)

    def lambda_1A7E():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_1A7E)
    Sleep(50)

    def lambda_1A91():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_1A91)
    Sleep(50)

    def lambda_1AA4():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_1AA4)
    Sleep(50)

    def lambda_1AB7():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_1AB7)
    Sleep(50)

    def lambda_1ACA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_1ACA)
    WaitChrThread(0xEE, 0x0)
    ClearChrFlags(0x18, 0x20)
    Sleep(500)
    OP_21()

    ChrTalk(    #22
        0x22,
        (
            "#1616F#5P#12CWell, now that we have everyone's support,\x01",
            "I think it's time to begin.#0C\x02",
        )
    )

    CloseMessageWindow()
    Fade(250)
    SetChrChipByIndex(0x22, 22)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(500)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x1, 0x0, 0x22, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(1000)
    OP_1D(0x99)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_22(0x146, 0x1, 0x46)
    PlayEffect(0x1, 0xFF, 0x11, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x12, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x13, 0, 600, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x14, 0, 600, -200, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x15, -100, 600, -100, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x16, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 0, 1000, 0, 0, 0, 0, 1500, 2800, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 0, 700, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #23
        0x11,
        "#1079F#6POh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x12,
        "#1934F#12PI-Is this...?\x02",
    )

    CloseMessageWindow()
    OP_A2(0x2C28)
    OP_22(0x9D, 0x0, 0x64)
    Fade(1000)
    OP_79(0x0, 0x2)
    OP_79(0x1, 0x2)
    OP_79(0x2, 0x2)
    OP_79(0x3, 0x2)
    OP_79(0x4, 0x2)
    OP_79(0x5, 0x2)
    OP_79(0x6, 0x2)
    OP_79(0x7, 0x2)
    OP_79(0x8, 0x2)
    OP_79(0x9, 0x2)
    OP_79(0xA, 0x2)
    OP_79(0xB, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0xD, 0x2)
    OP_79(0xE, 0x2)
    OP_79(0xF, 0x2)
    OP_79(0x10, 0x2)
    OP_79(0x11, 0x2)
    OP_79(0x12, 0x2)
    OP_79(0x13, 0x2)
    OP_79(0x14, 0x2)
    OP_79(0x15, 0x2)
    OP_79(0x16, 0x2)
    OP_79(0x17, 0x2)
    OP_79(0x18, 0x2)
    OP_7A(0x19, 0x2)
    OP_7A(0x1A, 0x2)
    OP_7A(0x1B, 0x2)
    OP_78(0xE6, 0xFA, 0xFF)
    OP_7B()
    OP_76(0xFF, 0x12, 0x2, 0x4, 0x8, 0x64, 0x0, 0xF)
    OP_76(0xFF, 0x15, 0x2, 0x4, 0x8, 0x64, 0x0, 0xF)
    OP_0D()
    Sleep(2000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_13_11E1 end

    def Function_14_203D(): pass

    label("Function_14_203D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    LoadEffect(0x1, "map\\mpU70_03.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    SetChrChipByIndex(0x22, 22)
    SetChrSubChip(0x22, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 5470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)
    PlayEffect(0x1, 0xFF, 0x22, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x11, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x12, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1F, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x13, 0, 500, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x14, 0, 600, -200, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x15, -200, 500, -100, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x16, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x17, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x18, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1A, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1B, 0, 1000, 0, 0, 0, 0, 1500, 2800, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1C, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1D, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x1E, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x20, 0, 500, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x21, 0, 700, 0, 0, 0, 0, 1000, 2000, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x1, 0xFF, 0x23, 0, 800, 0, 0, 0, 0, 1200, 2300, 700, 0xFF, 0, 0, 0, 0)
    OP_22(0x146, 0x1, 0x46)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(1000)
    Fade(1000)
    OP_22(0x138, 0x0, 0x64)
    OP_23(0x146)
    LoadEffect(0x1, "map\\mp049_21.eff")
    OP_0D()
    Sleep(300)
    Fade(250)
    SetChrChipByIndex(0x22, 0)
    SetChrSubChip(0x22, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #25
        0x14,
        (
            "#179F#5PActivation complete.\x02\x03",

            "#171FThe Arseille is now ready to depart at any time.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #26
        0x18,
        "Sieg",
        "#311F#5PScree!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x13,
        "#061F#11PWe did it!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x17,
        (
            "#1514F#5PWhew... I didn't want to think about what\x01",
            "would happen if that failed...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x20,
        "#119F#5PWell, we're finally ready.\x02",
    )

    CloseMessageWindow()
    SetChrFlags(0x18, 0x20)
    SetChrFlags(0x18, 0x20)
    OP_8C(0x18, 180, 400)
    Sleep(300)

    ChrTalk(    #30
        0x18,
        "#1382F#5PWhat should we do, Kevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x11,
        (
            "#1075F#6PIf we're ready, I'd say we should get going\x01",
            "immediately.\x02\x03",

            "#1063FOur destination's set...so let's go there and\x01",
            "finish this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x18,
        "#1383F#5PUnderstood.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x18, 0, 400)
    ClearChrFlags(0x18, 0x20)
    Sleep(300)

    ChrTalk(    #33
        0x18,
        "#1162F#6PIf you would, then, Julia?\x02",
    )

    CloseMessageWindow()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #34
        0x14,
        "#170F#5PCertainly, Your Highness.\x02",
    )

    CloseMessageWindow()

    def lambda_27E4():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_27E4)

    def lambda_27FC():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_27FC)

    def lambda_2814():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2814)

    def lambda_2824():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2824)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)
    Sleep(150)

    ChrTalk(    #35
        0x14,
        (
            "#176F#11PHenceforth, this ship will be accelerating to\x01",
            "maximum battle speed and exiting the planes.\x02\x03",

            "#178FStart all engines...\x02\x03",

            "...and advance!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(90, 130, -1, -1)
    SetChrName("Crew Members")

    AnonymousTalk(    #36
        "\x07\x00#4SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2505)
    NewScene("ED6_DT21/M7007   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_14_203D end

    def Function_15_2946(): pass

    label("Function_15_2946")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4980, -10000, 0)
    OP_6B(3070, 0)
    OP_6C(45000, 0)
    OP_6E(319, 0)

    def lambda_2A66():

        label("loc_2A66")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_2A66")

    QueueWorkItem2(0xEE, 0, lambda_2A66)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #37
        0x1C,
        "#814F#11PW-Wow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x15,
        "#277F#5PSo this is what the planes really look like...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x1A,
        (
            "#1541F#11PHeh. It's like being surrounded by a giant\x01",
            "kaleidoscope.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_2B68():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2B68)

    def lambda_2B80():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_2B80)

    def lambda_2B98():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_2B98)

    def lambda_2BA8():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_2BA8)
    WaitChrThread(0xEE, 0x0)
    Sleep(300)

    ChrTalk(    #40
        0x16,
        (
            "#210F#11P3,000 SPH... 3,100... 3,200...\x02\x03",

            "#216FW-Wait a second... 3,500?! 3,800?! 4,300?!\x02\x03",

            "We're now going at 5,000 SPH!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #41
        0x14,
        "#173F#11PWhat...?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #42
        0x18,
        (
            "#1164F#6PBut the Arseille should only be able to reach\x01",
            "3,600...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #43
        0x22,
        (
            "#1616F#11P#12CI can only assume this is the result of how well\x01",
            "you were able to combine your thoughts as one.\x02\x03",

            "#1611FThis must be the Arseille's theoretical maximum\x01",
            "capability rather than its real world maximum.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #44
        0x13,
        "#067F#11PTh-This is amazing...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x11,
        (
            "#1078F#6PShouldn't take us long to reach our destination\x01",
            "at this kinda speed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x12,
        "#1938F#11PAre we still in the planes, incidentally?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x20,
        "#110F#5PYes, but we shouldn't be for much longer.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)

    ChrTalk(    #48
        0x16,
        (
            "#214F#11PDetecting a barrier in front of us!\x02\x03",

            "120 seconds until impact!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #49
        0x14,
        (
            "#176F#6PFull speed ahead! Prepare the main cannon for\x01",
            "rapid fire!\x02\x03",

            "#172FWe're going to use it to force our way through!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #50
        0x15,
        "#271F#5P#3SRight!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2508)
    NewScene("ED6_DT21/E0811   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_15_2946 end

    def Function_16_30C6(): pass

    label("Function_16_30C6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(5820, 0, 104730, 0)
    OP_67(0, 6470, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(315, 0)

    def lambda_31E6():

        label("loc_31E6")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_31E6")

    QueueWorkItem2(0xEE, 0, lambda_31E6)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()

    def lambda_320F():
        OP_6D(500, 2000, 93390, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_320F)

    def lambda_3227():
        OP_6D(1000, 2000, 93000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3227)

    def lambda_323F():
        OP_67(0, 4370, -10000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_323F)

    def lambda_3257():
        OP_6B(3000, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3257)

    def lambda_3267():
        OP_6E(315, 5000)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3267)
    FadeToBright(1000, 0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #51
        0x1E,
        "#052F#6PWhoa...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x12,
        (
            "#1942F#11PSo this is how Phantasma looks outside of the\x01",
            "planes...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #53
        0x1D,
        "#1522F#11PIt's nothing but a barren wasteland...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x22,
        (
            "#1615F#5P#12COur destination's coordinates are as\x01",
            "I mentioned earlier.\x02\x03",

            "#1610FAs long as we keep heading straight,\x01",
            "we should reach it before long.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x1F,
        (
            "#1016F#6PWhew... Guess this is our chance to take a\x01",
            "breather.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #56
        0x21,
        (
            "#261F#6PThat was a real thrill, now, wasn't it?\x02\x03",

            "#265FEven Ouroboros doesn't have any airships quite\x01",
            "this fast.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #57
        0x1B,
        (
            "#074F#11PIt's only just starting to hit me just how vast\x01",
            "Phantasma actually is, though.\x02\x03",

            "#072FThe planes felt big enough as it was, but this\x01",
            "area around them seems even bigger.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x1A,
        (
            "#1545F#6PIndeed... It's astounding to believe that all of\x01",
            "this is only a subsystem of the Aureole's.\x02\x03",

            "#1540FIt also makes it even harder to believe that the\x01",
            "Aureole could have disappeared as it did.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #59
        0x11,
        (
            "#1841F#5PYeah... I'm with you.\x02\x03",

            "#1063FThere's no way that something capable of making\x01",
            "an entire other world like this could just vanish all\x01",
            "of a sudden.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_AD(0x24016C, 0x0, 0x0, 0x1F4)
    Sleep(2000)
    OP_AE(0x1F4)
    Sleep(1000)

    ChrTalk(    #60
        0x11,
        "#1067F#5P(Which means he probably collected it.)\x02",
    )

    CloseMessageWindow()
    OP_62(0x1F, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #61
        0x1F,
        "#1004F#6PIs something wrong, Kevin?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x11, 180, 400)
    Sleep(300)

    ChrTalk(    #62
        0x11,
        (
            "#1075F#5POh, nah... It's fine.\x02\x03",

            "#1060FI doubt what I'm thinking about has any direct\x01",
            "connection to what's happening here.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x1F,
        "#1015F...?#6P\x02",
    )

    CloseMessageWindow()
    OP_20(0x3E8)

    def lambda_37D4():
        OP_6D(760, 1800, 96310, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_37D4)

    def lambda_37EC():
        OP_67(0, 4800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_37EC)

    def lambda_3804():
        OP_6B(3030, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_3804)

    def lambda_3814():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_3814)
    LoadEffect(0x1, "map\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)

    def lambda_3893():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_3893)
    WaitChrThread(0xEE, 0x0)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #64
        0x16,
        "#216F#11PWh-What the...?\x02",
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #65
        0x16,
        (
            "#214F#11P#2SThere's a small flying object approaching us 200\x01",
            "selge from behind!\x02",
        )
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x23, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #66
        0x14,
        "#173F#11PWhat?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x18,
        (
            "#1163F#11PHow could there be another airship out here\x01",
            "other than ours?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x22,
        (
            "#1613F#11P#12CNo...\x02\x03",

            "#1612FIt seems to be a pursuer from the planes.#0C\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x11,
        "#1847F#6PA pursuer...?!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #70
        0x14,
        (
            "#172F#6PBring down the main monitor!\x02\x03",

            "Try and get the pursuer up on it using the ship's\x01",
            "rear camera!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x17,
        "#1502F#5PUnderstood!\x02",
    )

    CloseMessageWindow()
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)

    def lambda_3C8B():
        OP_67(0, 5150, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_3C8B)
    OP_72(0x40C, 0x0)
    ExitThread()
    OP_6F(0xC, 0)
    OP_70(0xC, 0x3C)
    Sleep(50)
    OP_22(0x127, 0x0, 0x64)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_73(0xC)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x4)
    OP_74(0xC, 0x8, 0x4)
    OP_74(0xC, 0xA, 0x4)
    OP_0D()
    OP_1D(0x9D)
    Sleep(500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2509)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_16_30C6 end

    def Function_17_3D2D(): pass

    label("Function_17_3D2D")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    ClearChrFlags(0x23, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 5560, -10000, 0)
    OP_6B(3030, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_3E86():

        label("loc_3E86")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_3E86")

    QueueWorkItem2(0xEE, 0, lambda_3E86)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #72
        0x1F,
        "#1020F#6PTh-That's...!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #73
        0x17,
        "#1506F#5PWhat's a silver Dragion doing here?!\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x1, 0x20)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F51")

    ChrTalk(    #74
        0x21,
        "#267F#6PHuh... I've never seen one in that color before.\x02",
    )

    CloseMessageWindow()

    label("loc_3F51")


    ChrTalk(    #75
        0x16,
        (
            "#212F#11PThis is bad... It's going faster than us!\x02\x03",

            "At this rate, it's gonna catch up before long.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x15,
        (
            "#276F#5PThat wouldn't be likely to end well, either.\x02\x03",

            "The Arseille has been taken down by a Dragion\x01",
            "once before as it is.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x17, 0x1, 0x20)"), scpexpr(EXPR_END)), "loc_40F9")

    ChrTalk(    #77
        0x21,
        (
            "#267F#6PHmm... I suppose I could always call Pater-Mater,\x01",
            "but I'm not sure what good he'd do.\x02\x03",

            "#268FHe doesn't have the kind of maneuverability that\x01",
            "thing does when in the air.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_40F9")


    ChrTalk(    #78
        0x14,
        "#175F#6PUgh...\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(500)

    ChrTalk(    #79
        0x14,
        (
            "#177F#11PPrepare for midair battle! Turn the ship and\x01",
            "intercept that Dragion!\x02",
        )
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()

    ChrTalk(    #80
        0x23,
        "#1226F#11P...No. There's no need to do that.\x02",
    )

    CloseMessageWindow()
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4330():
        OP_6D(3080, 0, 92930, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4330)

    def lambda_4348():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x22, 1, lambda_4348)
    Sleep(50)

    def lambda_435B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_435B)
    Sleep(50)

    def lambda_436E():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_436E)
    Sleep(50)
    SetChrFlags(0x18, 0x20)

    def lambda_4386():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x18, 1, lambda_4386)
    Sleep(50)

    def lambda_4399():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1F, 1, lambda_4399)
    Sleep(50)

    def lambda_43AC():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x21, 1, lambda_43AC)
    Sleep(50)

    def lambda_43BF():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_43BF)
    Sleep(50)

    def lambda_43D2():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1C, 1, lambda_43D2)
    Sleep(50)

    def lambda_43E5():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_43E5)
    Sleep(50)

    def lambda_43F8():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_43F8)
    Sleep(50)

    def lambda_440B():
        OP_8C(0xFE, 135, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_440B)
    Sleep(50)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #81
        0x14,
        "#173F#5PWhat?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x11,
        "#1063F#5PThis is new.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x23,
        (
            "#1226F#12PHa. Ha. Haaaaaa.\x02\x03",

            "#1221FThe time has finally come to show you\x01",
            "all my true brilliance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x11,
        "#1064F#5P...You actually got some?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x1F,
        "#1019F#5PYou feeling all right, buddy?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x12,
        (
            "#1942F#5PPerhaps you ought to go and rest in the medical\x01",
            "room. You seem confused.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x23,
        (
            "#1221F#12PHahaha! The rest of you can just stay there\x01",
            "and watch.\x02\x03",

            "You're about to see a REAL hero in action!\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x23, 180, 400)
    OP_43(0x23, 0x0, 0x0, 0x12)
    Sleep(500)

    def lambda_45F6():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1E, 1, lambda_45F6)
    Sleep(100)

    def lambda_4609():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1B, 1, lambda_4609)
    Sleep(100)

    def lambda_461C():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1A, 1, lambda_461C)
    Sleep(100)

    def lambda_462F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x1D, 1, lambda_462F)
    WaitChrThread(0x23, 0x0)
    Sleep(1500)

    def lambda_4647():
        OP_6D(3080, 0, 92930, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_4647)
    WaitChrThread(0xEE, 0x0)

    ChrTalk(    #88
        0x1C,
        "#814F...#5PAaaaaand he's gone.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #89
        0x1F,
        "#1007F#5PWhat's gotten into that goofball?\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x250A)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_17_3D2D end

    def Function_18_46CF(): pass

    label("Function_18_46CF")

    OP_8E(0xFE, 0xFFFFFB78, 0x7D0, 0x14D16, 0xBB8, 0x0)
    OP_22(0x6D, 0x0, 0x64)
    Sleep(500)

    def lambda_46F3():
        OP_6D(3080, 0, 91500, 1000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_46F3)

    def lambda_470B():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x190)
        ExitThread()

    QueueWorkItem(0xFE, 2, lambda_470B)
    OP_8E(0xFE, 0xFFFFFB14, 0x7D0, 0x14730, 0xFA0, 0x0)
    Return()

    # Function_18_46CF end

    def Function_19_472C(): pass

    label("Function_19_472C")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_4870():

        label("loc_4870")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_4870")

    QueueWorkItem2(0xEE, 0, lambda_4870)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #90
        0x1F,
        "#1004F#6P*gawp*\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #91
        0x11,
        (
            "#1079F#6PHe had that thing when we were in\x01",
            "Grancel!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x12,
        "#1934F#12PI had no idea that's how you rode it...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #93
        0x16,
        (
            "#214F#11PI-I know that thing!\x02\x03",

            "So he WAS the one who attacked the Bobcat!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x21,
        (
            "#263F#6PHmm... Maybe his idea wasn't so stupid\x01",
            "after all.\x02\x03",

            "#1306FIt might not be as strong as that Dragion,\x01",
            "but in terms of maneuverability, it actually\x01",
            "keeps up fairly well.\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x250B)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_19_472C end

    def Function_20_4A47(): pass

    label("Function_20_4A47")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)
    OP_74(0xC, 0x6, 0x5)
    OP_74(0xC, 0x8, 0x5)
    OP_74(0xC, 0xA, 0x5)

    def lambda_4B8B():

        label("loc_4B8B")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_4B8B")

    QueueWorkItem2(0xEE, 0, lambda_4B8B)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #95
        0x12,
        "#1934F#12PHe's actually fighting well...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #96
        0x1D,
        "#1536F#12PYeah. I'm impressed!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x1E,
        (
            "#051F#6PHeh. I always figured he was just some loser,\x01",
            "but maybe he's got more guts than I thought.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x1C,
        (
            "#811F#12PYeah! I feel like I'm seeing him in a whole new\x01",
            "light now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #99
        0x15,
        (
            "#276F#5PStill, while he's putting up a valiant effort,\x01",
            "I can't see him being able to actually take it\x01",
            "down...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #100
        0x14,
        (
            "#176F#6P...Indeed.\x02\x03",

            "#178FPerhaps it would be best for us to turn around\x01",
            "and engage it directly.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(250, 100, -1, -1)
    SetChrName("Voice")

    AnonymousTalk(    #101
        "\x07\x05I told you, there isn't any need for that!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_4F4D():
        OP_67(0, 3950, -10000, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_4F4D)

    def lambda_4F65():
        OP_6D(200, 2400, 93390, 1200)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_4F65)
    WaitChrThread(0xEE, 0x1)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x6)
    OP_74(0xC, 0x8, 0x6)
    OP_74(0xC, 0xA, 0x6)
    OP_0D()
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #102
        0x14,
        "#173F#6P...Oh.\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("Gilbert")

    AnonymousTalk(    #103
        (
            "\x07\x05I mean it! Get going!\x02\x03",

            "It's not like I would've been able to help you\x01",
            "out in battle much, anyway!\x02\x03",

            "I might as well do my part some other way!\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #104
        0x14,
        "#178F#6PYou're certain about this?\x02",
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("Gilbert")

    AnonymousTalk(    #105
        (
            "\x07\x05Sure, I might not be able to knock it out of\x01",
            "the sky, but I can get it out of your way!\x02\x03",

            "Then when you've safely escaped, I'll make\x01",
            "my own retreat and follow on after you.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    ChrTalk(    #106
        0x14,
        (
            "#170F#6P...\x02\x03",

            "#179FUnderstood. I shall be praying for your \x01",
            "success.\x02",
        )
    )

    CloseMessageWindow()
    SetMessageWindowPos(240, 160, -1, -1)
    SetChrName("Gilbert")

    AnonymousTalk(    #107
        "\x07\x05Heh. Same to you!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_22(0x9D, 0x0, 0x64)
    Sleep(200)
    Fade(500)
    OP_74(0xC, 0x6, 0x0)
    OP_74(0xC, 0x8, 0x0)
    OP_74(0xC, 0xA, 0x0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #108
        0x1F,
        "#1008F#6PWow...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x1B,
        "#573F#12PHeh. He sure knows how to steal the spotlight.\x02",
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)

    ChrTalk(    #110
        0x16,
        (
            "#210F#11PHonestly, he should be fine. He's pretty skilled at\x01",
            "operating that thing.\x02\x03",

            "He gave me and my brothers hell when he attacked\x01",
            "us before.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #111
        0x11,
        "#1840F#6PWell, I guess all we can do is believe in him now.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #112
        0x12,
        "#1937F#12PLet us pray to Aidios for his safety.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #113
        0x14,
        "#179F#5P...Indeed.\x02",
    )

    CloseMessageWindow()
    Sleep(150)

    def lambda_53A1():
        OP_6D(760, 1800, 96310, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_53A1)

    def lambda_53B9():
        OP_67(0, 4800, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_53B9)

    def lambda_53D1():
        OP_6B(3030, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_53D1)

    def lambda_53E1():
        OP_6E(316, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_53E1)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #114
        0x14,
        (
            "#177F#11PAll engines, full speed ahead!\x02\x03",

            "Don't slow down until we reach our destination!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(400)
    SetMessageWindowPos(50, 150, -1, -1)
    SetChrName("Crew Members")

    AnonymousTalk(    #115
        "\x07\x00#4SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0x12C, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(300)
    FadeToDark(1000, 0, -1)
    OP_0D()
    SetMapFlags(0x2000000)
    OP_A2(0x2504)
    OP_A2(0x2505)
    NewScene("ED6_DT21/P0800   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_20_4A47 end

    def Function_21_54E4(): pass

    label("Function_21_54E4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp259_01.eff")
    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    ClearChrFlags(0x22, 0x80)
    OP_9F(0x22, 0xFF, 0xFF, 0xFF, 0xDC, 0x0)
    PlayEffect(0x0, 0x7, 0x22, 0, 800, 0, 0, 0, 0, 1600, 3300, 0, 0xFF, 0, 0, 0, 0)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x1F, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x24, 0x80)
    OP_9F(0x24, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    ClearChrFlags(0x18, 0x80)
    ClearChrFlags(0x1A, 0x80)
    ClearChrFlags(0x1B, 0x80)
    ClearChrFlags(0x1C, 0x80)
    ClearChrFlags(0x1D, 0x80)
    ClearChrFlags(0x1E, 0x80)
    ClearChrFlags(0x20, 0x80)
    ClearChrFlags(0x21, 0x80)
    OP_6D(200, 2000, 93390, 0)
    OP_67(0, 4640, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x3C)

    def lambda_560D():

        label("loc_560D")

        OP_7C(0x1, 0x1, 0x7D0, 0x64)
        OP_48()
        Jump("loc_560D")

    QueueWorkItem2(0xEE, 0, lambda_560D)
    OP_22(0x7A, 0x1, 0x46)
    OP_82(0x80, 0x0)
    OP_72(0x40E, 0x0)
    ExitThread()
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #116
        0x1F,
        "#1015F#5PHuh? You guys hear something?\x02",
    )

    CloseMessageWindow()
    OP_8C(0x21, 90, 400)
    Sleep(300)

    ChrTalk(    #117
        0x21,
        "#267F#6PI didn't...\x02",
    )

    CloseMessageWindow()

    def lambda_5696():
        OP_6D(760, 1800, 96310, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5696)

    def lambda_56AE():
        OP_67(0, 4800, -10000, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_56AE)

    def lambda_56C6():
        OP_6B(3030, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_56C6)

    def lambda_56D6():
        OP_6E(316, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_56D6)
    LoadEffect(0x1, "map\\\\mp001_00.eff")
    PlayEffect(0x1, 0x0, 0xFF, -4410, 1230, 98850, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(800)
    OP_22(0xAB, 0x0, 0x64)
    Sleep(500)
    OP_82(0x0, 0x0)

    def lambda_5746():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0x21, 0, lambda_5746)
    OP_62(0x16, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    Sleep(300)

    ChrTalk(    #118
        0x16,
        (
            "#214F#11PDetecting a giant structure 120 selge ahead of us!\x02\x03",

            "I think this is where we were headed for!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x24, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x13, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x15, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x20, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x18, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x22, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x11, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x12, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1F, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x21, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1B, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x1C, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1D, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x1E, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #119
        0x14,
        (
            "#176F#6PWe should be able to get a visual on it before\x01",
            "long, then, if it's that close.\x02\x03",

            "#178FJoshua, could you move the main camera to\x01",
            "face it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #120
        0x17,
        (
            "#1500F#5POf course.\x02\x03",

            "#1503FZooming in as far as I can on the target...\x02\x03",

            "...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x17, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(2000)
    OP_63(0x17)
    Sleep(500)
    OP_62(0x17, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #121
        0x17,
        "#1506F#5PI've got it! Putting it up on the screen!\x02",
    )

    CloseMessageWindow()
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0x9D, 0x0, 0x64)
    OP_C5(0x0, 0x0, 0x0, 0x280, 0x1E0, 0x0, 0x0, 0x300, 0x200, 0x0, 0x0, 0x280, 0x1E0, 0xFFFFFF, 0x0, "C_VIS479._CH")
    OP_C6(0x0, 0x3, -1, 1000, 0)
    Sleep(2000)
    OP_C6(0x0, 0x0, -330000, -265000, 8000)
    OP_C6(0x0, 0x1, 2000, 2000, 8000)
    Sleep(5000)
    OP_C6(0x0, 0x3, 16777215, 1000, 0)
    Sleep(2000)
    OP_74(0xC, 0x6, 0x7)
    OP_74(0xC, 0x8, 0x7)
    OP_74(0xC, 0xA, 0x7)
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(0)
    OP_6D(250, 2000, 94350, 0)
    OP_67(0, 3930, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(323, 0)
    OP_8C(0x18, 45, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #122
        0x1F,
        "#1004F#6PWh-What's THAT?!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #123
        0x13,
        (
            "#560F#6PWow... It looks like something out of a\x01",
            "fairy tale!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #124
        0x18,
        (
            "#1169F#6PIt looks like some sort of palace...\x02\x03",

            "#1162FOr perhaps castle is the more appropriate word\x01",
            "for it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #125
        0x20,
        (
            "#112F#6PSo that is where the Lord of Phantasma waits for\x01",
            "us--a great castle standing in the wilderness...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #126
        0x1A,
        "#1545F#12PQuite the romantic concept.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #127
        0x12,
        "#1942F#12PRufina is waiting for us there?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #128
        0x11,
        (
            "#1065F#6PNo doubt about it.\x02\x03",

            "#1840FThat's one scary-looking castle she's built herself,\x01",
            "huh? I'm already shaking in my Stregas.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(150)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    Sleep(300)

    ChrTalk(    #129
        0x14,
        "#178F#5P...What should we do now, Kevin?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #130
        0x11,
        (
            "#1067F#6PHmm...\x02\x03",

            "#1060FLet's try and get closer and see if there's a way in.\x01",
            "Careful, though.\x02\x03",

            "I don't think our arrival's going to come as much of\x01",
            "a surprise for her.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #131
        0x14,
        "#176F#5PUnderstood.\x02",
    )

    CloseMessageWindow()

    def lambda_5F6C():
        OP_6D(730, 2000, 97690, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_5F6C)

    def lambda_5F84():
        OP_67(0, 4430, -10000, 1300)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_5F84)
    OP_51(0x14, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(200)
    OP_8C(0x18, 0, 400)
    WaitChrThread(0xEE, 0x0)
    Sleep(500)

    ChrTalk(    #132
        0x14,
        (
            "#172F#11PArseille, decelerate!\x02\x03",

            "As soon as we reach the target, begin to slowly\x01",
            "circle around it!\x02",
        )
    )

    CloseMessageWindow()
    OP_51(0x16, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x13, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x15, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    OP_51(0x17, 0x8, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(50)
    Sleep(500)
    SetMessageWindowPos(80, 150, -1, -1)
    SetChrName("Crew Members")

    AnonymousTalk(    #133
        "\x07\x00#4SYes, ma'am!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_24(0x7A, 0x3C)
    Sleep(500)
    OP_24(0x7A, 0x32)
    Sleep(500)
    OP_24(0x7A, 0x28)
    Sleep(500)
    OP_24(0x7A, 0x1E)
    Sleep(500)
    OP_24(0x7A, 0x14)
    Sleep(500)
    OP_24(0x7A, 0xA)
    Sleep(500)
    OP_23(0x7A)
    OP_A2(0x2504)
    NewScene("ED6_DT21/M7400   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_21_54E4 end

    SaveToFile()

Try(main)
