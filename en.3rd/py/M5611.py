from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5611   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5611.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60233",
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
        'Carna',                                # 9
        'Jaeger Carna',                         # 10
        'Jaeger Carna',                         # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
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
        'ED6_DT29/CH14950 ._CH',             # 00
        'ED6_DT29/CH14951 ._CH',             # 01
        'ED6_DT29/CH14960 ._CH',             # 02
        'ED6_DT29/CH14961 ._CH',             # 03
        'ED6_DT07/CH01240 ._CH',             # 04
        'ED6_DT07/CH00400 ._CH',             # 05
        'ED6_DT07/CH00401 ._CH',             # 06
        'ED6_DT07/CH00402 ._CH',             # 07
        'ED6_DT07/CH00404 ._CH',             # 08
        'ED6_DT07/CH00405 ._CH',             # 09
        'ED6_DT27/CH04640 ._CH',             # 0A
        'ED6_DT27/CH04641 ._CH',             # 0B
        'ED6_DT27/CH04642 ._CH',             # 0C
        'ED6_DT29/CH15160 ._CH',             # 0D
        'ED6_DT29/CH15161 ._CH',             # 0E
        'ED6_DT29/CH15170 ._CH',             # 0F
        'ED6_DT29/CH15171 ._CH',             # 10
    )

    AddCharChipPat(
        'ED6_DT29/CH14950P._CP',             # 00
        'ED6_DT29/CH14951P._CP',             # 01
        'ED6_DT29/CH14960P._CP',             # 02
        'ED6_DT29/CH14961P._CP',             # 03
        'ED6_DT07/CH01240P._CP',             # 04
        'ED6_DT07/CH00400P._CP',             # 05
        'ED6_DT07/CH00401P._CP',             # 06
        'ED6_DT07/CH00402P._CP',             # 07
        'ED6_DT07/CH00404P._CP',             # 08
        'ED6_DT07/CH00405P._CP',             # 09
        'ED6_DT27/CH04640P._CP',             # 0A
        'ED6_DT27/CH04641P._CP',             # 0B
        'ED6_DT27/CH04642P._CP',             # 0C
        'ED6_DT29/CH15160P._CP',             # 0D
        'ED6_DT29/CH15161P._CP',             # 0E
        'ED6_DT29/CH15170P._CP',             # 0F
        'ED6_DT29/CH15171P._CP',             # 10
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
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
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -75300,
        Z                   = 0,
        Y                   = 90720,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83650,
        Z                   = 0,
        Y                   = -50430,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -83370,
        Z                   = 0,
        Y                   = -63860,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x281,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 36110,
        Z                   = 100,
        Y                   = -57130,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x283,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 100880,
        Z                   = 0,
        Y                   = 9130,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 101280,
        Z                   = 0,
        Y                   = 30750,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 82820,
        Z                   = 0,
        Y                   = 29000,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 83160,
        Z                   = 0,
        Y                   = -8780,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 88970,
        Z                   = 0,
        Y                   = -2230,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -66880,
        Z                   = 0,
        Y                   = 99230,
        Unknown_0C          = 180,
        Unknown_0E          = 13,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x284,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -18820,
        Y                   = 0,
        Z                   = 153500,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = -31190,
        Y                   = 0,
        Z                   = 153500,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = 96700,
        TriggerZ            = 0,
        TriggerY            = 69850,
        TriggerRange        = 1000,
        ActorX              = 96700,
        ActorZ              = 2000,
        ActorY              = 69850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 93090,
        TriggerZ            = 0,
        TriggerY            = 131110,
        TriggerRange        = 800,
        ActorX              = 93090,
        ActorZ              = 1000,
        ActorY              = 131110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -23150,
        TriggerZ            = 0,
        TriggerY            = -6690,
        TriggerRange        = 800,
        ActorX              = -23150,
        ActorZ              = 1200,
        ActorY              = -6690,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 92700,
        TriggerZ            = 0,
        TriggerY            = -57020,
        TriggerRange        = 800,
        ActorX              = 92700,
        ActorZ              = 1200,
        ActorY              = -57020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -32810,
        TriggerZ            = 0,
        TriggerY            = 151740,
        TriggerRange        = 800,
        ActorX              = -32810,
        ActorZ              = 1200,
        ActorY              = 151740,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 18,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -14200,
        TriggerZ            = 0,
        TriggerY            = 146550,
        TriggerRange        = 800,
        ActorX              = -14200,
        ActorZ              = 1200,
        ActorY              = 146550,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 19,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 103700,
        TriggerZ            = 0,
        TriggerY            = 20560,
        TriggerRange        = 800,
        ActorX              = 103700,
        ActorZ              = 1200,
        ActorY              = 20560,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 17950,
        TriggerZ            = 1000,
        TriggerY            = 145980,
        TriggerRange        = 1000,
        ActorX              = 17950,
        ActorZ              = 1000,
        ActorY              = 145980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 50800,
        TriggerZ            = 1000,
        TriggerY            = 32509,
        TriggerRange        = 1000,
        ActorX              = 50800,
        ActorZ              = 1000,
        ActorY              = 32509,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 133910,
        TriggerZ            = 1000,
        TriggerY            = 17920,
        TriggerRange        = 1000,
        ActorX              = 133910,
        ActorZ              = 1000,
        ActorY              = 17920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -70970,
        TriggerZ            = 1000,
        TriggerY            = 95020,
        TriggerRange        = 1000,
        ActorX              = -70970,
        ActorZ              = 1000,
        ActorY              = 95020,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 141000,
        TriggerZ            = 0,
        TriggerY            = -59000,
        TriggerRange        = 1000,
        ActorX              = 141000,
        ActorZ              = 1000,
        ActorY              = -59000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -87040,
        TriggerZ            = 0,
        TriggerY            = -55500,
        TriggerRange        = 100,
        ActorX              = -87020,
        ActorZ              = 1000,
        ActorY              = -54160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_4BE",          # 00, 0
        "Function_1_4D7",          # 01, 1
        "Function_2_625",          # 02, 2
        "Function_3_781",          # 03, 3
        "Function_4_8D6",          # 04, 4
        "Function_5_A0F",          # 05, 5
        "Function_6_B4B",          # 06, 6
        "Function_7_C99",          # 07, 7
        "Function_8_D9D",          # 08, 8
        "Function_9_DA6",          # 09, 9
        "Function_10_1A67",        # 0A, 10
        "Function_11_1ABC",        # 0B, 11
        "Function_12_1B11",        # 0C, 12
        "Function_13_24EB",        # 0D, 13
        "Function_14_25AA",        # 0E, 14
        "Function_15_288A",        # 0F, 15
        "Function_16_2B0C",        # 10, 16
        "Function_17_2BAF",        # 11, 17
        "Function_18_2C52",        # 12, 18
        "Function_19_2CF5",        # 13, 19
        "Function_20_2D98",        # 14, 20
        "Function_21_2E3B",        # 15, 21
        "Function_22_3030",        # 16, 22
        "Function_23_3043",        # 17, 23
    )


    def Function_0_4BE(): pass

    label("Function_0_4BE")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x87), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4D6")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D6")
    Event(0, 8)

    label("loc_4D6")

    Return()

    # Function_0_4BE end

    def Function_1_4D7(): pass

    label("Function_1_4D7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4E8")
    OP_82(0x80, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x83, 0x0)

    label("loc_4E8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x567, 5)), scpexpr(EXPR_END)), "loc_4F3")
    OP_64(0xC, 0x1)

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 4)), scpexpr(EXPR_END)), "loc_50A")
    OP_64(0x2, 0x1)
    OP_10(0xE, 0x1)
    OP_71(0x100A, 0x0)
    ExitThread()
    Jump("loc_513")

    label("loc_50A")

    OP_10(0xE, 0x0)
    OP_72(0x100A, 0x0)
    ExitThread()

    label("loc_513")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 5)), scpexpr(EXPR_END)), "loc_52A")
    OP_64(0x3, 0x1)
    OP_10(0x18, 0x1)
    OP_71(0x100C, 0x0)
    ExitThread()
    Jump("loc_533")

    label("loc_52A")

    OP_10(0x18, 0x0)
    OP_72(0x100C, 0x0)
    ExitThread()

    label("loc_533")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 6)), scpexpr(EXPR_END)), "loc_54A")
    OP_64(0x4, 0x1)
    OP_10(0x1, 0x1)
    OP_71(0x1013, 0x0)
    ExitThread()
    Jump("loc_553")

    label("loc_54A")

    OP_10(0x1, 0x0)
    OP_72(0x1013, 0x0)
    ExitThread()

    label("loc_553")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56B, 7)), scpexpr(EXPR_END)), "loc_56A")
    OP_64(0x5, 0x1)
    OP_10(0x2, 0x1)
    OP_71(0x1009, 0x0)
    ExitThread()
    Jump("loc_573")

    label("loc_56A")

    OP_10(0x2, 0x0)
    OP_72(0x1009, 0x0)
    ExitThread()

    label("loc_573")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x56C, 0)), scpexpr(EXPR_END)), "loc_58A")
    OP_64(0x6, 0x1)
    OP_10(0x1E, 0x1)
    OP_71(0x100F, 0x0)
    ExitThread()
    Jump("loc_593")

    label("loc_58A")

    OP_10(0x1E, 0x0)
    OP_72(0x100F, 0x0)
    ExitThread()

    label("loc_593")

    OP_74(0x1A, 0x0, 0x0)
    OP_51(0x16, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5B9")
    OP_6F(0x1D, 0)
    Jump("loc_5C0")

    label("loc_5B9")

    OP_6F(0x1D, 60)

    label("loc_5C0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5D2")
    OP_6F(0x1E, 0)
    Jump("loc_5D9")

    label("loc_5D2")

    OP_6F(0x1E, 60)

    label("loc_5D9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5EB")
    OP_6F(0x1F, 0)
    Jump("loc_5F2")

    label("loc_5EB")

    OP_6F(0x1F, 60)

    label("loc_5F2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_604")
    OP_6F(0x20, 0)
    Jump("loc_60B")

    label("loc_604")

    OP_6F(0x20, 60)

    label("loc_60B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_61D")
    OP_6F(0x21, 0)
    Jump("loc_624")

    label("loc_61D")

    OP_6F(0x21, 60)

    label("loc_624")

    Return()

    # Function_1_4D7 end

    def Function_2_625(): pass

    label("Function_2_625")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6FE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C5, 1)"), scpexpr(EXPR_END)), "loc_693")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xC5\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB8)
    Jump("loc_6FB")

    label("loc_693")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xC5\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xC5\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_6FB")

    Jump("loc_773")

    label("loc_6FE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05Hey, there's an echo in here! ...Echo in here... ...Echo in here... ...in here...\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x95, 0x0)

    label("loc_773")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_625 end

    def Function_3_781(): pass

    label("Function_3_781")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_85A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A1, 1)"), scpexpr(EXPR_END)), "loc_7EF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Found \x1F\xA1\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB9)
    Jump("loc_857")

    label("loc_7EF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05Found \x1F\xA1\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xA1\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_857")

    Jump("loc_8C8")

    label("loc_85A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Warning: Chest must be filled past this line in order to operate properly!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x96, 0x0)

    label("loc_8C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_781 end

    def Function_4_8D6(): pass

    label("Function_4_8D6")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_9AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_944")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBA)
    Jump("loc_9AC")

    label("loc_944")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_9AC")

    Jump("loc_A01")

    label("loc_9AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05The bottom of this chest is a lovely mahogany.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x97, 0x0)

    label("loc_A01")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_8D6 end

    def Function_5_A0F(): pass

    label("Function_5_A0F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AE8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_A7D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBB)
    Jump("loc_AE5")

    label("loc_A7D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "\x07\x05Found \x1F\x04\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x04\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_AE5")

    Jump("loc_B3D")

    label("loc_AE8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Thank you, but your treasure is in another chest.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x98, 0x0)

    label("loc_B3D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_A0F end

    def Function_6_B4B(): pass

    label("Function_6_B4B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_C24")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E2, 1)"), scpexpr(EXPR_END)), "loc_BB9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x05Found \x1F\xE2\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBC)
    Jump("loc_C21")

    label("loc_BB9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "\x07\x05Found \x1F\xE2\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xE2\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_C21")

    Jump("loc_C8B")

    label("loc_C24")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05The chest secretly admires you, but it'll never admit its feelings.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x99, 0x0)

    label("loc_C8B")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_B4B end

    def Function_7_C99(): pass

    label("Function_7_C99")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)
    AddSepith(0x0, 0x3E8)
    AddSepith(0x1, 0x3E8)
    AddSepith(0x2, 0x3E8)
    AddSepith(0x3, 0x3E8)
    AddSepith(0x4, 0x3E8)
    AddSepith(0x5, 0x3E8)
    AddSepith(0x6, 0x3E8)

    AnonymousTalk(    #15
        (
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x1000\x01",
            "#57IWater Sepith x1000\x01",
            "#58IFire Sepith x1000\x01",
            "#59IWind Sepith x1000\x01",
            "#62ITime Sepith x1000\x01",
            "#60ISpace Sepith x1000\x01",
            "#61IMirage Sepith x1000.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2B3D)
    OP_64(0xC, 0x1)
    TalkEnd(0xFF)
    Return()

    # Function_7_C99 end

    def Function_8_D9D(): pass

    label("Function_8_D9D")

    Call(0, 9)
    Call(0, 12)
    Return()

    # Function_8_D9D end

    def Function_9_DA6(): pass

    label("Function_9_DA6")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x51, 0x2)
    OP_E0(238, 0x52, 0x3)
    OP_E0(239, 0x53, 0x2)
    OP_E0(239, 0x54, 0x3)
    OP_E0(240, 0x55, 0x2)
    OP_E0(240, 0x56, 0x3)
    OP_E0(241, 0x57, 0x2)
    OP_E0(241, 0x58, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 92860, 0, 126910, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 92290, 0, 116400, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E8B")
    SetChrPos(0xEF, 93710, 0, 116210, 0)
    SetChrPos(0xF0, 91850, 0, 114850, 0)
    SetChrPos(0xF1, 93870, 0, 114850, 0)
    Jump("loc_F10")

    label("loc_E8B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_ECF")
    SetChrPos(0xF0, 93710, 0, 116210, 0)
    SetChrPos(0xEF, 91850, 0, 114850, 0)
    SetChrPos(0xF1, 93870, 0, 114850, 0)
    Jump("loc_F10")

    label("loc_ECF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F10")
    SetChrPos(0xF1, 93710, 0, 116210, 0)
    SetChrPos(0xEF, 91850, 0, 114850, 0)
    SetChrPos(0xF0, 93870, 0, 114850, 0)

    label("loc_F10")

    OP_6D(94090, 0, 116380, 0)
    OP_67(0, 7130, -10000, 0)
    OP_6B(2460, 0)
    OP_6C(45000, 0)
    OP_6E(271, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #16
        0x10,
        "Female Voice",
        (
            "#4PI was almost wondering if you guys weren't\x01",
            "going to show up.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF2")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_FF2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_101A")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_101A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1042")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1059")

    label("loc_1042")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1059")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1086")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10ED")

    label("loc_1086")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10AE")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10ED")

    label("loc_10AE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D6")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10ED")

    label("loc_10D6")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_10ED")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_111A")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1181")

    label("loc_111A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1142")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1181")

    label("loc_1142")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_116A")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1181")

    label("loc_116A")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1181")

    Sleep(1000)

    def lambda_118C():
        OP_6D(93950, 0, 127660, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_118C)

    def lambda_11A4():
        OP_67(0, 5660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_11A4)

    def lambda_11BC():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_11BC)

    def lambda_11CC():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_11CC)

    def lambda_11DC():
        OP_6E(255, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_11DC)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #17
        0x10A,
        "#812F#1PCarna!\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(94000, 0, 124560, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)

    def lambda_124C():
        OP_8F(0xFE, 0x16800, 0x0, 0x1D60A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_124C)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12D2")

    def lambda_127A():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_127A)
    Sleep(100)

    def lambda_129A():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_129A)
    Sleep(100)

    def lambda_12BA():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_12BA)
    Jump("loc_13A7")

    label("loc_12D2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_133E")

    def lambda_12E6():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_12E6)
    Sleep(100)

    def lambda_1306():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1306)
    Sleep(100)

    def lambda_1326():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1326)
    Jump("loc_13A7")

    label("loc_133E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_13A7")

    def lambda_1352():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1352)
    Sleep(100)

    def lambda_1372():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1372)
    Sleep(100)

    def lambda_1392():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1392)

    label("loc_13A7")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#831F#5PHeh. Looks like you guys've gotten yourselves\x01",
            "caught up in something messy.\x02\x03",

            "#833FOrdinarily, this is where I'd pitch in and help out...\x02\x03",

            "#835F...but I don't think that's an option this time.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrSubChip(0x10, 0)

    def lambda_14B7():

        label("loc_14B7")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_14B7")

    QueueWorkItem2(0x10, 3, lambda_14B7)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_1506():
        OP_6D(93480, 0, 122940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1506)

    def lambda_151E():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_151E)

    def lambda_1536():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1536)

    def lambda_1546():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1546)

    def lambda_1556():
        OP_6E(308, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1556)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 86290, 0, 120750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 99200, 0, 120600, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1606")

    def lambda_15E8():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_15E8)
    Sleep(50)

    def lambda_15FB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_15FB)
    Jump("loc_1667")

    label("loc_1606")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1638")

    def lambda_161A():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_161A)
    Sleep(50)

    def lambda_162D():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_162D)
    Jump("loc_1667")

    label("loc_1638")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1667")

    def lambda_164C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_164C)
    Sleep(50)

    def lambda_165F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_165F)

    label("loc_1667")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 86290, -3000, 120750, 90)
    SetChrPos(0x12, 99200, -3000, 120600, 270)
    OP_22(0x85, 0x1, 0x64)

    def lambda_169E():

        label("loc_169E")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_169E")

    QueueWorkItem2(0x109, 3, lambda_169E)
    OP_43(0x11, 0x0, 0x0, 0xA)
    OP_43(0x12, 0x0, 0x0, 0xB)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    OP_44(0x109, 0x3)
    OP_23(0x85)
    OP_82(0x0, 0x2)
    OP_44(0x10, 0x3)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 0)
    WaitChrThread(0xEE, 0x0)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_172C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1793")

    label("loc_172C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1754")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1793")

    label("loc_1754")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_177C")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1793")

    label("loc_177C")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1793")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C0")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1827")

    label("loc_17C0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17E8")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1827")

    label("loc_17E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1810")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1827")

    label("loc_1810")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1827")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1854")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18BB")

    label("loc_1854")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_187C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18BB")

    label("loc_187C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_18A4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_18BB")

    label("loc_18A4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_18BB")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEE, 17)
    SetChrSubChip(0xEE, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 19)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 21)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 23)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #19
        0x109,
        "#1063F#6PUgh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10A,
        "#1317F#6PJust like when we fought Grant!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#833F#5PYou might've been able to win against him...\x02\x03",

            "#831F...but don't think breaking through my formation\x01",
            "is going to be a cakewalk!\x02\x03",

            "Come at me like your life depends on it!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 7)
    SetChrSubChip(0x10, 0)
    Sleep(30)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x11, 12)
    SetChrSubChip(0x11, 2)
    Sleep(30)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x12, 12)
    SetChrSubChip(0x12, 2)
    Sleep(300)
    Battle(0x2A3, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_9_DA6 end

    def Function_10_1A67(): pass

    label("Function_10_1A67")

    PlayEffect(0x1, 0x4, 0xFF, 86290, 0, 120750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1A67 end

    def Function_11_1ABC(): pass

    label("Function_11_1ABC")

    PlayEffect(0x1, 0x5, 0xFF, 99200, 0, 120600, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_1ABC end

    def Function_12_1B11(): pass

    label("Function_12_1B11")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 92860, 0, 126910, 180)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xD)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 0, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, 92160, 0, 123630, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C2D")
    SetChrPos(0xEF, 93540, 0, 123540, 0)
    SetChrPos(0xF0, 91620, 0, 122090, 0)
    SetChrPos(0xF1, 93300, 0, 121950, 0)
    Jump("loc_1CB2")

    label("loc_1C2D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1C71")
    SetChrPos(0xF0, 93540, 0, 123540, 0)
    SetChrPos(0xEF, 91620, 0, 122090, 0)
    SetChrPos(0xF1, 93300, 0, 121950, 0)
    Jump("loc_1CB2")

    label("loc_1C71")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CB2")
    SetChrPos(0xF1, 93540, 0, 123540, 0)
    SetChrPos(0xEF, 91620, 0, 122090, 0)
    SetChrPos(0xF0, 93300, 0, 121950, 0)

    label("loc_1CB2")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(94070, 0, 125860, 0)
    OP_67(0, 5390, -10000, 0)
    OP_6B(2640, 0)
    OP_6C(45000, 0)
    OP_6E(291, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #22
        0x10,
        (
            "#835F#5PAww... That's me beat.\x02\x03",

            "I was so confident in my battle formation,\x01",
            "too...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#819F#6PY-You had every right to. You put up\x01",
            "a heck of a fight.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1068F#6PThat battle was no joke...\x02\x03",

            "You sure know how to give people a hard time\x01",
            "with that rifle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#833F#5PHeehee. I try. Anyway, you were able to beat me,\x01",
            "so maybe you've actually got a shot at winning\x01",
            "against the next guy.\x02\x03",

            "#832FI'm sure you don't need me to spell out who that\x01",
            "is...but when it comes to mid-range tactics,\x01",
            "there's no one stronger than him in all of Liberl.\x02\x03",

            "So make sure you give him your very best.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -600, 0, 0, 0, 0, 1750, 1750, 1750, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_1FCA():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1FCA)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    Sleep(500)
    OP_6D(94110, 0, 124190, 1500)
    Sleep(500)

    ChrTalk(    #26
        0x10A,
        (
            "#1316F#11P*sigh*...\x02\x03",

            "#813FYep... We've beaten Grant and Carna, so our next\x01",
            "opponent goes without saying...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2117")

    ChrTalk(    #27
        0x10C,
        (
            "#115F#6PThe famed Artful Tactician... I've heard rumors of\x01",
            "his strength, but I've never had the chance to face\x01",
            "off against him in person.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_217A")

    label("loc_2117")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_217A")

    ChrTalk(    #28
        0x10E,
        (
            "#176F#6PThe famed Artful Tactician... I can see we're in for\x01",
            "trouble, as usual.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_217A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B6")

    ChrTalk(    #29
        0x106,
        "#555F#6PUgh... This is gonna be a blast.\x02",
    )

    CloseMessageWindow()

    label("loc_21B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2200")

    ChrTalk(    #30
        0x103,
        "#1526F#6P*sigh* I'm not looking forward to this one...\x02",
    )

    CloseMessageWindow()

    label("loc_2200")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2283")

    ChrTalk(    #31
        0x104,
        (
            "#1545F#6PI had the chance to fight against him during\x01",
            "the martial arts tournament, and he was quite\x01",
            "the foe.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_231F")

    label("loc_2283")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_231F")

    ChrTalk(    #32
        0x108,
        (
            "#070F#6PHmm... I had the chance to fight against him \x01",
            "during the martial arts tournament, but this'll\x01",
            "be my first time facing him since.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_231F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_238E")

    ChrTalk(    #33
        0x101,
        (
            "#1019F#6PW-Well, we can't turn back now!\x01",
            "We're just gonna have to pump out\x01",
            "another victory.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_238E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2425")

    ChrTalk(    #34
        0x10F,
        "#1802F#6PI take it this person is quite strong, then?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10A,
        (
            "#819F#5PHe's a real nice guy, but he really doesn't\x01",
            "hold back in battle.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2425")


    def lambda_242B():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_242B)
    Sleep(100)
    OP_8C(0x10A, 225, 400)
    Sleep(300)

    ChrTalk(    #36
        0x109,
        (
            "#1065F#5PHe's probably going to have backup, too...\x02\x03",

            "#1063FLet's be smart about this and make sure\x01",
            "we're nice and prepared before we keep\x01",
            "going.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B10)
    OP_28(0x38, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_1B11 end

    def Function_13_24EB(): pass

    label("Function_13_24EB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_250C")
    Sleep(100)
    Jump("loc_2587")

    label("loc_250C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2521")
    Sleep(200)
    Jump("loc_2587")

    label("loc_2521")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2536")
    Sleep(300)
    Jump("loc_2587")

    label("loc_2536")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_254B")
    Sleep(400)
    Jump("loc_2587")

    label("loc_254B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2560")
    Sleep(500)
    Jump("loc_2587")

    label("loc_2560")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2575")
    Sleep(600)
    Jump("loc_2587")

    label("loc_2575")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2587")
    Sleep(700)

    label("loc_2587")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_25A9")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_2587")

    label("loc_25A9")

    Return()

    # Function_13_24EB end

    def Function_14_25AA(): pass

    label("Function_14_25AA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27D8")
    EventBegin(0x0)
    Fade(500)
    OP_6D(93510, 0, 130570, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(281, 0)
    SetChrPos(0x109, 92790, 0, 130190, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264B")
    SetChrPos(0xEF, 92530, 0, 128699, 0)
    SetChrPos(0xF0, 91700, 0, 127500, 0)
    SetChrPos(0xF1, 93130, 0, 127700, 0)
    Jump("loc_26D0")

    label("loc_264B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_268F")
    SetChrPos(0xF0, 92530, 0, 128699, 0)
    SetChrPos(0xEF, 91700, 0, 127500, 0)
    SetChrPos(0xF1, 93130, 0, 127700, 0)
    Jump("loc_26D0")

    label("loc_268F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26D0")
    SetChrPos(0xF1, 92530, 0, 128699, 0)
    SetChrPos(0xEF, 91700, 0, 127500, 0)
    SetChrPos(0xF0, 93130, 0, 127700, 0)

    label("loc_26D0")

    OP_0D()
    Sleep(300)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x1A, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #37
        (
            "\x07\x02#1S#40WInspect the open glass coffin,\x01",
            "then you shall obtain radiance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    Sleep(500)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #38
        "\x07\x05Received \x1F\x30\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x330, 1)
    Sleep(500)
    OP_A2(0x2B11)
    OP_28(0x38, 0x1, 0x80)
    OP_74(0x1A, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    EventEnd(0x0)
    Jump("loc_2889")

    label("loc_27D8")

    TalkBegin(0xFF)
    OP_C4(0x0, 0x10000)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    OP_22(0x9D, 0x0, 0x64)
    OP_74(0x1A, 0x0, 0x3)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x02#1S#40WInspect the open glass coffin,\x01",
            "then you shall obtain radiance.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_C4(0x1, 0x10000)
    FadeToBright(300, 0)
    OP_74(0x1A, 0x0, 0x0)
    OP_22(0x9C, 0x0, 0x64)
    Sleep(500)
    TalkEnd(0xFF)

    label("loc_2889")

    Return()

    # Function_14_25AA end

    def Function_15_288A(): pass

    label("Function_15_288A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2959")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5632)
    Sleep(500)
    Jump("loc_295C")

    label("loc_2959")

    TalkBegin(0xFF)

    label("loc_295C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #40
        "\x07\x05Select an Option\x18\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2998")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ADB")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "Restore HP/EP\x01",          # 0
            "Shop\x01",                   # 1
            "Synthesize Quartz\x01",      # 2
            "End\x01",                    # 3
        )
    )

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_29F4"),
        (1, "loc_2A6F"),
        (2, "loc_2A9D"),
        (SWITCH_DEFAULT, "loc_2ACB"),
    )


    label("loc_29F4")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_1D(0xE9)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AD8")

    label("loc_2A6F")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #41
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2AD8")

    label("loc_2A9D")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #42
        "\x07\x05Select an Option\x18\x02",
    )

    Jump("loc_2AD8")

    label("loc_2ACB")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2AD8")

    label("loc_2AD8")

    Jump("loc_2998")

    label("loc_2ADB")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B08")
    OP_A2(0x2599)
    EventEnd(0x1)
    Jump("loc_2B0B")

    label("loc_2B08")

    TalkEnd(0xFF)

    label("loc_2B0B")

    Return()

    # Function_15_288A end

    def Function_16_2B0C(): pass

    label("Function_16_2B0C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B87")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x1E)
    OP_73(0xA)
    OP_64(0x2, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x2B5C)
    Jump("loc_2BAB")

    label("loc_2B87")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2BAB")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2BAB")

    label("loc_2BAB")

    TalkEnd(0xFF)
    Return()

    # Function_16_2B0C end

    def Function_17_2BAF(): pass

    label("Function_17_2BAF")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C2A")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_64(0x3, 0x1)
    OP_10(0x18, 0x1)
    OP_A2(0x2B5D)
    Jump("loc_2C4E")

    label("loc_2C2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2C4E")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2C4E")

    label("loc_2C4E")

    TalkEnd(0xFF)
    Return()

    # Function_17_2BAF end

    def Function_18_2C52(): pass

    label("Function_18_2C52")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CCD")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0x4, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x2B5E)
    Jump("loc_2CF1")

    label("loc_2CCD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2CF1")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2CF1")

    label("loc_2CF1")

    TalkEnd(0xFF)
    Return()

    # Function_18_2C52 end

    def Function_19_2CF5(): pass

    label("Function_19_2CF5")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2D70")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_64(0x5, 0x1)
    OP_10(0x2, 0x1)
    OP_A2(0x2B5F)
    Jump("loc_2D94")

    label("loc_2D70")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2D94")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2D94")

    label("loc_2D94")

    TalkEnd(0xFF)
    Return()

    # Function_19_2CF5 end

    def Function_20_2D98(): pass

    label("Function_20_2D98")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E13")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xF, 0)
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    OP_64(0x6, 0x1)
    OP_10(0x1E, 0x1)
    OP_A2(0x2B60)
    Jump("loc_2E37")

    label("loc_2E13")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2E37")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2E37")

    label("loc_2E37")

    TalkEnd(0xFF)
    Return()

    # Function_20_2D98 end

    def Function_21_2E3B(): pass

    label("Function_21_2E3B")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_END)), "loc_2E56")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2E56")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_END)), "loc_2E67")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2E67")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_END)), "loc_2E78")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2E78")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2EA4"),
        (1, "loc_2EB1"),
        (3, "loc_2F06"),
        (7, "loc_2F7E"),
        (SWITCH_DEFAULT, "loc_3018"),
    )


    label("loc_2EA4")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3018")

    label("loc_2EB1")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",      # 0
            "Do Nothing\x01",           # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2EE9"),
        (1, "loc_2EF6"),
        (SWITCH_DEFAULT, "loc_2F03"),
    )


    label("loc_2EE9")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F03")

    label("loc_2EF6")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F03")

    label("loc_2F03")

    Jump("loc_3018")

    label("loc_2F06")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",        # 0
            "Use Green Cardkey\x01",      # 1
            "Do Nothing\x01",             # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2F54"),
        (1, "loc_2F61"),
        (2, "loc_2F6E"),
        (SWITCH_DEFAULT, "loc_2F7B"),
    )


    label("loc_2F54")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7B")

    label("loc_2F61")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7B")

    label("loc_2F6E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2F7B")

    label("loc_2F7B")

    Jump("loc_3018")

    label("loc_2F7E")


    Menu(
        0,
        10,
        100,
        0,
        (
            "Use Red Cardkey\x01",        # 0
            "Use Green Cardkey\x01",      # 1
            "Use Blue Cardkey\x01",       # 2
            "Do Nothing\x01",             # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2FE1"),
        (1, "loc_2FEE"),
        (2, "loc_2FFB"),
        (3, "loc_3008"),
        (SWITCH_DEFAULT, "loc_3015"),
    )


    label("loc_2FE1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3015")

    label("loc_2FEE")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3015")

    label("loc_2FFB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3015")

    label("loc_3008")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_3015")

    label("loc_3015")

    Jump("loc_3018")

    label("loc_3018")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_21_2E3B end

    def Function_22_3030(): pass

    label("Function_22_3030")

    OP_A3(0x2B64)
    OP_A2(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_22_3030 end

    def Function_23_3043(): pass

    label("Function_23_3043")

    OP_A3(0x2B64)
    OP_A3(0x2B65)
    OP_A2(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_23_3043 end

    SaveToFile()

Try(main)
