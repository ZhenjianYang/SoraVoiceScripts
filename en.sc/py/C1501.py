from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C1501   ._SN',
        MapName             = 'Bose',
        Location            = 'C1501.x',
        MapIndex            = 61,
        MapDefaultBGM       = "ed60022",
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
        'Hapilsag',                             # 9
        'Manoria Coast',                        # 10
        'Krone Pass',                           # 11
        '',                                     # 12
        '',                                     # 13
        '',                                     # 14
        '',                                     # 15
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
        'ED6_DT29/CH12550 ._CH',             # 00
        'ED6_DT29/CH12551 ._CH',             # 01
        'ED6_DT29/CH12440 ._CH',             # 02
        'ED6_DT29/CH12441 ._CH',             # 03
    )

    AddCharChipPat(
        'ED6_DT29/CH12550P._CP',             # 00
        'ED6_DT29/CH12551P._CP',             # 01
        'ED6_DT29/CH12440P._CP',             # 02
        'ED6_DT29/CH12441P._CP',             # 03
    )

    DeclNpc(
        X                   = -96470,
        Z                   = 3990,
        Y                   = 82150,
        Direction           = 188,
        Unknown2            = 2,
        Unknown3            = 131072,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -68830,
        Z                   = 70,
        Y                   = -31470,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = -114600,
        Z                   = 6050,
        Y                   = 118780,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0xFF,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -106080,
        Z                   = 6030,
        Y                   = 93200,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -104200,
        Z                   = 1980,
        Y                   = 7590,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -109430,
        Z                   = 4040,
        Y                   = 46760,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121470,
        Z                   = 2040,
        Y                   = 22550,
        Unknown_0C          = 0,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0xC9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclEvent(
        X                   = -91580,
        Y                   = 3000,
        Z                   = 77390,
        Range               = -102500,
        Unknown_10          = 0x173E,
        Unknown_14          = 0x13D76,
        Unknown_18          = 0x0,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = -106310,
        TriggerZ            = 1990,
        TriggerY            = 2710,
        TriggerRange        = 1000,
        ActorX              = -106430,
        ActorZ              = 1990,
        ActorY              = 2090,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -112480,
        TriggerZ            = 2070,
        TriggerY            = 63130,
        TriggerRange        = 1000,
        ActorX              = -112990,
        ActorZ              = 2070,
        ActorY              = 63430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_202",          # 00, 0
        "Function_1_203",          # 01, 1
        "Function_2_283",          # 02, 2
        "Function_3_299",          # 03, 3
        "Function_4_468",          # 04, 4
        "Function_5_5B1",          # 05, 5
    )


    def Function_0_202(): pass

    label("Function_0_202")

    Return()

    # Function_0_202 end

    def Function_1_203(): pass

    label("Function_1_203")

    OP_16(0x2, 0xFA0, 0xFFFC8560, 0xFFFEA840, 0x23003F)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x243, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_233")
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    Jump("loc_245")

    label("loc_233")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_245")
    ClearChrFlags(0x8, 0x80)
    OP_B2(0x1, 0x0, 0x80)

    label("loc_245")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_257")
    OP_6F(0x0, 0)
    Jump("loc_25E")

    label("loc_257")

    OP_6F(0x0, 60)

    label("loc_25E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_270")
    OP_6F(0x1, 0)
    Jump("loc_277")

    label("loc_270")

    OP_6F(0x1, 60)

    label("loc_277")

    OP_51(0x8, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_203 end

    def Function_2_283(): pass

    label("Function_2_283")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_298")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_283")

    label("loc_298")

    Return()

    # Function_2_283 end

    def Function_3_299(): pass

    label("Function_3_299")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x25F, 3)), scpexpr(EXPR_END)), "loc_2A1")
    Return()

    label("loc_2A1")

    EventBegin(0x1)
    OP_51(0x0, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x2, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x3, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x4, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x5, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x6, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x7, 0xB, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    SetChrSubChip(0x4, 0)
    SetChrSubChip(0x5, 0)
    SetChrSubChip(0x6, 0)
    SetChrSubChip(0x7, 0)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05A large monster is prowling around.\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Exterminate\x01",      # 0
            "Leave Alone\x01",      # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (1, "loc_395"),
        (SWITCH_DEFAULT, "loc_3B8"),
    )


    label("loc_395")

    Fade(500)
    OP_89(0x0, -97890, 3940, 74670, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    OP_0D()
    EventEnd(0x0)
    Return()

    label("loc_3B8")

    Battle(0xEDE, 0x0, 0x0, 0x0, 0xFF)
    EventBegin(0x1)
    OP_89(0x0, -97890, 3940, 74670, 0)
    OP_69(0x0, 0x0)
    OP_30(0x1)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (2, "loc_3F1"),
        (1, "loc_3F4"),
        (SWITCH_DEFAULT, "loc_3F7"),
    )


    label("loc_3F1")

    EventEnd(0x0)
    Return()

    label("loc_3F4")

    OP_B4(0x0)
    Return()

    label("loc_3F7")

    EventBegin(0x1)
    SetChrFlags(0x8, 0x80)
    OP_B2(0x0, 0x0, 0x80)
    OP_0D()
    Sleep(400)
    OP_22(0x17, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        "\x07\x05Exterminated monster!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_A2(0x12FB)
    OP_28(0xA2, 0x4, 0x10)
    OP_28(0xA2, 0x4, 0x2)
    OP_28(0xA2, 0x1, 0x1)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_3_299 end

    def Function_4_468(): pass

    label("Function_4_468")

    OP_EA(0x2, 0x5A, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_540")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_4D9")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #2
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x130D)
    Jump("loc_53D")

    label("loc_4D9")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #3
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_53D")

    Jump("loc_5A3")

    label("loc_540")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        (
            "\x07\x05This chest was once full of wondrous\x01",
            "treasures. Then you came along.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_5A3")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_468 end

    def Function_5_5B1(): pass

    label("Function_5_5B1")

    OP_EA(0x2, 0x5B, 0x0, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x261, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_689")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1AB, 1)"), scpexpr(EXPR_END)), "loc_622")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "Found \x1F\xAB\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x130E)
    Jump("loc_686")

    label("loc_622")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "Found \x1F\xAB\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xAB\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x1, 60)
    OP_70(0x1, 0x0)

    label("loc_686")

    Jump("loc_707")

    label("loc_689")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        (
            "\x07\x05Looking into yet another empty chest, you\x01",
            "wonder who leaves all of these lying around\x01",
            "unlocked.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_707")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_5B1 end

    SaveToFile()

Try(main)
