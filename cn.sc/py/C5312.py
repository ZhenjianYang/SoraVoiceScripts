from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C5312   ._SN',
        MapName             = 'Other',
        Location            = 'C5312.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60064",
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
        'ED6_DT29/CH12420 ._CH',             # 00
        'ED6_DT29/CH12421 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH12420P._CP',             # 00
        'ED6_DT29/CH12421P._CP',             # 01
    )

    DeclNpc(
        X                   = -80,
        Z                   = 1500,
        Y                   = 27600,
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
        X                   = -27660,
        Z                   = 91500,
        Y                   = -1030,
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


    DeclActor(
        TriggerX            = -40,
        TriggerZ            = 0,
        TriggerY            = 28300,
        TriggerRange        = 1000,
        ActorX              = -80,
        ActorZ              = 0,
        ActorY              = 27600,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -28370,
        TriggerZ            = 90000,
        TriggerY            = -1030,
        TriggerRange        = 1000,
        ActorX              = -27660,
        ActorZ              = 90000,
        ActorY              = -1030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_17B",          # 02, 2
        "Function_3_191",          # 03, 3
        "Function_4_361",          # 04, 4
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    OP_22(0x1C3, 0x1, 0x64)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15A")
    OP_6F(0x0, 0)
    Jump("loc_161")

    label("loc_15A")

    OP_6F(0x0, 60)

    label("loc_161")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_173")
    OP_6F(0x1, 0)
    Jump("loc_17A")

    label("loc_173")

    OP_6F(0x1, 60)

    label("loc_17A")

    Return()

    # Function_1_143 end

    def Function_2_17B(): pass

    label("Function_2_17B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_190")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_17B")

    label("loc_190")

    Return()

    # Function_2_17B end

    def Function_3_191(): pass

    label("Function_3_191")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_324")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1E3():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E3)

    def lambda_1FE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_1FE)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_24B"),
        (2, "loc_25D"),
        (1, "loc_26D"),
        (SWITCH_DEFAULT, "loc_270"),
    )


    label("loc_24B")

    OP_A2(0x2361)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_270")

    label("loc_25D")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_26D")

    OP_B4(0x0)
    Return()

    label("loc_270")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15, 1)"), scpexpr(EXPR_END)), "loc_2BF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "\x07\x00得到了\x1F\x15\x00\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2360)
    Jump("loc_321")

    label("loc_2BF")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "宝箱里装有\x1F\x15\x00\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x15\x00\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_321")

    Jump("loc_353")

    label("loc_324")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_353")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_191 end

    def Function_4_361(): pass

    label("Function_4_361")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4F4")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_440")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_91(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_3B3():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3B3)

    def lambda_3CE():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_3CE)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(    #4
        "\x07\x05魔兽出现了！\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_41B"),
        (2, "loc_42D"),
        (1, "loc_43D"),
        (SWITCH_DEFAULT, "loc_440"),
    )


    label("loc_41B")

    OP_A2(0x2363)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_440")

    label("loc_42D")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_43D")

    OP_B4(0x0)
    Return()

    label("loc_440")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x129, 1)"), scpexpr(EXPR_END)), "loc_48F")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x29\x01\x07\x00。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2362)
    Jump("loc_4F1")

    label("loc_48F")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x29\x01\x07\x00。 \x01",
            "所持物品已经满了，\x1F\x29\x01\x07\x00只能放弃了。\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4F1")

    Jump("loc_523")

    label("loc_4F4")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_523")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_361 end

    SaveToFile()

Try(main)
