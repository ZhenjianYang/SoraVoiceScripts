from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 柏斯

    CreateScenaFile(
        FileName            = 'C1211   ._SN',
        MapName             = 'Bose',
        Location            = 'C1211.x',
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
        'ED6_DT09/CH10410 ._CH',             # 00
        'ED6_DT09/CH10411 ._CH',             # 01
        'ED6_DT09/CH10420 ._CH',             # 02
        'ED6_DT09/CH10421 ._CH',             # 03
        'ED6_DT09/CH10430 ._CH',             # 04
        'ED6_DT09/CH10431 ._CH',             # 05
        'ED6_DT09/CH10440 ._CH',             # 06
        'ED6_DT09/CH10441 ._CH',             # 07
        'ED6_DT29/CH12140 ._CH',             # 08
        'ED6_DT29/CH12141 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10410P._CP',             # 00
        'ED6_DT09/CH10411P._CP',             # 01
        'ED6_DT09/CH10420P._CP',             # 02
        'ED6_DT09/CH10421P._CP',             # 03
        'ED6_DT09/CH10430P._CP',             # 04
        'ED6_DT09/CH10431P._CP',             # 05
        'ED6_DT09/CH10440P._CP',             # 06
        'ED6_DT09/CH10441P._CP',             # 07
        'ED6_DT29/CH12140P._CP',             # 08
        'ED6_DT29/CH12141P._CP',             # 09
    )

    DeclActor(
        TriggerX            = -4400,
        TriggerZ            = 0,
        TriggerY            = 22310,
        TriggerRange        = 1000,
        ActorX              = -4490,
        ActorZ              = 0,
        ActorY              = 22920,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4430,
        TriggerZ            = 0,
        TriggerY            = 22300,
        TriggerRange        = 1000,
        ActorX              = 4430,
        ActorZ              = 0,
        ActorY              = 22960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_142",          # 00, 0
        "Function_1_143",          # 01, 1
        "Function_2_176",          # 02, 2
        "Function_3_2F1",          # 03, 3
    )


    def Function_0_142(): pass

    label("Function_0_142")

    Return()

    # Function_0_142 end

    def Function_1_143(): pass

    label("Function_1_143")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_155")
    OP_6F(0x0, 0)
    Jump("loc_15C")

    label("loc_155")

    OP_6F(0x0, 60)

    label("loc_15C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16E")
    OP_6F(0x1, 0)
    Jump("loc_175")

    label("loc_16E")

    OP_6F(0x1, 60)

    label("loc_175")

    Return()

    # Function_1_143 end

    def Function_2_176(): pass

    label("Function_2_176")

    OP_EA(0x2, 0x31, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_1E7")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B50)
    Jump("loc_24B")

    label("loc_1E7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_24B")

    Jump("loc_2E3")

    label("loc_24E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Did you hear about the girl who paid for\x01",
            "everything with black sepith crystals? She said it\x01",
            "was only costing her time!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_2E3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_176 end

    def Function_3_2F1(): pass

    label("Function_3_2F1")

    OP_EA(0x2, 0x32, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x36A, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3C9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x27D, 1)"), scpexpr(EXPR_END)), "loc_362")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x7D\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1B51)
    Jump("loc_3C6")

    label("loc_362")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x7D\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x7D\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_3C6")

    Jump("loc_479")

    label("loc_3C9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05The truth is, there's only one treasure chest in\x01",
            "this entire world. It just follows you around, filling\x01",
            "itself with new goods for you to plunder.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_479")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_2F1 end

    SaveToFile()

Try(main)
