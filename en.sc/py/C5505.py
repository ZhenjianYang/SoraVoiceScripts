from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5505   ._SN',
        MapName             = 'Other',
        Location            = 'C5505.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60021",
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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT29/CH12180 ._CH',             # 00
        'ED6_DT29/CH12181 ._CH',             # 01
        'ED6_DT29/CH12230 ._CH',             # 02
        'ED6_DT29/CH12231 ._CH',             # 03
        'ED6_DT29/CH12270 ._CH',             # 04
        'ED6_DT29/CH12271 ._CH',             # 05
        'ED6_DT29/CH12360 ._CH',             # 06
        'ED6_DT29/CH12361 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12180P._CP',             # 00
        'ED6_DT29/CH12181P._CP',             # 01
        'ED6_DT29/CH12230P._CP',             # 02
        'ED6_DT29/CH12231P._CP',             # 03
        'ED6_DT29/CH12270P._CP',             # 04
        'ED6_DT29/CH12271P._CP',             # 05
        'ED6_DT29/CH12360P._CP',             # 06
        'ED6_DT29/CH12361P._CP',             # 07
    )

    DeclNpc(
        X                   = -26690,
        Z                   = 1000,
        Y                   = 13420,
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
        X                   = -26150,
        Z                   = 0,
        Y                   = -18160,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -9050,
        Z                   = 0,
        Y                   = -1650,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 350,
        Z                   = 0,
        Y                   = -14310,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 37130,
        Z                   = 0,
        Y                   = -6030,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 16500,
        Z                   = 0,
        Y                   = 22960,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x389,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -24260,
        Z                   = 0,
        Y                   = 2230,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32920,
        Z                   = 0,
        Y                   = 21400,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x38C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 40970,
        TriggerZ            = 0,
        TriggerY            = -12100,
        TriggerRange        = 1000,
        ActorX              = 41400,
        ActorZ              = 0,
        ActorY              = -12530,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26690,
        TriggerZ            = 0,
        TriggerY            = 14080,
        TriggerRange        = 1000,
        ActorX              = -26690,
        ActorZ              = 0,
        ActorY              = 13420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_216",          # 00, 0
        "Function_1_217",          # 01, 1
        "Function_2_254",          # 02, 2
        "Function_3_26A",          # 03, 3
        "Function_4_3D7",          # 04, 4
        "Function_5_569",          # 05, 5
    )


    def Function_0_216(): pass

    label("Function_0_216")

    Return()

    # Function_0_216 end

    def Function_1_217(): pass

    label("Function_1_217")

    OP_22(0x1CD, 0x0, 0x64)
    OP_22(0x1CE, 0x1, 0x50)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_233")
    OP_6F(0x0, 0)
    Jump("loc_23A")

    label("loc_233")

    OP_6F(0x0, 60)

    label("loc_23A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_24C")
    OP_6F(0x1, 0)
    Jump("loc_253")

    label("loc_24C")

    OP_6F(0x1, 60)

    label("loc_253")

    Return()

    # Function_1_217 end

    def Function_2_254(): pass

    label("Function_2_254")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_269")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_254")

    label("loc_269")

    Return()

    # Function_2_254 end

    def Function_3_26A(): pass

    label("Function_3_26A")

    OP_EA(0x2, 0x8F, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_342")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x125, 1)"), scpexpr(EXPR_END)), "loc_2DB")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\x25\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1121)
    Jump("loc_33F")

    label("loc_2DB")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\x25\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x25\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_33F")

    Jump("loc_3C5")

    label("loc_342")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05Psychically sensing that there's nothing inside,\x01",
            "you walk away from the chest without disturbing\x01",
            "it.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_3C5")

    Sleep(30)
    Call(0, 5)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_26A end

    def Function_4_3D7(): pass

    label("Function_4_3D7")

    OP_EA(0x2, 0x90, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x224, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4AF")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x104, 1)"), scpexpr(EXPR_END)), "loc_448")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #3
        "Found \x1F\x04\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1122)
    Jump("loc_4AC")

    label("loc_448")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "Found \x1F\x04\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x04\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_4AC")

    Jump("loc_557")

    label("loc_4AF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #5
        (
            "\x07\x05Why did you have to come back? You could've\x01",
            "just walked away with the goods, but now the\x01",
            "treasure chest has you right where it wants you!\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_557")

    Sleep(30)
    Call(0, 5)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_3D7 end

    def Function_5_569(): pass

    label("Function_5_569")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x201, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_671")

    ChrTalk(    #6
        0x101,
        (
            "#1004FHey!\x02\x03",

            "Do you think this could be\x01",
            "our equipment?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10A,
        (
            "#811FSure looks like it! ♪\x02\x03",

            "#1310FThe rest of our stuff might be\x01",
            "hidden around like this.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0x101,
        (
            "#1006FCool. I'd kinda like to avoid fighting\x01",
            "the monsters, but we do need to find\x01",
            "our stuff.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x100F)

    label("loc_671")

    Return()

    # Function_5_569 end

    SaveToFile()

Try(main)
