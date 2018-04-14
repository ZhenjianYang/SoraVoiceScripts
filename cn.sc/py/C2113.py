from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'C2113   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2113.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60033",
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
        'ED6_DT09/CH10560 ._CH',             # 00
        'ED6_DT09/CH10561 ._CH',             # 01
        'ED6_DT09/CH10570 ._CH',             # 02
        'ED6_DT09/CH10571 ._CH',             # 03
        'ED6_DT09/CH10580 ._CH',             # 04
        'ED6_DT09/CH10581 ._CH',             # 05
        'ED6_DT09/CH10590 ._CH',             # 06
        'ED6_DT09/CH10591 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT09/CH10560P._CP',             # 00
        'ED6_DT09/CH10561P._CP',             # 01
        'ED6_DT09/CH10570P._CP',             # 02
        'ED6_DT09/CH10571P._CP',             # 03
        'ED6_DT09/CH10580P._CP',             # 04
        'ED6_DT09/CH10581P._CP',             # 05
        'ED6_DT09/CH10590P._CP',             # 06
        'ED6_DT09/CH10591P._CP',             # 07
    )

    DeclNpc(
        X                   = 0,
        Z                   = 1000,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -3760,
        Z                   = 0,
        Y                   = 100,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 4948,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 3670,
        Z                   = 0,
        Y                   = -10,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 4949,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -90,
        Z                   = 0,
        Y                   = -11260,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x1BB,
        Unknown_18          = 4950,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -30,
        TriggerZ            = 0,
        TriggerY            = -700,
        TriggerRange        = 1000,
        ActorX              = -50,
        ActorZ              = 0,
        ActorY              = 60,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_182",          # 00, 0
        "Function_1_183",          # 01, 1
        "Function_2_1C1",          # 02, 2
        "Function_3_1D7",          # 03, 3
    )


    def Function_0_182(): pass

    label("Function_0_182")

    Return()

    # Function_0_182 end

    def Function_1_183(): pass

    label("Function_1_183")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_195")
    OP_6F(0x0, 0)
    Jump("loc_19C")

    label("loc_195")

    OP_6F(0x0, 60)

    label("loc_19C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 4)), scpexpr(EXPR_END)), "loc_1A8")
    SetChrFlags(0x9, 0x80)

    label("loc_1A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 5)), scpexpr(EXPR_END)), "loc_1B4")
    SetChrFlags(0xA, 0x80)

    label("loc_1B4")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x26A, 6)), scpexpr(EXPR_END)), "loc_1C0")
    SetChrFlags(0xB, 0x80)

    label("loc_1C0")

    Return()

    # Function_1_183 end

    def Function_2_1C1(): pass

    label("Function_2_1C1")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1D6")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_1C1")

    label("loc_1D6")

    Return()

    # Function_2_1C1 end

    def Function_3_1D7(): pass

    label("Function_3_1D7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_36A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x262, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2B6")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_229():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_229)

    def lambda_244():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_244)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x1BC, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_291"),
        (2, "loc_2A3"),
        (1, "loc_2B3"),
        (SWITCH_DEFAULT, "loc_2B6"),
    )


    label("loc_291")

    OP_A2(0x1313)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_2B6")

    label("loc_2A3")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_2B3")

    OP_B4(0x0)
    Return()

    label("loc_2B6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x142, 1)"), scpexpr(EXPR_END)), "loc_305")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x42\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1312)
    Jump("loc_367")

    label("loc_305")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x42\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x42\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_367")

    Jump("loc_399")

    label("loc_36A")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_399")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_1D7 end

    SaveToFile()

Try(main)
