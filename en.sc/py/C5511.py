from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5511   ._SN',
        MapName             = 'Other',
        Location            = 'C5511.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60034",
        Flags               = 0,
        EntryFunctionIndex  = 14,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C5511   ._SN',
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
        ' ',                                    # 9
        ' ',                                    # 10
        ' ',                                    # 11
        ' ',                                    # 12
        ' ',                                    # 13
        ' ',                                    # 14
        ' ',                                    # 15
        ' ',                                    # 16
        'Jaeger',                               # 17
        'Carna',                                # 18
        'Grant',                                # 19
        'Phyllis',                              # 20
        'Robert',                               # 21
        ' ',                                    # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
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
        'ED6_DT29/CH12240 ._CH',             # 00
        'ED6_DT29/CH12241 ._CH',             # 01
        'ED6_DT29/CH12370 ._CH',             # 02
        'ED6_DT29/CH12371 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12270 ._CH',             # 06
        'ED6_DT29/CH12271 ._CH',             # 07
        'ED6_DT27/CH03630 ._CH',             # 08
        'ED6_DT27/CH03640 ._CH',             # 09
        'ED6_DT07/CH00261 ._CH',             # 0A
        'ED6_DT27/CH03900 ._CH',             # 0B
        'ED6_DT07/CH01450 ._CH',             # 0C
        'ED6_DT27/CH04000 ._CH',             # 0D
        'ED6_DT27/CH04001 ._CH',             # 0E
        'ED6_DT07/CH00420 ._CH',             # 0F
        'ED6_DT07/CH00421 ._CH',             # 10
        'ED6_DT27/CH04632 ._CH',             # 11
        'ED6_DT27/CH03820 ._CH',             # 12
        'ED6_DT27/CH04821 ._CH',             # 13
        'ED6_DT27/CH04640 ._CH',             # 14
        'ED6_DT27/CH04641 ._CH',             # 15
        'ED6_DT27/CH04630 ._CH',             # 16
        'ED6_DT27/CH04634 ._CH',             # 17
        'ED6_DT27/CH04631 ._CH',             # 18
        'ED6_DT26/CH20200 ._CH',             # 19
        'ED6_DT26/CH20201 ._CH',             # 1A
        'ED6_DT26/CH20202 ._CH',             # 1B
    )

    AddCharChipPat(
        'ED6_DT29/CH12240P._CP',             # 00
        'ED6_DT29/CH12241P._CP',             # 01
        'ED6_DT29/CH12370P._CP',             # 02
        'ED6_DT29/CH12371P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12270P._CP',             # 06
        'ED6_DT29/CH12271P._CP',             # 07
        'ED6_DT27/CH03630P._CP',             # 08
        'ED6_DT27/CH03640P._CP',             # 09
        'ED6_DT07/CH00261P._CP',             # 0A
        'ED6_DT27/CH03900P._CP',             # 0B
        'ED6_DT07/CH01450P._CP',             # 0C
        'ED6_DT27/CH04000P._CP',             # 0D
        'ED6_DT27/CH04001P._CP',             # 0E
        'ED6_DT07/CH00420P._CP',             # 0F
        'ED6_DT07/CH00421P._CP',             # 10
        'ED6_DT27/CH04632P._CP',             # 11
        'ED6_DT27/CH03820P._CP',             # 12
        'ED6_DT27/CH04821P._CP',             # 13
        'ED6_DT27/CH04640P._CP',             # 14
        'ED6_DT27/CH04641P._CP',             # 15
        'ED6_DT27/CH04630P._CP',             # 16
        'ED6_DT27/CH04634P._CP',             # 17
        'ED6_DT27/CH04631P._CP',             # 18
        'ED6_DT26/CH20200P._CP',             # 19
        'ED6_DT26/CH20201P._CP',             # 1A
        'ED6_DT26/CH20202P._CP',             # 1B
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        NpcIndex            = 0x0,
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
        Direction           = 180,
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
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 18,
        ChipIndex           = 0x12,
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
        Direction           = 180,
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
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x181,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 580,
        Z                   = 0,
        Y                   = -79030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 2350,
        Z                   = 0,
        Y                   = 18010,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 122670,
        Z                   = 0,
        Y                   = 56060,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 122370,
        Z                   = 0,
        Y                   = -65990,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1900,
        TriggerZ            = -500,
        TriggerY            = -56200,
        TriggerRange        = 1000,
        ActorX              = -1900,
        ActorZ              = 1000,
        ActorY              = -56200,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2470,
        TriggerZ            = 0,
        TriggerY            = -60170,
        TriggerRange        = 1000,
        ActorX              = 2470,
        ActorZ              = 0,
        ActorY              = -60170,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1930,
        TriggerZ            = 0,
        TriggerY            = -30370,
        TriggerRange        = 1000,
        ActorX              = -1930,
        ActorZ              = 0,
        ActorY              = -30370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1960,
        TriggerZ            = 0,
        TriggerY            = -26130,
        TriggerRange        = 1500,
        ActorX              = -1960,
        ActorZ              = 1500,
        ActorY              = -26130,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1870,
        TriggerZ            = 0,
        TriggerY            = -33850,
        TriggerRange        = 1500,
        ActorX              = -1870,
        ActorZ              = 1500,
        ActorY              = -33850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5920,
        TriggerZ            = 0,
        TriggerY            = -28120,
        TriggerRange        = 1500,
        ActorX              = -5920,
        ActorZ              = 1500,
        ActorY              = -28120,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -5990,
        TriggerZ            = 0,
        TriggerY            = -32009,
        TriggerRange        = 1500,
        ActorX              = -5990,
        ActorZ              = 1500,
        ActorY              = -32009,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1920,
        TriggerZ            = 0,
        TriggerY            = -28070,
        TriggerRange        = 1500,
        ActorX              = 1920,
        ActorZ              = 1500,
        ActorY              = -28070,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 1900,
        TriggerZ            = 0,
        TriggerY            = -32030,
        TriggerRange        = 1500,
        ActorX              = 1900,
        ActorZ              = 1500,
        ActorY              = -32030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = -1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 74740,
        TriggerZ            = 0,
        TriggerY            = 102630,
        TriggerRange        = 1000,
        ActorX              = 74740,
        ActorZ              = 1000,
        ActorY              = 102630,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -80430,
        TriggerZ            = 0,
        TriggerY            = 17900,
        TriggerRange        = 1000,
        ActorX              = -80430,
        ActorZ              = 1000,
        ActorY              = 17900,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 0,
        TriggerZ            = 0,
        TriggerY            = -28920,
        TriggerRange        = 1000,
        ActorX              = 0,
        ActorZ              = 1000,
        ActorY              = -28920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2000,
        TriggerZ            = 0,
        TriggerY            = -28000,
        TriggerRange        = 1000,
        ActorX              = -2000,
        ActorZ              = 1200,
        ActorY              = -28000,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_58E",          # 00, 0
        "Function_1_59F",          # 01, 1
        "Function_2_6F5",          # 02, 2
        "Function_3_6F9",          # 03, 3
        "Function_4_710",          # 04, 4
        "Function_5_711",          # 05, 5
        "Function_6_712",          # 06, 6
        "Function_7_729",          # 07, 7
        "Function_8_72A",          # 08, 8
        "Function_9_72B",          # 09, 9
        "Function_10_734",         # 0A, 10
        "Function_11_14B4",        # 0B, 11
        "Function_12_2AC1",        # 0C, 12
        "Function_13_2CE3",        # 0D, 13
        "Function_14_322B",        # 0E, 14
        "Function_15_38CB",        # 0F, 15
        "Function_16_3E22",        # 10, 16
    )


    def Function_0_58E(): pass

    label("Function_0_58E")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x7A), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_59E")
    Event(0, 9)

    label("loc_59E")

    Return()

    # Function_0_58E end

    def Function_1_59F(): pass

    label("Function_1_59F")

    OP_82(0x81, 0x0)
    OP_82(0x82, 0x0)
    OP_82(0x83, 0x0)
    OP_82(0x84, 0x0)
    OP_82(0x85, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5E6")
    OP_6F(0x2, 30)
    OP_6F(0x3, 30)
    OP_6F(0x4, 30)
    OP_6F(0x5, 30)
    OP_79(0xA, 0x2)
    OP_79(0xC, 0x2)
    OP_79(0x20, 0x2)
    OP_79(0x21, 0x2)
    OP_7B()
    Jump("loc_602")

    label("loc_5E6")

    OP_6F(0x2, 15)
    OP_6F(0x3, 15)
    OP_6F(0x4, 15)
    OP_6F(0x5, 15)

    label("loc_602")

    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_72(0xB, 0x10)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_65D")
    OP_64(0xC, 0x1)
    OP_7A(0xA, 0x2)
    OP_7A(0xC, 0x2)
    OP_7A(0x20, 0x2)
    OP_7A(0x21, 0x2)
    OP_7B()
    OP_6F(0x2E, 1)
    OP_6F(0xB, 29)
    OP_71(0xB, 0x2)
    Jump("loc_65D")

    label("loc_65D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_66F")
    OP_6F(0x2F, 0)
    Jump("loc_676")

    label("loc_66F")

    OP_6F(0x2F, 60)

    label("loc_676")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6E1")
    LoadEffect(0x0, "map\\\\mp027_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x0)
    Jump("loc_6F4")

    label("loc_6E1")

    OP_72(0x7, 0x20)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x0)

    label("loc_6F4")

    Return()

    # Function_1_59F end

    def Function_2_6F5(): pass

    label("Function_2_6F5")

    TalkEnd(0xFF)
    Return()

    # Function_2_6F5 end

    def Function_3_6F9(): pass

    label("Function_3_6F9")

    TalkBegin(0xFF)

    AnonymousTalk(    #0
        "Begin\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x4)
    TalkEnd(0xFF)
    Return()

    # Function_3_6F9 end

    def Function_4_710(): pass

    label("Function_4_710")

    Return()

    # Function_4_710 end

    def Function_5_711(): pass

    label("Function_5_711")

    Return()

    # Function_5_711 end

    def Function_6_712(): pass

    label("Function_6_712")

    TalkBegin(0xFF)

    AnonymousTalk(    #1
        "Begin\x02",
    )

    CloseMessageWindow()
    OP_43(0x8, 0x0, 0x0, 0x7)
    TalkEnd(0xFF)
    Return()

    # Function_6_712 end

    def Function_7_729(): pass

    label("Function_7_729")

    Return()

    # Function_7_729 end

    def Function_8_72A(): pass

    label("Function_8_72A")

    Return()

    # Function_8_72A end

    def Function_9_72B(): pass

    label("Function_9_72B")

    Call(0, 10)
    Call(0, 11)
    Return()

    # Function_9_72B end

    def Function_10_734(): pass

    label("Function_10_734")

    EventBegin(0x0)
    OP_6D(71250, 0, -31120, 0)
    OP_67(0, 7140, -10000, 0)
    OP_6B(3500, 0)
    OP_6C(57000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 70500, 0, -30340, 0)
    SetChrPos(0x10A, 72480, 0, -30340, 0)
    OP_4F(0x65, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x1), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x1), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x66, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x2), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x2), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x67, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x3), scpexpr(EXPR_GET_CHR_WORK, 0x10A, 0x3), scpexpr(EXPR_ADD), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_IDIV), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrChipByIndex(0x10, 22)
    SetChrPos(0x10, 71440, 2000, -19470, 178)
    ClearChrFlags(0x10, 0x80)
    OP_20(0x5DC)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #2
        0x10,
        "Man's Voice",
        (
            "HEH! Finally made yer way here,\x01",
            "didja, ya freakin' brats?!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_1D(0x56)
    Sleep(500)

    def lambda_889():
        OP_6D(71640, 1000, -22120, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_889)

    def lambda_8A1():
        OP_67(0, 5140, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_8A1)

    def lambda_8B9():
        OP_6C(57000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_8B9)
    WaitChrThread(0x101, 0x1)
    WaitChrThread(0x101, 0x2)
    WaitChrThread(0x101, 0x3)

    ChrTalk(    #3
        0x101,
        "#2P#1005FYou!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #4
        0x10A,
        "#2P#812FSo you finally show your face!\x02",
    )

    CloseMessageWindow()

    def lambda_917():
        OP_6B(3700, 1200)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_917)
    SetChrChipByIndex(0x101, 13)

    def lambda_92C():
        OP_94(0x0, 0x101, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_92C)
    Sleep(200)
    SetChrChipByIndex(0x10A, 15)

    def lambda_94C():
        OP_94(0x0, 0x10A, 0x0, 0x1388, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x10A, 0, lambda_94C)
    WaitChrThread(0x101, 0x0)
    SetChrChipByIndex(0x101, 13)
    WaitChrThread(0x10A, 0x0)
    SetChrChipByIndex(0x10A, 15)

    ChrTalk(    #5
        0x10,
        (
            "#6PWelcome to the newest outpost\x01",
            "of the jaegers in the Leman State,\x01",
            "kidlets!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#6PDidja have FUN with all those\x01",
            "great traps we left for ya?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x101,
        (
            "#2P#1007FYeah. Barrel of laughs.\x01",
            "Thanks for that.\x02\x03",

            "#1002FMore to the point, I'm guessing\x01",
            "you're keeping Kurt and Phyllis\x01",
            "behind that door, right?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x10A,
        (
            "#816F#2PHow about you let them go before\x01",
            "I pry off that mask and paint your\x01",
            "face with my sword?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10,
        (
            "#6PHa HAAA! Chirp all you want,\x01",
            "little chicks.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #10
        0x10,
        (
            "#6PYou've come so far not even\x01",
            "realizing this would be your grave.\x01",
            "How sad! How very like a BRACER!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0x101,
        (
            "#2P#1006FIsn't that our line?\x02\x03",

            "I have NO idea what you guys are\x01",
            "trying to accomplish here, but you\x01",
            "really backed yourselves into a corner.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10,
        "#6PThe heck do you...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #13
        0x10A,
        (
            "#816F#2PUh... Yeah! Guild reinforcements\x01",
            "are gonna be here soon!\x02\x03",

            "Once they get here, you're out of\x01",
            "luck!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x10,
        (
            "#6PTry again, girlies!\x01",
            "We smashed your phone.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#6PJust how did you make contact with\x01",
            "any 'reinforcements' without that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        (
            "#2P#1015FEr, well...\x02\x03",

            "(Oh, crap, I need to pull\x01",
            "out a really good bluff...)\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetMessageWindowPos(-1, 50, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x18\x07\x05What kind of bluff will you use?\x02",
    )


    Menu(
        0,
        -1,
        150,
        0,
        (
            "Smoke Signals\x01",              # 0
            "Don't NEED To Contact\x01",      # 1
            "Trainees Coming\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_E4F"),
        (1, "loc_FDA"),
        (2, "loc_11D4"),
        (SWITCH_DEFAULT, "loc_137B"),
    )


    label("loc_E4F")


    ChrTalk(    #18
        0x101,
        (
            "#2P#1009F...We contacted the base of the\x01",
            "mountain with smoke signals!\x02\x03",

            "It's not like we were completely\x01",
            "unprepared for an emergency,\x01",
            "you know!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10A,
        "#1317F#2PUh, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10,
        (
            "#6PBWAHAHA! What a cute little lie,\x01",
            "girlie!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#6PIt's funnyyy...\x01",
            "I was on the roof a little while ago,\x01",
            "so why didn't I see any smoke? At all?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x101,
        (
            "#2P#1019FNnngh...\x01",
            "(I guess that was a little too simple...)\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137B")

    label("loc_FDA")

    OP_2B(0x7E, 0x2)

    ChrTalk(    #23
        0x101,
        (
            "#2P#1006FActually, I oughtta thank you for\x01",
            "breaking the phone as bad as you did.\x01",
            "Good job!\x02\x03",

            "The fact that Le Locle has gone totally\x01",
            "silent for a whole day will mean the guild\x01",
            "will already know something's wrong!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x10,
        "#6PWh-What...?\x02",
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x26, 0x26, 0xFA, 0x1)
    Sleep(1000)

    ChrTalk(    #25
        0x10A,
        (
            "#814F#2PHey, that's...true!\x01",
            "They probably figured it out ages ago.\x02\x03",

            "#811FHeck, I bet our reinforcements are\x01",
            "already in the air! They'll be here any\x01",
            "MINUTE now!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #26
        0x10,
        (
            "#6PTch. Guess we took that bracer\x01",
            "pig-headedness a bit too lightly.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_137B")

    label("loc_11D4")


    ChrTalk(    #27
        0x101,
        (
            "#2P#1002F...Several new trainees are going\x01",
            "to be arriving today!\x02\x03",

            "With them on our side, you don't\x01",
            "stand a chance!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x10A,
        "#1317F#2PUm, Estelle...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        "#6POh, reeeally...? That's good to hear.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x10,
        (
            "#6PWell, then, we'll just set a little\x01",
            "ambush at the canyon entrance.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x10,
        (
            "#6PLong as they aren't ready for us,\x01",
            "we can slaughter 'em all nice and\x01",
            "quick-like!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x101,
        (
            "#2P#1019FErk! Nngh...\x01",
            "(That didn't even WORK as a bluff...)\x02",
        )
    )

    CloseMessageWindow()

    label("loc_137B")


    ChrTalk(    #33
        0x10,
        "#6PEither way, you brats are an eyesore!\x02",
    )

    CloseMessageWindow()
    OP_22(0x1FD, 0x0, 0x64)
    SetChrChipByIndex(0x10, 17)
    OP_99(0x10, 0x0, 0x5, 0x7D0)
    Sleep(500)

    ChrTalk(    #34
        0x10,
        (
            "#6PThe best use for your skins will be as\x01",
            "CLEANING RAGS for our new base! DIE!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#2P#1005FAll right! Bring it on,\x01",
            "you monster!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #36
        0x10A,
        (
            "#815F#2PWe won't lose!\x01",
            "FOR THE GUILD!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(100)
    OP_44(0x101, 0xFF)
    OP_44(0x10A, 0xFF)
    OP_44(0x10, 0xFF)
    Battle(0x395, 0x0, 0x0, 0x0, 0xFF)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Return()

    # Function_10_734 end

    def Function_11_14B4(): pass

    label("Function_11_14B4")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x101, 0x0)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x0)
    OP_44(0x10, 0x0)
    OP_6D(72290, 1500, -21120, 0)
    SetChrPos(0x101, 70540, 1500, -21200, 78)
    SetChrChipByIndex(0x101, 13)
    SetChrPos(0x10A, 73110, 1000, -22200, 17)
    SetChrChipByIndex(0x10A, 15)
    SetChrPos(0x10, 73240, 2000, -19780, 225)
    ClearChrFlags(0x10, 0x80)
    SetChrChipByIndex(0x10, 23)
    SetChrSubChip(0x10, 3)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #37
        0x10,
        "#6PNngh...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x101,
        (
            "#1006F#6PHooh... Haaaah...\x01",
            "W-We... We won...\x02\x03",

            "#1015FBut the way he fights...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #39
        0x10A,
        (
            "#1317FY-Yeah... You noticed too,\x01",
            "Estelle? It's like...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x11, 71420, 2000, -15600, 180)
    SetChrPos(0x12, 71420, 2000, -15600, 180)

    NpcTalk(    #40
        0x11,
        "Woman's Voice",
        (
            "#4PHeehee! You guys sure are\x01",
            "good at being tricked.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)

    NpcTalk(    #41
        0x12,
        "Man's Voice",
        (
            "#4PHa-ha-ha! Man, you guys were\x01",
            "great! What a beat down!\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_20(0x7D0)

    def lambda_16D5():
        OP_6D(72300, 2000, -18490, 1000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_16D5)

    def lambda_16ED():
        OP_6B(3600, 1000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_16ED)
    OP_8C(0x101, 3, 1000)
    Sleep(100)
    OP_8C(0x10A, 3, 1000)
    WaitChrThread(0x101, 0x0)
    WaitChrThread(0x101, 0x1)
    SetChrPos(0x11, 71480, 2000, -12880, 180)
    SetChrPos(0x12, 71480, 2000, -11880, 180)
    OP_22(0x6D, 0x0, 0x64)
    OP_72(0xD, 0x10)
    OP_6F(0xD, 0)
    OP_70(0xD, 0x1D)
    OP_73(0xD)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)

    def lambda_1761():
        OP_8E(0x11, 0x11AE4, 0x7D0, 0xFFFFB8FC, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_1761)

    def lambda_177C():
        OP_8E(0x12, 0x11738, 0x7D0, 0xFFFFC34C, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_177C)
    WaitChrThread(0x12, 0x1)

    ChrTalk(    #42
        0x101,
        "#1020F#2POh, crap!\x02",
    )


    def lambda_17B3():
        OP_8E(0x12, 0x11698, 0x7D0, 0xFFFFB9CE, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 1, lambda_17B3)
    WaitChrThread(0x11, 0x1)
    CloseMessageWindow()

    ChrTalk(    #43
        0x10A,
        "#812F#2PMORE enemies?\x02",
    )

    CloseMessageWindow()
    WaitChrThread(0x12, 0x1)
    TurnDirection(0x12, 0x101, 400)

    NpcTalk(    #44
        0x11,
        "Female Jaeger",
        "#6PHaha! No, no, no!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #45
        0x11,
        "Female Jaeger",
        (
            "#6PC'mon, I'm not even changing my\x01",
            "voice anymore! Don't tell me you\x01",
            "can't figure it out?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x101,
        (
            "#1015F#2PThat voice... Girly yet tough...\x02\x03",

            "#1004FNo... No WAY!\x02",
        )
    )

    CloseMessageWindow()
    Sleep(500)

    ChrTalk(    #47
        0x10A,
        "#1317F#3S#2PCARNA?!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()

    NpcTalk(    #48
        0x11,
        "Female Jaeger",
        "#6PBiiiin-gooooo!\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x11, 25)
    OP_0D()
    OP_1D(0x1)
    Sleep(500)

    ChrTalk(    #49
        0x11,
        (
            "#1201F#6PAnelace, Estelle! It's really been\x01",
            "a while, hasn't it?\x02",
        )
    )

    CloseMessageWindow()
    Fade(500)
    SetChrSubChip(0x101, 0)
    SetChrChipByIndex(0x101, 65535)
    SetChrSubChip(0x10A, 0)
    SetChrChipByIndex(0x10A, 65535)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x101,
        (
            "#1005F#2PUh, a while, yeah...\x01",
            "but what are you doing in a\x01",
            "JAEGER SUIT?!\x02\x03",

            "Wait, that'd mean that the\x01",
            "guy over there is...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #51
        0x10A,
        "#815FGrant?!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #52
        0x12,
        "Jaeger",
        "#5PHole in one!\x02",
    )

    CloseMessageWindow()
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x12, 27)
    OP_0D()
    Sleep(500)

    ChrTalk(    #53
        0x12,
        "#1191F#6PHey, you two! Great work!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        (
            "#1015F#2PGreat work? Wait...\x02\x03",

            "Do you mean this was all...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x10,
        "And at last, comprehension dawns.\x02",
    )

    CloseMessageWindow()
    OP_99(0x10, 0x3, 0x0, 0x5DC)
    Sleep(500)
    OP_22(0xD5, 0x0, 0x64)
    Fade(500)
    SetChrChipByIndex(0x10, 26)
    OP_0D()
    OP_8C(0x101, 78, 500)

    NpcTalk(    #56
        0x10,
        "Kurt",
        (
            "#1211FEstelle. Anelace.\x01",
            "Excellent work on your final\x01",
            "training course.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #57
        0x101,
        "#1004F#5PF-Final training...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #58
        0x10A,
        (
            "#1317FS-So...\x02\x03",

            "Everything since last night's attack\x01",
            "has been a...performance?!\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #59
        0x10,
        "Kurt",
        (
            "#1210FExactly!\x01",
            "This is a long-standing Le Locle tradition.\x02\x03",

            "The idea is to put trainees in a life-\x01",
            "threatening situation in order to see how\x01",
            "well they utilize their newly-learned skills.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #60
        0x101,
        "#1019F#5PAre you frickin' KIDDING me...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #61
        0x12,
        (
            "#1190F#6PWhen Kurt told us your finals were\x01",
            "comin' up, we rode our butts out\x01",
            "here from Liberl to help out!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #62
        0x11,
        "#1201F#6PHeheh! It was a lot of fun.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #63
        0x10A,
        (
            "#1316FFUN?! Ooooooh...!\x02\x03",

            "#812FYou guys are all THE WORST!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #64
        0x101,
        (
            "#1009F#5PSeriously!\x02\x03",

            "We really thought it was hitting the fan!\x01",
            "We were out of our minds with worry...\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #65
        0x10,
        "Kurt",
        (
            "#1213FWell, that was part of the point,\x01",
            "in fact.\x02\x03",

            "#1212FAnd just so you're aware...\x01",
            "real jaegers would not have been\x01",
            "half as gentle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #66
        0x101,
        "#1003F#5PEr...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #67
        0x10A,
        "#813FWell...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #68
        0x11,
        (
            "#1200F#6PI know it's hard for you two to\x01",
            "imagine since the jaegers are\x01",
            "barred from operating in Liberl, but...\x02\x03",

            "Across the rest of the continent,\x01",
            "bracers and jaegers are at each\x01",
            "other's throats almost constantly.\x02\x03",

            "#1202FSo most bracers have to be prepared\x01",
            "to fight in life-threatening situations\x01",
            "at any moment.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #69
        0x12,
        (
            "#1192F#6PWe want to make sure Liberlian\x01",
            "newbies get a chance to experience\x01",
            "that.\x02\x03",

            "I know it seems rough, but we're not\x01",
            "being mean just for cruelty's sake.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x101,
        (
            "#1007F#5P*sigh* That's no fair.\x02\x03",

            "#1019FHow am I supposed to go on a\x01",
            "good complaining jag after hearing\x01",
            "something like that?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #71
        0x10A,
        "#812FYeah, no fair!\x02",
    )

    CloseMessageWindow()
    SetChrPos(0x13, 71480, 2000, -12880, 180)

    NpcTalk(    #72
        0x13,
        "Woman's Voice",
        (
            "#4PWell, looks like you're finally done\x01",
            "beating the stuffing out of one another.\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x10A, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    TurnDirection(0x101, 0x12, 500)

    def lambda_21EF():
        OP_6D(71800, 2000, -18000, 800)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_21EF)
    ClearChrFlags(0x13, 0x80)
    OP_8E(0x13, 0x116F2, 0x7D0, 0xFFFFC464, 0x7D0, 0x0)
    OP_8F(0x13, 0x111FC, 0x7D0, 0xFFFFB88E, 0x7D0, 0x0)

    ChrTalk(    #73
        0x101,
        "#1004F#2PAh, Phyllis!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x10A,
        (
            "#812FPhyllis was in on the conspiracy, too?\x01",
            "Awwwwwww... Can't trust any of you...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #75
        0x13,
        "#5PNow, now, 'conspiracy' is a bit much!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x13,
        (
            "#5PThey said they needed me for your test,\x01",
            "so I worked hard to remember my lines!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #77
        0x13,
        (
            "#5PI made a perfect 'tragic lodge\x01",
            "keeper heroine,' if you ask me!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x101,
        (
            "#1019F#2PYeah, yeah, we were totally\x01",
            "fooled last night...\x02",
        )
    )

    CloseMessageWindow()
    SetChrPos(0x14, 71310, 0, -31680, 358)

    NpcTalk(    #79
        0x14,
        "Man's Voice",
        "#1PHahaha! Excellent work, you two!\x02",
    )

    CloseMessageWindow()
    ClearChrFlags(0x14, 0x80)

    def lambda_23FC():
        OP_94(0x0, 0xFE, 0x0, 0x1C84, 0xBB8, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 1, lambda_23FC)

    def lambda_2412():
        OP_6D(72580, 1500, -21110, 2500)
        ExitThread()

    QueueWorkItem(0x14, 3, lambda_2412)

    def lambda_242A():

        label("loc_242A")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_242A")

    QueueWorkItem2(0x101, 1, lambda_242A)

    def lambda_243B():

        label("loc_243B")

        TurnDirection(0xFE, 0x14, 500)
        OP_48()
        Jump("loc_243B")

    QueueWorkItem2(0x10A, 1, lambda_243B)
    WaitChrThread(0x14, 0x1)
    WaitChrThread(0x14, 0x3)
    OP_44(0x101, 0x1)
    OP_44(0x10A, 0x1)

    ChrTalk(    #80
        0x10A,
        "#4P#815FAnd here's the last little liar.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #81
        0x101,
        (
            "#1007F#6PYou were ALL in on it?\x02\x03",

            "#1004FSo I'm guessing the telephone...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #82
        0x14,
        (
            "Yeah, that was an old piece\x01",
            "of junk I had lying around.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #83
        0x14,
        (
            "I kept the real phone somewhere safe.\x01",
            "I've already re-mounted it, so no worries.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #84
        0x14,
        (
            "Actually, I was supposed to be a hostage\x01",
            "myself and not show up today, but, well...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #85
        0x14,
        (
            "I really wanted to see you use the new\x01",
            "orbments!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #86
        0x10A,
        (
            "#4P#1316FMan, you guys seriously covered\x01",
            "every angle.\x02\x03",

            "#1314FI guess it's our fault for getting\x01",
            "tricked, huh?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x101,
        (
            "#1007F#6PAs much as I hate to admit it,\x01",
            "yeah...\x02\x03",

            "#1025FIf you think about it rationally,\x01",
            "a lot of stuff didn't make any sense.\x02\x03",

            "It just shows how far we have to go,\x01",
            "I guess.\x02",
        )
    )

    CloseMessageWindow()

    NpcTalk(    #88
        0x10,
        "Kurt",
        "#1211FDon't be too hard on yourselves.\x02",
    )

    CloseMessageWindow()

    def lambda_2752():

        label("loc_2752")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_2752")

    QueueWorkItem2(0x101, 1, lambda_2752)

    def lambda_2763():

        label("loc_2763")

        TurnDirection(0xFE, 0x10, 500)
        OP_48()
        Jump("loc_2763")

    QueueWorkItem2(0x10A, 1, lambda_2763)
    OP_6D(72500, 1750, -20000, 800)

    NpcTalk(    #89
        0x10,
        "Kurt",
        (
            "#1213FAs Carna and Grant said, the point of this\x01",
            "exercise was to give you a life-threatening\x01",
            "experience to work through with your skills.\x02\x03",

            "In that sense, the exercise has been a\x01",
            "runaway success.\x02\x03",

            "#1210FNow then. Anelace Elfead.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #90
        0x10A,
        "#814FUh, yes!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #91
        0x10,
        "Kurt",
        "#1210FEstelle Bright.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x101,
        "#1002F#5PYes, sir!\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #93
        0x10,
        "Kurt",
        (
            "#1210FAs of this moment, you have completed\x01",
            "the Le Locle Training Program.\x02\x03",

            "You have learned a great deal over the\x01",
            "past month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #94
        0x101,
        "#1004F#5PSo, then...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #95
        0x10A,
        "#1310FTomorrow we're...?\x02",
    )

    CloseMessageWindow()

    NpcTalk(    #96
        0x10,
        "Kurt",
        (
            "#1211FTwo tickets on the next flight to Liberl\x01",
            "have already been arranged for you.\x02\x03",

            "Nothing more will happen tonight...\x01",
            "I promise. So rest easy.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #97
        0x13,
        "#3PTerrific!\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #98
        0x13,
        (
            "#3PWell, then! Tonight we congratulate our new\x01",
            "graduates, and stuff them PROPERLY at a\x01",
            "nice, big farewell party!\x02",
        )
    )

    CloseMessageWindow()
    FadeToDark(2000, 0, -1)
    OP_0D()
    OP_20(0xBB8)
    OP_21()
    Sleep(1000)
    OP_3F(0x416, 1)
    NewScene("ED6_DT21/C5600   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_11_14B4 end

    def Function_12_2AC1(): pass

    label("Function_12_2AC1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B27")
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #99
        "\x07\x05Orbal energy appears to be shut down.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_2CE2")

    label("loc_2B27")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #100
        "\x07\x05There is an orbment charging station here.\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Rest\x01",       # 0
            "Leave\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2CC7")
    FadeToBright(100, 0)
    Sleep(500)
    SoundLoad(13)
    OP_82(0x0, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 700, 700, 700, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x32)
    OP_73(0x7)
    OP_20(0xBB8)
    OP_22(0xC, 0x0, 0x64)
    OP_82(0x0, 0x2)
    LoadEffect(0x1, "map\\\\mp027_01.eff")
    PlayEffect(0x1, 0x1, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1500, 1500, 1500, 0xFF, 0, 0, 0, 0)
    FadeToDark(1000, 0, -1)
    Sleep(700)
    OP_22(0xD, 0x0, 0x64)
    OP_0D()
    OP_31(0xFF, 0xFE, 0x0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x1, 0x2)
    PlayEffect(0x0, 0x0, 0xFF, 74740, 1000, 102630, 0, 0, 0, 1300, 1300, 1300, 0xFF, 0, 0, 0, 0)
    OP_6F(0x7, 0)
    OP_1E()
    FadeToBright(1000, 0)
    OP_56(0x0)
    TalkEnd(0xFF)
    Return()

    label("loc_2CC7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CE1")
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    label("loc_2CE1")

    Return()

    label("loc_2CE2")

    Return()

    # Function_12_2AC1 end

    def Function_13_2CE3(): pass

    label("Function_13_2CE3")

    OP_EA(0x2, 0x9B, 0x1, 0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2D57")
    EventBegin(0x0)
    Fade(1000)
    SetChrPos(0x101, -81450, 0, 18230, 90)
    SetChrPos(0x10A, -81380, 0, 17370, 90)
    OP_6D(-80680, 0, 18040, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    OP_0D()

    label("loc_2D57")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E2A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x416, 1)"), scpexpr(EXPR_END)), "loc_2DC3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #101
        "Found \x1F\x16\x04\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1145)
    Jump("loc_2E27")

    label("loc_2DC3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #102
        (
            "Found \x1F\x16\x04\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x16\x04\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2F, 60)
    OP_70(0x2F, 0x0)

    label("loc_2E27")

    Jump("loc_2EA2")

    label("loc_2E2A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #103
        (
            "\x07\x05This is the 56th chest you've opened! Congrats!\x01",
            "Nah, just kidding. I'm not even COUNTING.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2EA2")

    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3222")
    Sleep(400)
    OP_62(0x101, 0x0, 2000, 0x0, 0x1, 0xFA, 0x2)
    OP_22(0x26, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #104
        0x101,
        "#1015F#3PWhat's this?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #105
        0x10A,
        (
            "#818F#6PHmmm, seems like some kinda device.\x02\x03",

            "Also looks kinda like an orbment switch...\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)
    Sleep(500)

    ChrTalk(    #106
        0x10A,
        (
            "#810F#6PWell, probably good to take it with us,\x01",
            "right?\x02\x03",

            "This place is a training facility, so it might\x01",
            "be used to open trap areas or something.\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #107
        0x101,
        (
            "#1011F#3PYeah, good point.\x02\x03",

            "#1015FEven just getting here there's been a lot\x01",
            "of gates, pitch black rooms and stuff, so...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #108
        0x10A,
        (
            "#1310F#6PWelp, they're always saying to 'be prepared,'\x01",
            "right?\x02\x03",

            "Anyway, let's get going.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #109
        0x101,
        "#1006F#3PYeah.\x02",
    )

    CloseMessageWindow()
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #110
        (
            "\x07\x05You've obtained a [#15IUsable Event Item]. Throughout the story, you'll run\x01",
            "into certain story events that will require using one of these\x01",
            "in order to proceed.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #111
        (
            "\x07\x05To take advantage of Usable Event Items, open the Items tab\x01",
            "in the Camp Menu and directly select the one you'd like to use.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1065)
    EventEnd(0x0)

    label("loc_3222")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_2CE3 end

    def Function_14_322B(): pass

    label("Function_14_322B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x13), scpexpr(EXPR_PUSH_LONG, 0x416), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3238")
    Return()

    label("loc_3238")

    SetMapFlags(0x80)
    OP_C0(0x1, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    Sleep(30)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_END)), "loc_32D6")
    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #112
        "\x07\x05Activated ID Unit, but...there was no notable response.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Jump("loc_38C5")

    label("loc_32D6")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35ED")
    EventBegin(0x0)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #113
        "\x07\x05Activated ID Unit.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Sleep(400)
    SetChrPos(0x15, -1980, 0, -27750, 201)

    def lambda_3346():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3346)

    def lambda_3354():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3354)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #114
        0x101,
        "#1004FWhoa!\x02",
    )

    CloseMessageWindow()
    OP_6D(-1890, 0, -32890, 1000)
    OP_64(0xC, 0x1)
    OP_6F(0x2, 30)
    OP_70(0x2, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x2)
    SetChrPos(0x15, -5940, 0, -29460, 201)

    def lambda_33CB():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_33CB)

    def lambda_33D9():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_33D9)
    OP_7A(0xA, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x3, 30)
    OP_70(0x3, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x3)
    SetChrPos(0x15, -5900, 0, -37010, 225)

    def lambda_3418():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3418)

    def lambda_3426():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3426)
    OP_7A(0x20, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x5, 30)
    OP_70(0x5, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x5)
    SetChrPos(0x15, 1660, 0, -36980, 45)

    def lambda_3465():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_3465)

    def lambda_3473():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_3473)
    OP_7A(0x21, 0x2)
    OP_7B()
    Sleep(400)
    OP_6F(0x4, 30)
    OP_70(0x4, 0xF)
    OP_22(0x6B, 0x0, 0x64)
    OP_73(0x4)
    SetChrPos(0x15, 1670, 0, -29260, 45)

    def lambda_34B2():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34B2)

    def lambda_34C0():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_34C0)
    OP_7A(0xC, 0x2)
    OP_7B()
    Sleep(1000)
    OP_22(0x73, 0x0, 0x64)
    OP_6F(0xB, 0)
    OP_70(0xB, 0x1D)
    OP_73(0xB)
    SetChrPos(0x15, -1980, 0, -27750, 201)

    def lambda_34FF():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_34FF)

    def lambda_350D():
        TurnDirection(0xFE, 0x15, 400)
        ExitThread()

    QueueWorkItem(0x10A, 1, lambda_350D)
    OP_22(0x9D, 0x0, 0x64)
    OP_6F(0x2E, 1)
    OP_70(0x2E, 0x1)
    OP_73(0x2E)
    OP_71(0xB, 0x2)
    OP_A2(0x1067)
    Sleep(1000)
    Fade(1000)
    OP_69(0x0, 0x0)
    OP_0D()

    ChrTalk(    #115
        0x101,
        "#1008FAhaha... It really opened.\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #116
        0x10A,
        (
            "#811FHeehee, justice prevails!\x02\x03",

            "#816FAll right! Let's keep our eyes\x01",
            "peeled and carry on!\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #117
        0x101,
        "#1006FYeah!\x02",
    )

    CloseMessageWindow()
    EventEnd(0x1)
    Jump("loc_38C5")

    label("loc_35ED")

    TalkBegin(0xFF)
    OP_22(0x9D, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #118
        "\x07\x05Activated ID Unit, but...there was no notable response.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_36BF")

    ChrTalk(    #119
        0x10A,
        (
            "#814FEstelle, I don't think this is the right place.\x02\x03",

            "Let's just keep going, huh?\x02",
        )
    )

    CloseMessageWindow()
    OP_A3(0x0)
    Jump("loc_38C2")

    label("loc_36BF")

    RunExpression(0x2, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_370C")

    ChrTalk(    #120
        0x10A,
        "#812FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_370C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_374D")

    ChrTalk(    #121
        0x10A,
        "#813FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_374D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3788")

    ChrTalk(    #122
        0x10A,
        "#814FMaybe you use it somewhere else?\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_3788")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_37C9")

    ChrTalk(    #123
        0x10A,
        "#817FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_37C9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380A")

    ChrTalk(    #124
        0x10A,
        "#818FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_380A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_383E")

    ChrTalk(    #125
        0x10A,
        "#819FSeems like this isn't it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_383E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3880")

    ChrTalk(    #126
        0x10A,
        "#1315FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()
    Jump("loc_38BF")

    label("loc_3880")

    Jc((scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BF")

    ChrTalk(    #127
        0x10A,
        "#1316FDoesn't look like it can be used here.\x02",
    )

    CloseMessageWindow()

    label("loc_38BF")

    OP_A2(0x0)

    label("loc_38C2")

    TalkEnd(0xFF)

    label("loc_38C5")

    ClearMapFlags(0x80)
    Return()

    # Function_14_322B end

    def Function_15_38CB(): pass

    label("Function_15_38CB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #128
        (
            "\x07\x05The door appears to have a lock mechanism,\x01",
            "but there's no obvious lever.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x20C, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E1E")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 1)), scpexpr(EXPR_END)), "loc_3A34")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_39CA")

    ChrTalk(    #129
        0x10A,
        (
            "#813FMaybe there's a device somewhere that\x01",
            "controls this.\x02\x03",

            "#1316FWe should head back along the passages\x01",
            "and look, I guess.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_3A31")

    label("loc_39CA")


    ChrTalk(    #130
        0x10A,
        (
            "#812FMaybe we use that device we picked up\x01",
            "a while back here.\x02\x03",

            "#812FHey, Estelle. Give it a shot.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_3A31")

    Jump("loc_3E1E")

    label("loc_3A34")

    EventBegin(0x0)

    ChrTalk(    #131
        0x101,
        (
            "#1002FHey, Anelace, you think this\x01",
            "device might be...?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #132
        0x10A,
        (
            "#812FYeah, looks like it's a machine to\x01",
            "control the door's lock.\x02\x03",

            "If we use it, the door should open.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #133
        0x101,
        (
            "#1007FBut how do you use the darn thing?\x02\x03",

            "#1003FI don't see a lever or anything...\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x228, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3BC8")

    ChrTalk(    #134
        0x10A,
        (
            "#813FMaybe there's something to open\x01",
            "it somewhere.\x02\x03",

            "#812FWhy don't we go back and search\x01",
            "for it?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #135
        0x101,
        "#1006FSounds like a plan.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1)
    Jump("loc_3E1C")

    label("loc_3BC8")


    ChrTalk(    #136
        0x10A,
        (
            "#813FMaybe there's something to open\x01",
            "it somewhere.\x02\x03",

            "#812FWhy don't we go back and...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x10A, 0x0, 2000, 0x22, 0x24, 0xFA, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #137
        0x10A,
        "#814FHey, that's right!\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x101, 0x10A, 400)

    ChrTalk(    #138
        0x101,
        "#1004FYou think of something?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x10A, 0x101, 400)

    ChrTalk(    #139
        0x10A,
        (
            "#812FRemember that device we picked up?\x02\x03",

            "Near the stairs?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #140
        0x101,
        "#1011FAhh, that weird piece of junk?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #141
        0x10A,
        (
            "#810FYup. Maybe we should try it out.\x02\x03",

            "C'mon, whaddaya say?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #142
        0x101,
        (
            "#1015FHmm...\x02\x03",

            "Well, I don't mind trying, but I don't know\x01",
            "if it'll be that easy.\x02",
        )
    )

    CloseMessageWindow()

    AnonymousTalk(    #143
        (
            "\x07\x05To take advantage of Usable Event Items, open the Items tab\x01",
            "in the Camp Menu and directly select the one you'd like to use.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_59()
    OP_A2(0x1)

    label("loc_3E1C")

    EventEnd(0x1)

    label("loc_3E1E")

    TalkEnd(0xFF)
    Return()

    # Function_15_38CB end

    def Function_16_3E22(): pass

    label("Function_16_3E22")

    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #144
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_16_3E22 end

    SaveToFile()

Try(main)
