from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5202   ._SN',
        MapName             = 'Other',
        Location            = 'C5202.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60063",
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
        'ED6_DT29/CH12950 ._CH',             # 00
        'ED6_DT29/CH12951 ._CH',             # 01
        'ED6_DT29/CH12000 ._CH',             # 02
        'ED6_DT29/CH12001 ._CH',             # 03
        'ED6_DT29/CH12960 ._CH',             # 04
        'ED6_DT29/CH12961 ._CH',             # 05
        'ED6_DT29/CH13010 ._CH',             # 06
        'ED6_DT29/CH13011 ._CH',             # 07
        'ED6_DT29/CH12200 ._CH',             # 08
        'ED6_DT29/CH12201 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT29/CH12950P._CP',             # 00
        'ED6_DT29/CH12951P._CP',             # 01
        'ED6_DT29/CH12000P._CP',             # 02
        'ED6_DT29/CH12001P._CP',             # 03
        'ED6_DT29/CH12960P._CP',             # 04
        'ED6_DT29/CH12961P._CP',             # 05
        'ED6_DT29/CH13010P._CP',             # 06
        'ED6_DT29/CH13011P._CP',             # 07
        'ED6_DT29/CH12200P._CP',             # 08
        'ED6_DT29/CH12201P._CP',             # 09
    )

    DeclNpc(
        X                   = 9910,
        Z                   = -3000,
        Y                   = 271990,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 7140,
        Z                   = 0,
        Y                   = 78500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x440,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -10,
        Z                   = 0,
        Y                   = 173660,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x442,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 20,
        Z                   = 0,
        Y                   = 271220,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x441,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -188060,
        Z                   = 0,
        Y                   = 155810,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x443,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -190000,
        Z                   = -4000,
        Y                   = 174020,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x442,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 18010,
        Z                   = 0,
        Y                   = 369940,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x441,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -14480,
        Z                   = 0,
        Y                   = 383370,
        Unknown_0C          = 180,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x444,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14180,
        Z                   = 0,
        Y                   = 384030,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x440,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 9290,
        TriggerZ            = -4000,
        TriggerY            = 271990,
        TriggerRange        = 1000,
        ActorX              = 9910,
        ActorZ              = -4000,
        ActorY              = 271990,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -2029,
        TriggerZ            = 0,
        TriggerY            = 449750,
        TriggerRange        = 1000,
        ActorX              = -2029,
        ActorZ              = 0,
        ActorY              = 450360,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 990,
        TriggerZ            = 0,
        TriggerY            = 449750,
        TriggerRange        = 1000,
        ActorX              = 990,
        ActorZ              = 0,
        ActorY              = 450410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4030,
        TriggerZ            = 0,
        TriggerY            = 449750,
        TriggerRange        = 1000,
        ActorX              = 4030,
        ActorZ              = 0,
        ActorY              = 450370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_28A",          # 00, 0
        "Function_1_28B",          # 01, 1
        "Function_2_2F0",          # 02, 2
        "Function_3_306",          # 03, 3
        "Function_4_4D6",          # 04, 4
        "Function_5_5D2",          # 05, 5
        "Function_6_6E9",          # 06, 6
    )


    def Function_0_28A(): pass

    label("Function_0_28A")

    Return()

    # Function_0_28A end

    def Function_1_28B(): pass

    label("Function_1_28B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_29D")
    OP_6F(0x8, 0)
    Jump("loc_2A4")

    label("loc_29D")

    OP_6F(0x8, 60)

    label("loc_2A4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6")
    OP_6F(0x9, 0)
    Jump("loc_2BD")

    label("loc_2B6")

    OP_6F(0x9, 60)

    label("loc_2BD")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2CF")
    OP_6F(0xA, 0)
    Jump("loc_2D6")

    label("loc_2CF")

    OP_6F(0xA, 60)

    label("loc_2D6")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2E8")
    OP_6F(0xB, 0)
    Jump("loc_2EF")

    label("loc_2E8")

    OP_6F(0xB, 60)

    label("loc_2EF")

    Return()

    # Function_1_28B end

    def Function_2_2F0(): pass

    label("Function_2_2F0")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_305")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_2F0")

    label("loc_305")

    Return()

    # Function_2_2F0 end

    def Function_3_306(): pass

    label("Function_3_306")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_499")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3E5")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_358():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_358)

    def lambda_373():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_373)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x447, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_3C0"),
        (2, "loc_3D2"),
        (1, "loc_3E2"),
        (SWITCH_DEFAULT, "loc_3E5"),
    )


    label("loc_3C0")

    OP_A2(0x2314)
    OP_6F(0x8, 60)
    Sleep(500)
    Jump("loc_3E5")

    label("loc_3D2")

    OP_6F(0x8, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_3E2")

    OP_B4(0x0)
    Return()

    label("loc_3E5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17F, 1)"), scpexpr(EXPR_END)), "loc_434")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x7F\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2313)
    Jump("loc_496")

    label("loc_434")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x7F\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x7F\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_496")

    Jump("loc_4C8")

    label("loc_499")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_4C8")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_306 end

    def Function_4_4D6(): pass

    label("Function_4_4D6")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5A6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    AddSepith(0x0, 0x64)
    AddSepith(0x1, 0x64)
    AddSepith(0x2, 0x64)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #4
        (
            "\x07\x00得到了\x07\x02#56I地之耀晶片×１００\x01",
            "\x07\x02#57I水之耀晶片×１００\x01",
            "\x07\x02#58I火之耀晶片×１００\x01",
            "\x07\x02#59I风之耀晶片×１００\x01",
            "\x07\x00。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2315)
    Jump("loc_5C0")

    label("loc_5A6")


    AnonymousTalk(    #5
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_5C0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_4D6 end

    def Function_5_5D2(): pass

    label("Function_5_5D2")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_6AA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0xE0, 1)"), scpexpr(EXPR_END)), "loc_641")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x00得到了\x1F\xE0\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2316)
    Jump("loc_6A7")

    label("loc_641")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "宝箱里装有\x1F\xE0\x00\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xE0\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_6A7")

    Jump("loc_6DB")

    label("loc_6AA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_6DB")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5D2 end

    def Function_6_6E9(): pass

    label("Function_6_6E9")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x462, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C1")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_758")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2317)
    Jump("loc_7BE")

    label("loc_758")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。   \x01",
            "所持物品已经满了，\x1F\xFD\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_7BE")

    Jump("loc_7F2")

    label("loc_7C1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_7F2")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_6E9 end

    SaveToFile()

Try(main)
