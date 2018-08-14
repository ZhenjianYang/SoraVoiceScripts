from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M3200   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60232",
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
        'ED6_DT07/CH00320 ._CH',             # 00
        'ED6_DT07/CH00321 ._CH',             # 01
        'ED6_DT09/CH11210 ._CH',             # 02
        'ED6_DT09/CH11211 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT07/CH00320P._CP',             # 00
        'ED6_DT07/CH00321P._CP',             # 01
        'ED6_DT09/CH11210P._CP',             # 02
        'ED6_DT09/CH11211P._CP',             # 03
    )

    DeclNpc(
        X                   = 3320,
        Z                   = 1000,
        Y                   = 42150,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = 82850,
        Z                   = 0,
        Y                   = 44690,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -53160,
        Z                   = 0,
        Y                   = 65780,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 3320,
        TriggerZ            = 0,
        TriggerY            = 42150,
        TriggerRange        = 1000,
        ActorX              = 3320,
        ActorZ              = 1000,
        ActorY              = 42150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 84710,
        TriggerZ            = 0,
        TriggerY            = 9160,
        TriggerRange        = 1000,
        ActorX              = 84710,
        ActorZ              = 1000,
        ActorY              = 9160,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -54000,
        TriggerZ            = 0,
        TriggerY            = 68710,
        TriggerRange        = 1000,
        ActorX              = -54000,
        ActorZ              = 1000,
        ActorY              = 68710,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_18E",          # 00, 0
        "Function_1_18F",          # 01, 1
        "Function_2_1DB",          # 02, 2
        "Function_3_358",          # 03, 3
        "Function_4_533",          # 04, 4
        "Function_5_653",          # 05, 5
    )


    def Function_0_18E(): pass

    label("Function_0_18E")

    Return()

    # Function_0_18E end

    def Function_1_18F(): pass

    label("Function_1_18F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A1")
    OP_6F(0x6, 0)
    Jump("loc_1A8")

    label("loc_1A1")

    OP_6F(0x6, 60)

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BA")
    OP_6F(0x17, 0)
    Jump("loc_1C1")

    label("loc_1BA")

    OP_6F(0x17, 60)

    label("loc_1C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D3")
    OP_6F(0x18, 0)
    Jump("loc_1DA")

    label("loc_1D3")

    OP_6F(0x18, 60)

    label("loc_1DA")

    Return()

    # Function_1_18F end

    def Function_2_1DB(): pass

    label("Function_2_1DB")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_200")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_342")

    label("loc_200")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_219")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_342")

    label("loc_219")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_232")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_342")

    label("loc_232")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24B")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_342")

    label("loc_24B")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_264")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_342")

    label("loc_264")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27D")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_342")

    label("loc_27D")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_342")

    label("loc_296")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AF")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_342")

    label("loc_2AF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C8")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_342")

    label("loc_2C8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E1")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_342")

    label("loc_2E1")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2FA")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_342")

    label("loc_2FA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_313")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_342")

    label("loc_313")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_32C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_342")

    label("loc_32C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_342")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_342")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_357")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_342")

    label("loc_357")

    Return()

    # Function_2_1DB end

    def Function_3_358(): pass

    label("Function_3_358")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_437")
    OP_9F(0x10, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x10, 0x0, 0)
    OP_91(0x10, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_3AA():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AA)

    def lambda_3C5():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C5)
    ClearChrFlags(0x10, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x2B2, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x10, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_412"),
        (2, "loc_424"),
        (1, "loc_434"),
        (SWITCH_DEFAULT, "loc_437"),
    )


    label("loc_412")

    OP_A2(0x2B80)
    OP_6F(0x6, 60)
    Sleep(500)
    Jump("loc_437")

    label("loc_424")

    OP_6F(0x6, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_434")

    OP_B4(0x0)
    Return()

    label("loc_437")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x333, 1)"), scpexpr(EXPR_END)), "loc_489")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x33\x03\x07\x00。\x02",
    )

    Jump("loc_46E")

    label("loc_46E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B80)
    Jump("loc_4F3")

    label("loc_489")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x33\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x33\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_4D4")

    label("loc_4D4")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_4F3")

    Jump("loc_525")

    label("loc_4F6")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_525")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_358 end

    def Function_4_533(): pass

    label("Function_4_533")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_614")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x17, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_5A5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_58A")

    label("loc_58A")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B96)
    Jump("loc_611")

    label("loc_5A5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_5F2")

    label("loc_5F2")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x17, 60)
    OP_70(0x17, 0x0)

    label("loc_611")

    Jump("loc_645")

    label("loc_614")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_645")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_533 end

    def Function_5_653(): pass

    label("Function_5_653")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x572, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_734")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x18, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x3EE, 1)"), scpexpr(EXPR_END)), "loc_6C5")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x00得到了\x1F\xEE\x03\x07\x00。\x02",
    )

    Jump("loc_6AA")

    label("loc_6AA")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2B97)
    Jump("loc_731")

    label("loc_6C5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "宝箱里装有\x1F\xEE\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xEE\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_712")

    label("loc_712")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x18, 60)
    OP_70(0x18, 0x0)

    label("loc_731")

    Jump("loc_765")

    label("loc_734")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_765")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_653 end

    SaveToFile()

Try(main)
