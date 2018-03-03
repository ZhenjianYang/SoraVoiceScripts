from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'U4252   ._SN',
        MapName             = 'Gaiden2',
        Location            = 'U4252.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60230",
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
        'ED6_DT29/CH14510 ._CH',             # 00
        'ED6_DT29/CH14511 ._CH',             # 01
        'ED6_DT29/CH14790 ._CH',             # 02
        'ED6_DT29/CH14790 ._CH',             # 03
        'ED6_DT29/CH14450 ._CH',             # 04
        'ED6_DT29/CH14451 ._CH',             # 05
    )

    AddCharChipPat(
        'ED6_DT29/CH14510P._CP',             # 00
        'ED6_DT29/CH14511P._CP',             # 01
        'ED6_DT29/CH14790P._CP',             # 02
        'ED6_DT29/CH14790P._CP',             # 03
        'ED6_DT29/CH14450P._CP',             # 04
        'ED6_DT29/CH14451P._CP',             # 05
    )

    DeclMonster(
        X                   = -72820,
        Z                   = 0,
        Y                   = -39360,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xE7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -67880,
        TriggerZ            = 0,
        TriggerY            = -29030,
        TriggerRange        = 1000,
        ActorX              = -67880,
        ActorZ              = 1000,
        ActorY              = -29030,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_11A",          # 00, 0
        "Function_1_11B",          # 01, 1
        "Function_2_135",          # 02, 2
    )


    def Function_0_11A(): pass

    label("Function_0_11A")

    Return()

    # Function_0_11A end

    def Function_1_11B(): pass

    label("Function_1_11B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_12D")
    OP_6F(0x4, 0)
    Jump("loc_134")

    label("loc_12D")

    OP_6F(0x4, 60)

    label("loc_134")

    Return()

    # Function_1_11B end

    def Function_2_135(): pass

    label("Function_2_135")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4F4, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_20E")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F6, 1)"), scpexpr(EXPR_END)), "loc_1A3")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xF6\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x27A0)
    Jump("loc_20B")

    label("loc_1A3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xF6\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF6\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_20B")

    Jump("loc_284")

    label("loc_20E")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05How many chests could a chest checker check if a chest checker could\x01",
            "check chests?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x128, 0x0)

    label("loc_284")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_135 end

    SaveToFile()

Try(main)
