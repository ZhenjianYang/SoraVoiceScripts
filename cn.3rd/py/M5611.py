from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

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
        '卡露娜',                               # 9
        '猎兵卡露娜',                           # 10
        '猎兵卡露娜',                           # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        "Function_3_74B",          # 03, 3
        "Function_4_871",          # 04, 4
        "Function_5_997",          # 05, 5
        "Function_6_ABD",          # 06, 6
        "Function_7_BE3",          # 07, 7
        "Function_8_D07",          # 08, 8
        "Function_9_D10",          # 09, 9
        "Function_10_1966",        # 0A, 10
        "Function_11_19BB",        # 0B, 11
        "Function_12_1A10",        # 0C, 12
        "Function_13_21AE",        # 0D, 13
        "Function_14_226D",        # 0E, 14
        "Function_15_255C",        # 0F, 15
        "Function_16_27F4",        # 10, 16
        "Function_17_2892",        # 11, 17
        "Function_18_2930",        # 12, 18
        "Function_19_29CE",        # 13, 19
        "Function_20_2A6C",        # 14, 20
        "Function_21_2B0A",        # 15, 21
        "Function_22_2D24",        # 16, 22
        "Function_23_2D37",        # 17, 23
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_70A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1D, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C5, 1)"), scpexpr(EXPR_END)), "loc_699")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xC5\x02\x07\x00。\x02",
    )

    Jump("loc_67E")

    label("loc_67E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB8)
    Jump("loc_707")

    label("loc_699")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xC5\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xC5\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_6E8")

    label("loc_6E8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1D, 60)
    OP_70(0x1D, 0x0)

    label("loc_707")

    Jump("loc_73D")

    label("loc_70A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_73D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_625 end

    def Function_3_74B(): pass

    label("Function_3_74B")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_830")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1E, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2A1, 1)"), scpexpr(EXPR_END)), "loc_7BF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\xA1\x02\x07\x00。\x02",
    )

    Jump("loc_7A4")

    label("loc_7A4")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BB9)
    Jump("loc_82D")

    label("loc_7BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\xA1\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xA1\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_80E")

    label("loc_80E")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1E, 60)
    OP_70(0x1E, 0x0)

    label("loc_82D")

    Jump("loc_863")

    label("loc_830")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_863")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_74B end

    def Function_4_871(): pass

    label("Function_4_871")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_956")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1F, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_8E5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_8CA")

    label("loc_8CA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBA)
    Jump("loc_953")

    label("loc_8E5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_934")

    label("loc_934")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1F, 60)
    OP_70(0x1F, 0x0)

    label("loc_953")

    Jump("loc_989")

    label("loc_956")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_989")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_871 end

    def Function_5_997(): pass

    label("Function_5_997")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A7C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x20, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_A0B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    Jump("loc_9F0")

    label("loc_9F0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBB)
    Jump("loc_A79")

    label("loc_A0B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x04\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_A5A")

    label("loc_A5A")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x20, 60)
    OP_70(0x20, 0x0)

    label("loc_A79")

    Jump("loc_AAF")

    label("loc_A7C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_AAF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_997 end

    def Function_6_ABD(): pass

    label("Function_6_ABD")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x577, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BA2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x21, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2E2, 1)"), scpexpr(EXPR_END)), "loc_B31")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xE2\x02\x07\x00。\x02",
    )

    Jump("loc_B16")

    label("loc_B16")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2BBC)
    Jump("loc_B9F")

    label("loc_B31")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xE2\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xE2\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_B80")

    label("loc_B80")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x21, 60)
    OP_70(0x21, 0x0)

    label("loc_B9F")

    Jump("loc_BD5")

    label("loc_BA2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_BD5")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_ABD end

    def Function_7_BE3(): pass

    label("Function_7_BE3")

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
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１０００\x01",
            "\x07\x02#57I水之耀晶片×１０００\x01",
            "\x07\x02#58I火之耀晶片×１０００\x01",
            "\x07\x02#59I风之耀晶片×１０００\x01",
            "\x07\x02#62I时之耀晶片×１０００\x01",
            "\x07\x02#60I空之耀晶片×１０００\x01",
            "\x07\x02#61I幻之耀晶片×１０００\x07\x00\x02",
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

    # Function_7_BE3 end

    def Function_8_D07(): pass

    label("Function_8_D07")

    Call(0, 9)
    Call(0, 12)
    Return()

    # Function_8_D07 end

    def Function_9_D10(): pass

    label("Function_9_D10")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DF5")
    SetChrPos(0xEF, 93710, 0, 116210, 0)
    SetChrPos(0xF0, 91850, 0, 114850, 0)
    SetChrPos(0xF1, 93870, 0, 114850, 0)
    Jump("loc_E7A")

    label("loc_DF5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E39")
    SetChrPos(0xF0, 93710, 0, 116210, 0)
    SetChrPos(0xEF, 91850, 0, 114850, 0)
    SetChrPos(0xF1, 93870, 0, 114850, 0)
    Jump("loc_E7A")

    label("loc_E39")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E7A")
    SetChrPos(0xF1, 93710, 0, 116210, 0)
    SetChrPos(0xEF, 91850, 0, 114850, 0)
    SetChrPos(0xF0, 93870, 0, 114850, 0)

    label("loc_E7A")

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
        "女人的声音",
        (
            "#4P哎呀呀……\x01",
            "终于该出场了吗。\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F40")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FA7")

    label("loc_F40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F68")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FA7")

    label("loc_F68")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F90")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_FA7")

    label("loc_F90")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_FA7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FD4")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_103B")

    label("loc_FD4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FFC")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_103B")

    label("loc_FFC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1024")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_103B")

    label("loc_1024")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_103B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1068")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10CF")

    label("loc_1068")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1090")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10CF")

    label("loc_1090")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10B8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_10CF")

    label("loc_10B8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_10CF")

    Sleep(1000)

    def lambda_10DA():
        OP_6D(93950, 0, 127660, 2000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_10DA)

    def lambda_10F2():
        OP_67(0, 5660, -10000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_10F2)

    def lambda_110A():
        OP_6B(2600, 2000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_110A)

    def lambda_111A():
        OP_6C(45000, 2000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_111A)

    def lambda_112A():
        OP_6E(255, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_112A)
    WaitChrThread(0x109, 0x0)

    ChrTalk(    #17
        0x10A,
        "#812F#1P卡露娜前辈……！\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    Fade(500)
    OP_6D(94000, 0, 124560, 0)
    OP_67(0, 5480, -10000, 0)
    OP_6B(2870, 0)
    OP_6C(45000, 0)
    OP_6E(303, 0)

    def lambda_11AB():
        OP_8F(0xFE, 0x16800, 0x0, 0x1D60A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_11AB)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1231")

    def lambda_11D9():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_11D9)
    Sleep(100)

    def lambda_11F9():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_11F9)
    Sleep(100)

    def lambda_1219():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1219)
    Jump("loc_1306")

    label("loc_1231")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_129D")

    def lambda_1245():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1245)
    Sleep(100)

    def lambda_1265():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1265)
    Sleep(100)

    def lambda_1285():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1285)
    Jump("loc_1306")

    label("loc_129D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1306")

    def lambda_12B1():
        OP_8F(0xFE, 0x16E5E, 0x0, 0x1D678, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_12B1)
    Sleep(100)

    def lambda_12D1():
        OP_8F(0xFE, 0x16616, 0x0, 0x1D024, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_12D1)
    Sleep(100)

    def lambda_12F1():
        OP_8F(0xFE, 0x16E40, 0x0, 0x1D042, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_12F1)

    label("loc_1306")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Sleep(500)

    ChrTalk(    #18
        0x10,
        (
            "#831F#5P哈哈，\x01",
            "好像被卷进麻烦事里来了呢。\x02\x03",

            "#833F本来我应该在这里\x01",
            "帮你们的忙的……\x02\x03",

            "#835F不过不凑巧，\x01",
            "好像没办法做到呢。\x02",
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

    def lambda_13DB():

        label("loc_13DB")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_13DB")

    QueueWorkItem2(0x10, 3, lambda_13DB)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_1D(0xC4)

    def lambda_142A():
        OP_6D(93480, 0, 122940, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_142A)

    def lambda_1442():
        OP_67(0, 6040, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1442)

    def lambda_145A():
        OP_6B(2970, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_145A)

    def lambda_146A():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_146A)

    def lambda_147A():
        OP_6E(308, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_147A)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, 86290, 0, 120750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 99200, 0, 120600, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_152A")

    def lambda_150C():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_150C)
    Sleep(50)

    def lambda_151F():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_151F)
    Jump("loc_158B")

    label("loc_152A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_155C")

    def lambda_153E():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_153E)
    Sleep(50)

    def lambda_1551():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1551)
    Jump("loc_158B")

    label("loc_155C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158B")

    def lambda_1570():
        OP_8C(0xFE, 270, 400)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1570)
    Sleep(50)

    def lambda_1583():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1583)

    label("loc_158B")

    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    SetChrPos(0x11, 86290, -3000, 120750, 90)
    SetChrPos(0x12, 99200, -3000, 120600, 270)
    OP_22(0x85, 0x1, 0x64)

    def lambda_15C2():

        label("loc_15C2")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_15C2")

    QueueWorkItem2(0x109, 3, lambda_15C2)
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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1650")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16B7")

    label("loc_1650")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1678")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16B7")

    label("loc_1678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16A0")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_16B7")

    label("loc_16A0")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_16B7")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_16E4")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_174B")

    label("loc_16E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170C")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_174B")

    label("loc_170C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1734")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_174B")

    label("loc_1734")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_174B")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1778")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17DF")

    label("loc_1778")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A0")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17DF")

    label("loc_17A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17C8")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_17DF")

    label("loc_17C8")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_17DF")

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
        "#1063F#6P唔……！？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x10A,
        "#1317F#6P果然是那时的……！\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x10,
        (
            "#833F#5P呵呵，\x01",
            "看来你们已经战胜库拉茨了……\x02\x03",

            "#831F不过我卡露娜的包围阵\x01",
            "可没那么简单哦。\x02\x03",

            "抱着必死的决心来应战吧！\x02",
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

    # Function_9_D10 end

    def Function_10_1966(): pass

    label("Function_10_1966")

    PlayEffect(0x1, 0x4, 0xFF, 86290, 0, 120750, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x1, 0x2)
    OP_82(0x4, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_10_1966 end

    def Function_11_19BB(): pass

    label("Function_11_19BB")

    PlayEffect(0x1, 0x5, 0xFF, 99200, 0, 120600, 0, 0, 0, 600, 600, 600, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    OP_82(0x2, 0x2)
    OP_82(0x5, 0x2)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_11_19BB end

    def Function_12_1A10(): pass

    label("Function_12_1A10")

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
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B2C")
    SetChrPos(0xEF, 93540, 0, 123540, 0)
    SetChrPos(0xF0, 91620, 0, 122090, 0)
    SetChrPos(0xF1, 93300, 0, 121950, 0)
    Jump("loc_1BB1")

    label("loc_1B2C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B70")
    SetChrPos(0xF0, 93540, 0, 123540, 0)
    SetChrPos(0xEF, 91620, 0, 122090, 0)
    SetChrPos(0xF1, 93300, 0, 121950, 0)
    Jump("loc_1BB1")

    label("loc_1B70")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB1")
    SetChrPos(0xF1, 93540, 0, 123540, 0)
    SetChrPos(0xEF, 91620, 0, 122090, 0)
    SetChrPos(0xF0, 93300, 0, 121950, 0)

    label("loc_1BB1")

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
            "#835F#5P唉，伤脑筋啊……\x02\x03",

            "我对那个包围阵\x01",
            "可是相当有自信的……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10A,
        (
            "#819F#6P不、不……\x01",
            "已经强过头了啦……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x109,
        (
            "#1068F#6P不、不愧是步枪手……\x02\x03",

            "用的战术\x01",
            "都这么冷酷无情啊……\x02",
        )
    )

    Jump("loc_1D03")

    label("loc_1D03")

    CloseMessageWindow()

    ChrTalk(    #25
        0x10,
        (
            "#833F#5P哈哈，\x01",
            "你们应该也能通过下一关吧。\x02\x03",

            "#832F你们应该想到了……\x01",
            "那是王国屈指可数的中距离战强者。\x02\x03",

            "要鼓足干劲哦。\x02",
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

    def lambda_1DED():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_1DED)
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
            "#1316F#11P呜呜……\x02\x03",

            "#813F既然库拉茨前辈和卡露娜前辈都来了，\x01",
            "接下来想都不用想了……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1ED5")

    ChrTalk(    #27
        0x10C,
        (
            "#115F#6P『方术使』吗……\x01",
            "我也听过传闻。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1F1D")

    label("loc_1ED5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F1D")

    ChrTalk(    #28
        0x10E,
        (
            "#176F#6P『方术使』……\x01",
            "可不是个简单的对手啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F1D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F58")

    ChrTalk(    #29
        0x106,
        "#555F#6P真是的……开什么玩笑啊。\x02",
    )

    CloseMessageWindow()

    label("loc_1F58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F8F")

    ChrTalk(    #30
        0x103,
        (
            "#1526F#6P唉……\x01",
            "真是郁闷啊。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1F8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1FDF")

    ChrTalk(    #31
        0x104,
        (
            "#1545F#6P呼，\x01",
            "自从武术大会以后就没直接交手过了吧？\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_202B")

    label("loc_1FDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_202B")

    ChrTalk(    #32
        0x108,
        (
            "#070F#6P嗯，\x01",
            "自从武术大会以后就没直接交手过了吧。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_202B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2078")

    ChrTalk(    #33
        0x101,
        (
            "#1019F#6P既、既然如此\x01",
            "就抱着必死的决心挑战试试吧！\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2078")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2109")

    ChrTalk(    #34
        0x10F,
        (
            "#1802F#6P……虽然搞不清楚状况，\x01",
            "不过看来是相当厉害的人吧？\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x10A,
        (
            "#819F#5P嗯，\x01",
            "虽然是个沉稳的人但要求非常严格……\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2109")


    def lambda_210F():
        OP_8C(0xFE, 180, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_210F)
    Sleep(100)
    OP_8C(0x10A, 225, 400)
    Sleep(300)

    ChrTalk(    #36
        0x109,
        (
            "#1065F#5P要是同时出来几个的话，\x01",
            "的确是相当难办啊……\x02\x03",

            "#1063F似乎先做好万全准备\x01",
            "再去挑战比较好啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B10)
    OP_28(0x38, 0x1, 0x40)
    Sleep(300)
    EventEnd(0x0)
    Return()

    # Function_12_1A10 end

    def Function_13_21AE(): pass

    label("Function_13_21AE")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21CF")
    Sleep(100)
    Jump("loc_224A")

    label("loc_21CF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21E4")
    Sleep(200)
    Jump("loc_224A")

    label("loc_21E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F9")
    Sleep(300)
    Jump("loc_224A")

    label("loc_21F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_220E")
    Sleep(400)
    Jump("loc_224A")

    label("loc_220E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2223")
    Sleep(500)
    Jump("loc_224A")

    label("loc_2223")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2238")
    Sleep(600)
    Jump("loc_224A")

    label("loc_2238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_224A")
    Sleep(700)

    label("loc_224A")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_226C")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_224A")

    label("loc_226C")

    Return()

    # Function_13_21AE end

    def Function_14_226D(): pass

    label("Function_14_226D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24A4")
    EventBegin(0x0)
    Fade(500)
    OP_6D(93510, 0, 130570, 0)
    OP_67(0, 6900, -10000, 0)
    OP_6B(2470, 0)
    OP_6C(45000, 0)
    OP_6E(281, 0)
    SetChrPos(0x109, 92790, 0, 130190, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_230E")
    SetChrPos(0xEF, 92530, 0, 128699, 0)
    SetChrPos(0xF0, 91700, 0, 127500, 0)
    SetChrPos(0xF1, 93130, 0, 127700, 0)
    Jump("loc_2393")

    label("loc_230E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2352")
    SetChrPos(0xF0, 92530, 0, 128699, 0)
    SetChrPos(0xEF, 91700, 0, 127500, 0)
    SetChrPos(0xF1, 93130, 0, 127700, 0)
    Jump("loc_2393")

    label("loc_2352")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2393")
    SetChrPos(0xF1, 92530, 0, 128699, 0)
    SetChrPos(0xEF, 91700, 0, 127500, 0)
    SetChrPos(0xF0, 93130, 0, 127700, 0)

    label("loc_2393")

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
            "\x07\x02#1S#40W玻璃之棺已准备就绪。\x01",
            "调查等待开启的那一个吧。\x01",
            "如此汝即可获得光辉。\x02",
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
        "\x07\x00得到了\x1F\x30\x03\x07\x00。\x02",
    )

    Jump("loc_2464")

    label("loc_2464")

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
    Jump("loc_255B")

    label("loc_24A4")

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
            "\x07\x02#1S#40W玻璃之棺已准备就绪。\x01",
            "调查等待开启的那一个吧。\x01",
            "如此汝即可获得光辉。\x02",
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

    label("loc_255B")

    Return()

    # Function_14_226D end

    def Function_15_255C(): pass

    label("Function_15_255C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_262B")
    EventBegin(0x1)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(500)
    OP_22(0x161, 0x0, 0x64)
    Fade(1000)
    PlayEffect(0x80, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x81, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x83, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_0D()
    OP_AA(5632)
    Sleep(500)
    Jump("loc_262E")

    label("loc_262B")

    TalkBegin(0xFF)

    label("loc_262E")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #40
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2658")

    label("loc_2658")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_266B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C3")

    Menu(
        1,
        -1,
        150,
        1,
        (
            "回复ＨＰ·ＥＰ\x01",      # 0
            "获得武具\x01",            # 1
            "合成结晶回路\x01",        # 2
            "结束\x01",                # 3
        )
    )

    Jump("loc_26BD")

    label("loc_26BD")

    MenuEnd(0x0)
    OP_5F(0x1)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_26DA"),
        (1, "loc_2755"),
        (2, "loc_2784"),
        (SWITCH_DEFAULT, "loc_27B3"),
    )


    label("loc_26DA")

    FadeToBright(300, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
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
    Jump("loc_27C0")

    label("loc_2755")

    OP_A9(0x26)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #41
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_2781")

    label("loc_2781")

    Jump("loc_27C0")

    label("loc_2784")

    OP_A9(0x9)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, 60, -1, -1)

    AnonymousTalk(    #42
        "\x07\x05请选择\x18\x02",
    )

    Jump("loc_27B0")

    label("loc_27B0")

    Jump("loc_27C0")

    label("loc_27B3")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_27C0")

    label("loc_27C0")

    Jump("loc_266B")

    label("loc_27C3")

    OP_5F(0x1)
    OP_56(0x0)
    FadeToBright(300, 0)
    Sleep(300)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4B3, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27F0")
    OP_A2(0x2599)
    EventEnd(0x1)
    Jump("loc_27F3")

    label("loc_27F0")

    TalkEnd(0xFF)

    label("loc_27F3")

    Return()

    # Function_15_255C end

    def Function_16_27F4(): pass

    label("Function_16_27F4")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #43
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_286A")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xA, 0)
    OP_70(0xA, 0x1E)
    OP_73(0xA)
    OP_64(0x2, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x2B5C)
    Jump("loc_288E")

    label("loc_286A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_288E")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_288E")

    label("loc_288E")

    TalkEnd(0xFF)
    Return()

    # Function_16_27F4 end

    def Function_17_2892(): pass

    label("Function_17_2892")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #44
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2908")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xC, 0)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_64(0x3, 0x1)
    OP_10(0x18, 0x1)
    OP_A2(0x2B5D)
    Jump("loc_292C")

    label("loc_2908")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_292C")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_292C")

    label("loc_292C")

    TalkEnd(0xFF)
    Return()

    # Function_17_2892 end

    def Function_18_2930(): pass

    label("Function_18_2930")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #45
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29A6")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x13, 0)
    OP_70(0x13, 0x1E)
    OP_73(0x13)
    OP_64(0x4, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x2B5E)
    Jump("loc_29CA")

    label("loc_29A6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_29CA")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_29CA")

    label("loc_29CA")

    TalkEnd(0xFF)
    Return()

    # Function_18_2930 end

    def Function_19_29CE(): pass

    label("Function_19_29CE")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #46
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A44")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x9, 0)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_64(0x5, 0x1)
    OP_10(0x2, 0x1)
    OP_A2(0x2B5F)
    Jump("loc_2A68")

    label("loc_2A44")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2A68")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2A68")

    label("loc_2A68")

    TalkEnd(0xFF)
    Return()

    # Function_19_29CE end

    def Function_20_2A6C(): pass

    label("Function_20_2A6C")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #47
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 21)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE2")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0xF, 0)
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    OP_64(0x6, 0x1)
    OP_10(0x1E, 0x1)
    OP_A2(0x2B60)
    Jump("loc_2B06")

    label("loc_2AE2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2B06")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_2B06")

    label("loc_2B06")

    TalkEnd(0xFF)
    Return()

    # Function_20_2A6C end

    def Function_21_2B0A(): pass

    label("Function_21_2B0A")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x561, 7)), scpexpr(EXPR_END)), "loc_2B25")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2B25")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 1)), scpexpr(EXPR_END)), "loc_2B36")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2B36")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x562, 3)), scpexpr(EXPR_END)), "loc_2B47")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_2B47")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_2B73"),
        (1, "loc_2B80"),
        (3, "loc_2BDE"),
        (7, "loc_2C62"),
        (SWITCH_DEFAULT, "loc_2D0C"),
    )


    label("loc_2B73")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D0C")

    label("loc_2B80")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【什么也不做】\x01",            # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2BC1"),
        (1, "loc_2BCE"),
        (SWITCH_DEFAULT, "loc_2BDB"),
    )


    label("loc_2BC1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDB")

    label("loc_2BCE")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2BDB")

    label("loc_2BDB")

    Jump("loc_2D0C")

    label("loc_2BDE")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【什么也不做】\x01",            # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2C38"),
        (1, "loc_2C45"),
        (2, "loc_2C52"),
        (SWITCH_DEFAULT, "loc_2C5F"),
    )


    label("loc_2C38")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C5F")

    label("loc_2C45")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C5F")

    label("loc_2C52")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2C5F")

    label("loc_2C5F")

    Jump("loc_2D0C")

    label("loc_2C62")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色卡片钥匙】\x01",      # 0
            "【使用绿色卡片钥匙】\x01",      # 1
            "【使用蓝色卡片钥匙】\x01",      # 2
            "【什么也不做】\x01",            # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2CD5"),
        (1, "loc_2CE2"),
        (2, "loc_2CEF"),
        (3, "loc_2CFC"),
        (SWITCH_DEFAULT, "loc_2D09"),
    )


    label("loc_2CD5")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D09")

    label("loc_2CE2")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D09")

    label("loc_2CEF")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D09")

    label("loc_2CFC")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_2D09")

    label("loc_2D09")

    Jump("loc_2D0C")

    label("loc_2D0C")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_21_2B0A end

    def Function_22_2D24(): pass

    label("Function_22_2D24")

    OP_A3(0x2B64)
    OP_A2(0x2B65)
    OP_A3(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_22_2D24 end

    def Function_23_2D37(): pass

    label("Function_23_2D37")

    OP_A3(0x2B64)
    OP_A3(0x2B65)
    OP_A2(0x2B66)
    OP_A3(0x2B67)
    OP_A3(0x2B68)
    OP_A3(0x2B69)
    Return()

    # Function_23_2D37 end

    SaveToFile()

Try(main)
