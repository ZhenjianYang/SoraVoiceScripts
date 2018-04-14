from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5612   ._SN',
        MapName             = 'Other',
        Location            = 'C5612.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60061",
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
        '',                                     # 9
        '',                                     # 10
        '',                                     # 11
        '',                                     # 12
        '',                                     # 13
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
        'ED6_DT29/CH12570 ._CH',             # 00
        'ED6_DT29/CH12571 ._CH',             # 01
        'ED6_DT29/CH12320 ._CH',             # 02
        'ED6_DT29/CH12321 ._CH',             # 03
        'ED6_DT29/CH12330 ._CH',             # 04
        'ED6_DT29/CH12331 ._CH',             # 05
        'ED6_DT29/CH12350 ._CH',             # 06
        'ED6_DT29/CH12351 ._CH',             # 07
        'ED6_DT29/CH12000 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12570P._CP',             # 00
        'ED6_DT29/CH12571P._CP',             # 01
        'ED6_DT29/CH12320P._CP',             # 02
        'ED6_DT29/CH12321P._CP',             # 03
        'ED6_DT29/CH12330P._CP',             # 04
        'ED6_DT29/CH12331P._CP',             # 05
        'ED6_DT29/CH12350P._CP',             # 06
        'ED6_DT29/CH12351P._CP',             # 07
        'ED6_DT29/CH12000P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
    )

    DeclNpc(
        X                   = 55620,
        Z                   = 9000,
        Y                   = 35600,
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
        X                   = 60070,
        Z                   = 0,
        Y                   = 33920,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x14D,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -22330,
        Z                   = 0,
        Y                   = 127860,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -13930,
        Z                   = 0,
        Y                   = -4390,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -840,
        Z                   = 0,
        Y                   = 6830,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -68950,
        Z                   = 0,
        Y                   = 155090,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 97120,
        Z                   = 0,
        Y                   = 86150,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x41D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = 48040,
        Y                   = -1000,
        Z                   = 131420,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 22,
    )

    DeclEvent(
        X                   = 36070,
        Y                   = -1000,
        Z                   = 131620,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 23,
    )


    DeclActor(
        TriggerX            = -69010,
        TriggerZ            = 0,
        TriggerY            = 148300,
        TriggerRange        = 1000,
        ActorX              = -69010,
        ActorZ              = 0,
        ActorY              = 148960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 55620,
        TriggerZ            = 8000,
        TriggerY            = 34900,
        TriggerRange        = 1000,
        ActorX              = 55620,
        ActorZ              = 8000,
        ActorY              = 35600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -1700,
        TriggerZ            = 0,
        TriggerY            = -4650,
        TriggerRange        = 1000,
        ActorX              = -1040,
        ActorZ              = 0,
        ActorY              = -4650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27290,
        TriggerZ            = 0,
        TriggerY            = 9990,
        TriggerRange        = 1000,
        ActorX              = -27990,
        ActorZ              = 0,
        ActorY              = 9990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -27290,
        TriggerZ            = 0,
        TriggerY            = 7570,
        TriggerRange        = 1000,
        ActorX              = -27950,
        ActorZ              = 0,
        ActorY              = 7570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -70540,
        TriggerZ            = 0,
        TriggerY            = 100850,
        TriggerRange        = 800,
        ActorX              = -70540,
        ActorZ              = 1100,
        ActorY              = 100850,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 37890,
        TriggerZ            = 0,
        TriggerY            = 131750,
        TriggerRange        = 800,
        ActorX              = 37890,
        ActorZ              = 1100,
        ActorY              = 131750,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -8010,
        TriggerZ            = 720,
        TriggerY            = -2040,
        TriggerRange        = 800,
        ActorX              = -8010,
        ActorZ              = 720,
        ActorY              = -2040,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 20,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -21970,
        TriggerZ            = 20,
        TriggerY            = -1650,
        TriggerRange        = 800,
        ActorX              = -21970,
        ActorZ              = 20,
        ActorY              = -1650,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 21,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_34A",          # 00, 0
        "Function_1_37C",          # 01, 1
        "Function_2_46D",          # 02, 2
        "Function_3_483",          # 03, 3
        "Function_4_55C",          # 04, 4
        "Function_5_72C",          # 05, 5
        "Function_6_843",          # 06, 6
        "Function_7_95A",          # 07, 7
        "Function_8_A71",          # 08, 8
        "Function_9_B0D",          # 09, 9
        "Function_10_BA9",         # 0A, 10
        "Function_11_DB7",         # 0B, 11
        "Function_12_1482",        # 0C, 12
        "Function_13_149E",        # 0D, 13
        "Function_14_14BA",        # 0E, 14
        "Function_15_14D6",        # 0F, 15
        "Function_16_14F2",        # 10, 16
        "Function_17_1BF0",        # 11, 17
        "Function_18_22F5",        # 12, 18
        "Function_19_237F",        # 13, 19
        "Function_20_23DC",        # 14, 20
        "Function_21_2858",        # 15, 21
        "Function_22_2E13",        # 16, 22
        "Function_23_2E26",        # 17, 23
    )


    def Function_0_34A(): pass

    label("Function_0_34A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_37B")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_END)),
        (122, "loc_366"),
        (123, "loc_36D"),
        (124, "loc_374"),
        (SWITCH_DEFAULT, "loc_37B"),
    )


    label("loc_366")

    Event(0, 11)
    Jump("loc_37B")

    label("loc_36D")

    Event(0, 16)
    Jump("loc_37B")

    label("loc_374")

    Event(0, 17)
    Jump("loc_37B")

    label("loc_37B")

    Return()

    # Function_0_34A end

    def Function_1_37C(): pass

    label("Function_1_37C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_38E")
    OP_6F(0x0, 0)
    Jump("loc_395")

    label("loc_38E")

    OP_6F(0x0, 60)

    label("loc_395")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3A7")
    OP_6F(0x1, 0)
    Jump("loc_3AE")

    label("loc_3A7")

    OP_6F(0x1, 60)

    label("loc_3AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C0")
    OP_6F(0x2, 0)
    Jump("loc_3C7")

    label("loc_3C0")

    OP_6F(0x2, 60)

    label("loc_3C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9")
    OP_6F(0x3, 0)
    Jump("loc_3E0")

    label("loc_3D9")

    OP_6F(0x3, 60)

    label("loc_3E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3F2")
    OP_6F(0x4, 0)
    Jump("loc_3F9")

    label("loc_3F2")

    OP_6F(0x4, 60)

    label("loc_3F9")

    OP_A1(0x9, 0x12)
    SetChrFlags(0x9, 0x1)
    OP_51(0x9, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_OR), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x7, (scpexpr(EXPR_PUSH_LONG, 0x1770), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x9, 0x34, (scpexpr(EXPR_PUSH_LONG, 0xC350), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 0)), scpexpr(EXPR_END)), "loc_446")
    OP_64(0x5, 0x1)
    OP_10(0xE, 0x1)
    OP_71(0x8, 0x10)
    Jump("loc_44E")

    label("loc_446")

    OP_10(0x8, 0x0)
    OP_72(0x8, 0x10)

    label("loc_44E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x383, 1)), scpexpr(EXPR_END)), "loc_464")
    OP_64(0x6, 0x1)
    OP_10(0x1, 0x1)
    OP_71(0x10, 0x10)
    Jump("loc_46C")

    label("loc_464")

    OP_10(0x1, 0x0)
    OP_72(0x10, 0x10)

    label("loc_46C")

    Return()

    # Function_1_37C end

    def Function_2_46D(): pass

    label("Function_2_46D")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_482")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_46D")

    label("loc_482")

    Return()

    # Function_2_46D end

    def Function_3_483(): pass

    label("Function_3_483")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_530")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x1E)
    OP_73(0x0)
    OP_6F(0x0, 30)
    AddSepith(0x4, 0x32)
    AddSepith(0x5, 0x32)
    AddSepith(0x6, 0x32)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "\x07\x00得到了\x07\x02#62I时之耀晶片×５０\x01",
            "\x07\x02#60I空之耀晶片×５０\x01",
            "\x07\x02#61I幻之耀晶片×５０\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1D20)
    Jump("loc_54A")

    label("loc_530")


    AnonymousTalk(    #1
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_54A")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_483 end

    def Function_4_55C(): pass

    label("Function_4_55C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6EF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_63B")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_5AE():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_5AE)

    def lambda_5C9():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_5C9)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #2
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x423, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_616"),
        (2, "loc_628"),
        (1, "loc_638"),
        (SWITCH_DEFAULT, "loc_63B"),
    )


    label("loc_616")

    OP_A2(0x1D23)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_63B")

    label("loc_628")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_638")

    OP_B4(0x0)
    Return()

    label("loc_63B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x298, 1)"), scpexpr(EXPR_END)), "loc_68A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #3
        "\x07\x00得到了\x1F\x98\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D22)
    Jump("loc_6EC")

    label("loc_68A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #4
        (
            "宝箱里装有\x1F\x98\x02\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x98\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_6EC")

    Jump("loc_71E")

    label("loc_6EF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_71E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_55C end

    def Function_5_72C(): pass

    label("Function_5_72C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_804")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x162, 1)"), scpexpr(EXPR_END)), "loc_79B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\x62\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D24)
    Jump("loc_801")

    label("loc_79B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\x62\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x62\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_801")

    Jump("loc_835")

    label("loc_804")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_835")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_72C end

    def Function_6_843(): pass

    label("Function_6_843")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_91B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x202, 1)"), scpexpr(EXPR_END)), "loc_8B2")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\x02\x02\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D26)
    Jump("loc_918")

    label("loc_8B2")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\x02\x02\x07\x00。   \x01",
            "所持物品已经满了，\x1F\x02\x02\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_918")

    Jump("loc_94C")

    label("loc_91B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_94C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_843 end

    def Function_7_95A(): pass

    label("Function_7_95A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x3A4, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_A32")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_9C9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #12
        "\x07\x00得到了\x1F\xF6\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1D27)
    Jump("loc_A2F")

    label("loc_9C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        (
            "宝箱里装有\x1F\xF6\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xF6\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_A2F")

    Jump("loc_A63")

    label("loc_A32")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_A63")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_95A end

    def Function_8_A71(): pass

    label("Function_8_A71")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #15
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AE5")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x8, 0)
    OP_70(0x8, 0x1E)
    OP_73(0x11)
    OP_64(0x5, 0x1)
    OP_10(0xE, 0x1)
    OP_A2(0x1C18)
    Jump("loc_B09")

    label("loc_AE5")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_B09")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_B09")

    label("loc_B09")

    TalkEnd(0xFF)
    Return()

    # Function_8_A71 end

    def Function_9_B0D(): pass

    label("Function_9_B0D")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05门被锁上了。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    Call(0, 10)
    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B81")
    OP_22(0x9D, 0x0, 0x64)
    Sleep(1000)
    OP_6F(0x10, 0)
    OP_70(0x10, 0x1E)
    OP_73(0x10)
    OP_64(0x6, 0x1)
    OP_10(0x1, 0x1)
    OP_A2(0x1C19)
    Jump("loc_BA5")

    label("loc_B81")

    Jc((scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_GET_RESULT, 0x3), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_BA5")
    OP_22(0xAB, 0x0, 0x64)
    Sleep(1000)
    Jump("loc_BA5")

    label("loc_BA5")

    TalkEnd(0xFF)
    Return()

    # Function_9_B0D end

    def Function_10_BA9(): pass

    label("Function_10_BA9")

    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 1)), scpexpr(EXPR_END)), "loc_BC4")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_BC4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 4)), scpexpr(EXPR_END)), "loc_BD5")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_BD5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x381, 6)), scpexpr(EXPR_END)), "loc_BE6")
    RunExpression(0x2, (scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_OR_SAVE), scpexpr(EXPR_END)))

    label("loc_BE6")

    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_END)),
        (0, "loc_C12"),
        (1, "loc_C1F"),
        (3, "loc_C7B"),
        (7, "loc_CFB"),
        (SWITCH_DEFAULT, "loc_D9F"),
    )


    label("loc_C12")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9F")

    label("loc_C1F")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【什么也不做】\x01",          # 1
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_C5E"),
        (1, "loc_C6B"),
        (SWITCH_DEFAULT, "loc_C78"),
    )


    label("loc_C5E")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C78")

    label("loc_C6B")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_C78")

    label("loc_C78")

    Jump("loc_D9F")

    label("loc_C7B")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【什么也不做】\x01",          # 2
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_CD1"),
        (1, "loc_CDE"),
        (2, "loc_CEB"),
        (SWITCH_DEFAULT, "loc_CF8"),
    )


    label("loc_CD1")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CDE")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CEB")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_CF8")

    label("loc_CF8")

    Jump("loc_D9F")

    label("loc_CFB")


    Menu(
        0,
        10,
        100,
        0,
        (
            "【使用红色密码卡】\x01",      # 0
            "【使用绿色密码卡】\x01",      # 1
            "【使用蓝色密码卡】\x01",      # 2
            "【什么也不做】\x01",          # 3
        )
    )

    MenuEnd(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_D68"),
        (1, "loc_D75"),
        (2, "loc_D82"),
        (3, "loc_D8F"),
        (SWITCH_DEFAULT, "loc_D9C"),
    )


    label("loc_D68")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D75")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D82")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D8F")

    RunExpression(0x3, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_D9C")

    label("loc_D9C")

    Jump("loc_D9F")

    label("loc_D9F")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    FadeToBright(300, 0)
    Return()

    # Function_10_BA9 end

    def Function_11_DB7(): pass

    label("Function_11_DB7")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_DCE")
    Call(0, 18)
    Call(0, 19)

    label("loc_DCE")

    SetChrPos(0x101, 67270, 0, 29420, 270)
    SetChrPos(0x109, 67270, 0, 28510, 270)
    SetChrPos(0xF8, 68260, 0, 28510, 270)
    SetChrPos(0xF9, 68260, 0, 29420, 270)
    OP_6D(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EB3")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EF1")

    label("loc_EB3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_EDA")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_EF1")

    label("loc_EDA")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_EF1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F18")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F56")

    label("loc_F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_F3F")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_F56")

    label("loc_F3F")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_F56")

    Sleep(1000)
    OP_8C(0x101, 315, 400)
    OP_8C(0x109, 315, 400)
    OP_8C(0xF8, 315, 400)
    OP_8C(0xF9, 315, 400)

    def lambda_F7D():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_F7D)

    def lambda_F95():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_F95)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(67730, 0, 29250, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #17
        0x101,
        "#1020F#6P那、那个时候的机械兽！？\x02",
    )

    CloseMessageWindow()

    def lambda_1022():
        OP_6D(59730, 0, 33680, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1022)

    def lambda_103A():
        OP_67(0, 8070, -10000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_103A)

    def lambda_1052():
        OP_6B(2800, 4000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1052)

    def lambda_1062():
        OP_6C(350000, 4000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1062)

    def lambda_1072():
        OP_6E(302, 4000)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_1072)
    OP_43(0x109, 0x1, 0x0, 0xD)
    Sleep(100)
    OP_43(0xF8, 0x1, 0x0, 0xE)
    Sleep(400)
    OP_43(0x101, 0x1, 0x0, 0xC)
    Sleep(100)
    OP_43(0xF9, 0x1, 0x0, 0xF)
    WaitChrThread(0xF8, 0x1)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #18
        0x109,
        (
            "#1064F#6P啊～确实和王城地下\x01",
            "是同样的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x101,
        (
            "#1026F#6P为、为什么\x01",
            "这里会有那种东西……\x02\x03",

            "#1019F我是说，那种怪物\x01",
            "怎么会有两台这么多！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_131E")

    ChrTalk(    #20
        0x107,
        (
            "#065F#6P不、不清楚……\x02\x03",

            "不过这里好像是研究设施，\x01",
            "可能进行了不少调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #21
        0x101,
        "#1015F#6P调查？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x107,
        (
            "#561F#6P嗯……\x02\x03",

            "作为开发独创的人形兵器时\x01",
            "参考之用等等的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1224")

    ChrTalk(    #23
        0x106,
        "#057F#6P原来如此……有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_1224")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1259")

    ChrTalk(    #24
        0x103,
        "#022F#6P原来如此……有可能呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_1259")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1290")

    ChrTalk(    #25
        0x105,
        "#042F#6P这个可能性似乎很高呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_1290")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12BD")

    ChrTalk(    #26
        0x108,
        "#072F#6P这很有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_12E9")

    label("loc_12BD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12E9")

    ChrTalk(    #27
        0x104,
        "#032F#6P唔……有可能呢。\x02",
    )

    CloseMessageWindow()

    label("loc_12E9")


    ChrTalk(    #28
        0x109,
        (
            "#1068F#6P看来这是超乎预料之外\x01",
            "的危险设施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1477")

    label("loc_131E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1375")

    ChrTalk(    #29
        0x104,
        (
            "#035F#6P这就不清楚了……\x02\x03",

            "#032F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1477")

    label("loc_1375")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13CC")

    ChrTalk(    #30
        0x108,
        (
            "#074F#6P这就不清楚了……\x02\x03",

            "#072F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1477")

    label("loc_13CC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1423")

    ChrTalk(    #31
        0x105,
        (
            "#047F#6P这就不清楚了……\x02\x03",

            "#042F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1477")

    label("loc_1423")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1477")

    ChrTalk(    #32
        0x103,
        (
            "#026F#6P这就不清楚了……\x02\x03",

            "#022F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1477")

    Sleep(200)
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_11_DB7 end

    def Function_12_1482(): pass

    label("Function_12_1482")

    OP_8E(0xFE, 0xEED4, 0x14, 0x7986, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_12_1482 end

    def Function_13_149E(): pass

    label("Function_13_149E")

    OP_8E(0xFE, 0xE970, 0x14, 0x78FA, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_13_149E end

    def Function_14_14BA(): pass

    label("Function_14_14BA")

    OP_8E(0xFE, 0xE8E4, 0x14, 0x7454, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_14_14BA end

    def Function_15_14D6(): pass

    label("Function_15_14D6")

    OP_8E(0xFE, 0xEE8E, 0x14, 0x7472, 0xBB8, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_15_14D6 end

    def Function_16_14F2(): pass

    label("Function_16_14F2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1509")
    Call(0, 18)
    Call(0, 19)

    label("loc_1509")

    SetChrPos(0x101, 60570, 4000, 21850, 0)
    SetChrPos(0x109, 59450, 4000, 21810, 0)
    SetChrPos(0xF8, 59430, 4000, 20670, 0)
    SetChrPos(0xF9, 60900, 4000, 20660, 0)
    OP_6D(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(80)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_15EE")
    OP_62(0xF8, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_162C")

    label("loc_15EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF8)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1615")
    OP_62(0xF8, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_162C")

    label("loc_1615")

    OP_62(0xF8, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_162C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1653")
    OP_62(0xF9, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1691")

    label("loc_1653")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0xF9)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_167A")
    OP_62(0xF9, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1691")

    label("loc_167A")

    OP_62(0xF9, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1691")

    Sleep(1000)

    def lambda_169C():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_169C)

    def lambda_16B4():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_16B4)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(59880, 4000, 21450, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #33
        0x101,
        "#1020F#6P那、那个时候的机械兽！？\x02",
    )

    CloseMessageWindow()

    def lambda_1741():
        OP_6D(59950, 4000, 27700, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1741)

    def lambda_1759():
        OP_6C(327000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1759)

    def lambda_1769():
        OP_6E(283, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1769)

    def lambda_1779():
        OP_67(0, 7140, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1779)

    def lambda_1791():
        OP_8E(0xFE, 0xEC0E, 0xFA0, 0x5B72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1791)
    Sleep(50)

    def lambda_17B1():
        OP_8E(0xFE, 0xE8DA, 0xFA0, 0x5B72, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_17B1)
    Sleep(100)

    def lambda_17D1():
        OP_8E(0xFE, 0xE5B0, 0xFA0, 0x583E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_17D1)
    Sleep(60)

    def lambda_17F1():
        OP_8E(0xFE, 0xF0DC, 0xFA0, 0x578A, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_17F1)
    WaitChrThread(0xF8, 0x1)
    OP_8C(0xF8, 0, 400)
    WaitChrThread(0xF9, 0x1)
    OP_8C(0xF9, 0, 400)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #34
        0x109,
        (
            "#1064F#6P啊～确实和王城地下\x01",
            "是同样的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #35
        0x101,
        (
            "#1026F#6P为、为什么\x01",
            "这里会有那种东西……\x02\x03",

            "#1019F我是说，那种怪物\x01",
            "怎么会有两台这么多！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A8C")

    ChrTalk(    #36
        0x107,
        (
            "#065F#6P不、不清楚……\x02\x03",

            "不过这里好像是研究设施，\x01",
            "可能进行了不少调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x101,
        "#1015F#6P调查？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x107,
        (
            "#561F#6P嗯……\x02\x03",

            "作为开发独创的人形兵器时\x01",
            "参考之用等等的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1996")

    ChrTalk(    #39
        0x106,
        "#057F#6P原来如此……有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_1996")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_19CB")

    ChrTalk(    #40
        0x103,
        "#022F#6P原来如此……有可能呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_19CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A02")

    ChrTalk(    #41
        0x105,
        "#042F#6P这个可能性似乎很高呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_1A02")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A2F")

    ChrTalk(    #42
        0x108,
        "#072F#6P这很有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_1A5B")

    label("loc_1A2F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1A5B")

    ChrTalk(    #43
        0x104,
        "#032F#6P唔……有可能呢。\x02",
    )

    CloseMessageWindow()

    label("loc_1A5B")


    ChrTalk(    #44
        0x109,
        (
            "#1068F#6P看来这是超乎预想\x01",
            "的危险设施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE5")

    label("loc_1A8C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AE3")

    ChrTalk(    #45
        0x104,
        (
            "#035F#6P这就不清楚了……\x02\x03",

            "#032F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE5")

    label("loc_1AE3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B3A")

    ChrTalk(    #46
        0x108,
        (
            "#074F#6P这就不清楚了……\x02\x03",

            "#072F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE5")

    label("loc_1B3A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B91")

    ChrTalk(    #47
        0x105,
        (
            "#047F#6P这就不清楚了……\x02\x03",

            "#042F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_1BE5")

    label("loc_1B91")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1BE5")

    ChrTalk(    #48
        0x103,
        (
            "#026F#6P这就不清楚了……\x02\x03",

            "#022F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_1BE5")

    Sleep(200)
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_16_14F2 end

    def Function_17_1BF0(): pass

    label("Function_17_1BF0")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1C07")
    Call(0, 18)
    Call(0, 19)

    label("loc_1C07")

    SetChrPos(0x101, 52920, 8000, 28620, 90)
    SetChrPos(0x109, 52800, 8000, 29590, 90)
    SetChrPos(0xF8, 51980, 8000, 28450, 90)
    SetChrPos(0xF9, 51750, 8000, 29450, 90)
    OP_6D(52120, 8000, 28960, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    OP_0D()

    ChrTalk(    #49
        0x101,
        (
            "#1004F#5P啊……\x01",
            "这里是楼梯井？\x02",
        )
    )

    CloseMessageWindow()
    OP_8F(0x101, 0xD46C, 0x1F40, 0x72D8, 0x7D0, 0x0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    def lambda_1CEC():
        OP_6D(59860, 0, 35220, 4000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_1CEC)

    def lambda_1D04():
        OP_6C(333000, 4000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D04)
    OP_6E(238, 4000)
    Sleep(1000)
    Fade(500)
    OP_6D(52850, 8000, 29240, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_0D()
    Sleep(200)

    ChrTalk(    #50
        0x101,
        "#1020F#5P那、那个时候的机械兽！？\x02",
    )

    CloseMessageWindow()

    def lambda_1D91():
        OP_6D(60080, 8000, 30590, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1D91)

    def lambda_1DA9():
        OP_67(0, 8189, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_1DA9)

    def lambda_1DC1():
        OP_6C(297000, 3000)
        ExitThread()

    QueueWorkItem(0x109, 2, lambda_1DC1)

    def lambda_1DD1():
        OP_6E(363, 3000)
        ExitThread()

    QueueWorkItem(0x109, 3, lambda_1DD1)

    def lambda_1DE1():
        OP_6B(2710, 3000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_1DE1)

    def lambda_1DF1():
        OP_8E(0xFE, 0xD444, 0x1F40, 0x75F8, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1DF1)
    Sleep(50)

    def lambda_1E11():
        OP_8E(0xFE, 0xD426, 0x1F40, 0x790E, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1E11)
    Sleep(50)

    def lambda_1E31():
        OP_8E(0xFE, 0xD46C, 0x1F40, 0x6F86, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1E31)
    WaitChrThread(0x109, 0x1)

    def lambda_1E51():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x109, 1, lambda_1E51)
    WaitChrThread(0xF8, 0x1)

    def lambda_1E64():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_1E64)
    WaitChrThread(0xF9, 0x1)

    def lambda_1E77():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_1E77)
    WaitChrThread(0x109, 0x2)

    ChrTalk(    #51
        0x109,
        (
            "#1064F#6P从这里\x01",
            "有点看不清楚……\x02\x03",

            "不过确实和王城地下\x01",
            "是同样的类型。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #52
        0x101,
        (
            "#1026F#6P为、为什么\x01",
            "这里会有那种东西……\x02\x03",

            "#1019F我是说，那种怪物\x01",
            "怎么会有两台这么多！？\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_210A")

    ChrTalk(    #53
        0x107,
        (
            "#065F#6P不、不清楚……\x02\x03",

            "不过这里好像是研究设施，\x01",
            "可能进行了不少调查……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #54
        0x101,
        "#1015F#6P调查？\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #55
        0x107,
        (
            "#561F#6P嗯……\x02\x03",

            "作为开发独创的人形兵器时\x01",
            "参考之用等等的……\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2010")

    ChrTalk(    #56
        0x106,
        "#057F#6P原来如此……有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D5")

    label("loc_2010")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2045")

    ChrTalk(    #57
        0x103,
        "#022F#6P原来如此……有可能呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D5")

    label("loc_2045")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_207C")

    ChrTalk(    #58
        0x105,
        "#042F#6P这个可能性似乎很高呢……\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D5")

    label("loc_207C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20A9")

    ChrTalk(    #59
        0x108,
        "#072F#6P这很有可能啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_20D5")

    label("loc_20A9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_20D5")

    ChrTalk(    #60
        0x104,
        "#032F#6P唔……有可能呢。\x02",
    )

    CloseMessageWindow()

    label("loc_20D5")


    ChrTalk(    #61
        0x109,
        (
            "#1068F#6P看来这是超乎预料之外\x01",
            "的危险设施啊。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2263")

    label("loc_210A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2161")

    ChrTalk(    #62
        0x104,
        (
            "#035F#6P这就不清楚了……\x02\x03",

            "#032F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2263")

    label("loc_2161")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_21B8")

    ChrTalk(    #63
        0x108,
        (
            "#074F#6P这就不清楚了……\x02\x03",

            "#072F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2263")

    label("loc_21B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_220F")

    ChrTalk(    #64
        0x105,
        (
            "#047F#6P这就不清楚了……\x02\x03",

            "#042F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2263")

    label("loc_220F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2263")

    ChrTalk(    #65
        0x103,
        (
            "#026F#6P这就不清楚了……\x02\x03",

            "#022F看来是超乎预料之外\x01",
            "的危险设施呢。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2263")

    Sleep(200)
    Fade(500)
    OP_6D(54380, 8000, 29400, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 54380, 8000, 29400, 90)
    SetChrPos(0x1, 54380, 8000, 29400, 90)
    SetChrPos(0x2, 54380, 8000, 29400, 90)
    SetChrPos(0x3, 54380, 8000, 29400, 90)
    OP_0D()
    OP_A2(0x1C0A)
    EventEnd(0x0)
    Return()

    # Function_17_1BF0 end

    def Function_18_22F5(): pass

    label("Function_18_22F5")

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
            "【◇选择雪拉扎德为队友】\x01",      # 0
            "【◇选择阿加特为队友】\x01",        # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_2372"),
        (1, "loc_2378"),
        (SWITCH_DEFAULT, "loc_237E"),
    )


    label("loc_2372")

    OP_A2(0x1200)
    Jump("loc_237E")

    label("loc_2378")

    OP_A2(0x1201)
    Jump("loc_237E")

    label("loc_237E")

    Return()

    # Function_18_22F5 end

    def Function_19_237F(): pass

    label("Function_19_237F")

    ClearMapFlags(0x1)
    OP_6D(64510, 0, -14780, 92)
    Sleep(100)
    FadeToBright(0, 0)
    OP_C9(0x0, 0x4, 0x0, 0x8, 0xFF, 0xFF, 0x5, 0x2, 0x6, 0x3, 0x4, 0x7, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Sleep(1000)
    Return()

    # Function_19_237F end

    def Function_20_23DC(): pass

    label("Function_20_23DC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2619")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #66
        "\x07\x05有大型的『福音』。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #67
        0x101,
        (
            "#1004F咦……这不是\x01",
            "新型福音吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -7520, 20, -3140, 0)
    SetChrPos(0x1, -8620, 20, -3320, 0)
    SetChrPos(0x2, -9230, 20, -4070, 0)
    SetChrPos(0x3, -6590, 20, -3840, 0)

    def lambda_24AF():
        OP_6D(-8010, 730, -510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_24AF)

    def lambda_24C7():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_24C7)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2508")

    ChrTalk(    #68
        0x105,
        "#042F看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A9")

    label("loc_2508")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2530")

    ChrTalk(    #69
        0x104,
        "#032F看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A9")

    label("loc_2530")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2558")

    ChrTalk(    #70
        0x106,
        "#050F看来没错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A9")

    label("loc_2558")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2584")

    ChrTalk(    #71
        0x107,
        "#062F嗯，看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_25A9")

    label("loc_2584")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A9")

    ChrTalk(    #72
        0x108,
        "#072F看来没错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_25A9")


    ChrTalk(    #73
        0x101,
        (
            "#1015F……新型福音\x01",
            "就是在这个设施制造出来的啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        (
            "#1063F没想到，『福音』\x01",
            "竟然是在利贝尔制造的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C90)
    EventEnd(0x0)
    Jump("loc_2857")

    label("loc_2619")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2829")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #75
        "\x07\x05有大型的『福音』。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_8C(0x0, 0, 400)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #76
        0x101,
        (
            "#1004F咦……这不是\x01",
            "新型福音吗？\x02",
        )
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -7520, 20, -3140, 0)
    SetChrPos(0x1, -8620, 20, -3320, 0)
    SetChrPos(0x2, -9230, 20, -4070, 0)
    SetChrPos(0x3, -6590, 20, -3840, 0)

    def lambda_26F2():
        OP_6D(-8010, 730, -510, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_26F2)

    def lambda_270A():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_270A)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_274B")

    ChrTalk(    #77
        0x105,
        "#042F看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_274B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2773")

    ChrTalk(    #78
        0x104,
        "#032F看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_2773")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_279B")

    ChrTalk(    #79
        0x106,
        "#050F看来没错啊。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_279B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27C7")

    ChrTalk(    #80
        0x107,
        "#062F嗯，看来没错呢。\x02",
    )

    CloseMessageWindow()
    Jump("loc_27EC")

    label("loc_27C7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_27EC")

    ChrTalk(    #81
        0x108,
        "#072F看来没错啊。\x02",
    )

    CloseMessageWindow()

    label("loc_27EC")


    ChrTalk(    #82
        0x101,
        (
            "#1015F……新型福音\x01",
            "就是在这个设施制造出来的啊。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C90)
    EventEnd(0x0)
    Jump("loc_2857")

    label("loc_2829")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #83
        "\x07\x05有大型的福音。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_2857")

    Return()

    # Function_20_23DC end

    def Function_21_2858(): pass

    label("Function_21_2858")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B2E")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #84
        "\x07\x05有制作成『桩』的形状的装置。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #85
        0x101,
        "#1004F咦……这个难道是……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -21420, 20, -3140, 0)
    SetChrPos(0x1, -22470, 20, -3320, 0)
    SetChrPos(0x2, -23030, 20, -4070, 0)
    SetChrPos(0x3, -20590, 20, -3840, 0)

    def lambda_2930():
        OP_6D(-21890, 1010, -480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2930)

    def lambda_2948():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2948)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29A8")

    ChrTalk(    #86
        0x108,
        (
            "#072F嗯，看来和瓦鲁特使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_29A8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_29F5")

    ChrTalk(    #87
        0x107,
        (
            "#062F嗯，似乎和在蔡斯扰乱\x01",
            "七耀脉的『桩』是同样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_29F5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A3C")

    ChrTalk(    #88
        0x103,
        (
            "#022F这好像和『瘦狼』使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_2A3C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A83")

    ChrTalk(    #89
        0x106,
        (
            "#050F这好像和『瘦狼』使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2ACB")

    label("loc_2A83")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2ACB")

    ChrTalk(    #90
        0x104,
        (
            "#032F唔，看来和在蔡斯引起地震的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2ACB")


    ChrTalk(    #91
        0x101,
        "#1015F……那个装置是这里制造的啊。\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #92
        0x109,
        (
            "#1063F没想到，这种东西\x01",
            "竟然是在利贝尔制造的。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x1C91)
    EventEnd(0x0)
    Jump("loc_2E12")

    label("loc_2B2E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 0)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x392, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2DD6")
    EventBegin(0x0)
    FadeToDark(300, 0, 100)

    AnonymousTalk(    #93
        "\x07\x05有制作成『桩』的形状的装置。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_62(0x101, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #94
        0x101,
        "#1004F咦……这个难道是……\x02",
    )

    CloseMessageWindow()
    Sleep(200)
    Fade(3000)
    SetChrPos(0x0, -21420, 20, -3140, 0)
    SetChrPos(0x1, -22470, 20, -3320, 0)
    SetChrPos(0x2, -23030, 20, -4070, 0)
    SetChrPos(0x3, -20590, 20, -3840, 0)

    def lambda_2C05():
        OP_6D(-21890, 1010, -480, 2000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_2C05)

    def lambda_2C1D():
        OP_6C(333000, 2000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_2C1D)
    OP_6E(238, 2000)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2C7D")

    ChrTalk(    #95
        0x108,
        (
            "#072F唔，看来和瓦鲁特使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA0")

    label("loc_2C7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2CCA")

    ChrTalk(    #96
        0x107,
        (
            "#062F嗯，似乎和在蔡斯扰乱\x01",
            "七耀脉的『桩』是同样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA0")

    label("loc_2CCA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D11")

    ChrTalk(    #97
        0x103,
        (
            "#022F这好像和『瘦狼』使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA0")

    label("loc_2D11")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2D58")

    ChrTalk(    #98
        0x106,
        (
            "#050F这好像和『瘦狼』使用的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_2DA0")

    label("loc_2D58")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA0")

    ChrTalk(    #99
        0x104,
        (
            "#032F唔，看来和在蔡斯引起地震的\x01",
            "『桩』是一样的东西。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2DA0")


    ChrTalk(    #100
        0x101,
        "#1015F……连那个装置都是在这里制造的啊。\x02",
    )

    CloseMessageWindow()
    OP_A2(0x1C91)
    EventEnd(0x0)
    Jump("loc_2E12")

    label("loc_2DD6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #101
        "\x07\x05有制作成『桩』的形状的装置。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)

    label("loc_2E12")

    Return()

    # Function_21_2858 end

    def Function_22_2E13(): pass

    label("Function_22_2E13")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A2(0x1C9D)
    OP_A3(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_22_2E13 end

    def Function_23_2E26(): pass

    label("Function_23_2E26")

    OP_A3(0x1C9A)
    OP_A3(0x1C9B)
    OP_A3(0x1C9C)
    OP_A3(0x1C9D)
    OP_A2(0x1C9E)
    OP_A3(0x1C9F)
    Return()

    # Function_23_2E26 end

    SaveToFile()

Try(main)
