from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        "Function_4_392",          # 04, 4
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

    OP_EA(0x2, 0x5, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_32C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_27B")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_1E8():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_1E8)

    def lambda_203():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_203)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #0
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_256"),
        (2, "loc_268"),
        (1, "loc_278"),
        (SWITCH_DEFAULT, "loc_27B"),
    )


    label("loc_256")

    OP_A2(0x2361)
    OP_6F(0x0, 60)
    Sleep(500)
    Jump("loc_27B")

    label("loc_268")

    OP_6F(0x0, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_278")

    OP_B4(0x0)
    Return()

    label("loc_27B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x15, 1)"), scpexpr(EXPR_END)), "loc_2C7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #1
        "Found \x1F\x15\x00\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2360)
    Jump("loc_329")

    label("loc_2C7")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #2
        (
            "Found \x1F\x15\x00\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x15\x00\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_329")

    Jump("loc_384")

    label("loc_32C")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #3
        (
            "\x07\x05What you have taken from this chest, you\x01",
            "can never restore.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_384")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_191 end

    def Function_4_392(): pass

    label("Function_4_392")

    OP_EA(0x2, 0x6, 0x2, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_52D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x46C, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_47C")
    OP_9F(0x9, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x9, 0x0, 0)
    OP_91(0x9, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_3E9():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x9, 1, lambda_3E9)

    def lambda_404():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x9, 2, lambda_404)
    ClearChrFlags(0x9, 0x80)

    AnonymousTalk(    #4
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x532, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x9, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_457"),
        (2, "loc_469"),
        (1, "loc_479"),
        (SWITCH_DEFAULT, "loc_47C"),
    )


    label("loc_457")

    OP_A2(0x2363)
    OP_6F(0x1, 60)
    Sleep(500)
    Jump("loc_47C")

    label("loc_469")

    OP_6F(0x1, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_479")

    OP_B4(0x0)
    Return()

    label("loc_47C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x129, 1)"), scpexpr(EXPR_END)), "loc_4C8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        "Found \x1F\x29\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2362)
    Jump("loc_52A")

    label("loc_4C8")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #6
        (
            "Found \x1F\x29\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x29\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_52A")

    Jump("loc_58E")

    label("loc_52D")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #7
        (
            "\x07\x05This chest was once full of wondrous\x01",
            "treasures. Then you came along.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_58E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_392 end

    SaveToFile()

Try(main)
