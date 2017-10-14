from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5502   ._SN',
        MapName             = 'Other',
        Location            = 'C5502.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60031",
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
        '',                                     # 17
        '',                                     # 18
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
        'ED6_DT29/CH12190 ._CH',             # 00
        'ED6_DT29/CH12191 ._CH',             # 01
        'ED6_DT29/CH12200 ._CH',             # 02
        'ED6_DT29/CH12201 ._CH',             # 03
        'ED6_DT29/CH12210 ._CH',             # 04
        'ED6_DT29/CH12211 ._CH',             # 05
        'ED6_DT29/CH12220 ._CH',             # 06
        'ED6_DT29/CH12221 ._CH',             # 07
    )

    AddCharChipPat(
        'ED6_DT29/CH12190P._CP',             # 00
        'ED6_DT29/CH12191P._CP',             # 01
        'ED6_DT29/CH12200P._CP',             # 02
        'ED6_DT29/CH12201P._CP',             # 03
        'ED6_DT29/CH12210P._CP',             # 04
        'ED6_DT29/CH12211P._CP',             # 05
        'ED6_DT29/CH12220P._CP',             # 06
        'ED6_DT29/CH12221P._CP',             # 07
    )

    DeclNpc(
        X                   = -47360,
        Z                   = -1000,
        Y                   = 191570,
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
        X                   = 12820,
        Z                   = 0,
        Y                   = 136490,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27240,
        Z                   = 0,
        Y                   = 139530,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -42600,
        Z                   = 0,
        Y                   = 150280,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -39260,
        Z                   = 0,
        Y                   = 169730,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -28360,
        Z                   = 0,
        Y                   = 190270,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 14670,
        Z                   = 0,
        Y                   = 176940,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x388,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32659,
        Z                   = -2000,
        Y                   = 160510,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18800,
        Z                   = -2000,
        Y                   = 167080,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -43100,
        Z                   = -2000,
        Y                   = 155530,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x387,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -1160,
        TriggerZ            = 0,
        TriggerY            = 144370,
        TriggerRange        = 1700,
        ActorX              = -1160,
        ActorZ              = 2500,
        ActorY              = 144370,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -13210,
        TriggerZ            = 0,
        TriggerY            = 169110,
        TriggerRange        = 1700,
        ActorX              = -13210,
        ActorZ              = 2500,
        ActorY              = 169110,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 4340,
        TriggerZ            = 0,
        TriggerY            = 181980,
        TriggerRange        = 1700,
        ActorX              = 4340,
        ActorZ              = 2500,
        ActorY              = 181980,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -30880,
        TriggerZ            = 0,
        TriggerY            = 150510,
        TriggerRange        = 1700,
        ActorX              = -30880,
        ActorZ              = 2500,
        ActorY              = 150510,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -38950,
        TriggerZ            = 0,
        TriggerY            = 173800,
        TriggerRange        = 1000,
        ActorX              = -38990,
        ActorZ              = 0,
        ActorY              = 174460,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -42500,
        TriggerZ            = 0,
        TriggerY            = 173790,
        TriggerRange        = 1000,
        ActorX              = -42500,
        ActorZ              = 0,
        ActorY              = 174410,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -35450,
        TriggerZ            = 0,
        TriggerY            = 173790,
        TriggerRange        = 1000,
        ActorX              = -35450,
        ActorZ              = 0,
        ActorY              = 174450,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36970,
        TriggerZ            = 0,
        TriggerY            = 187560,
        TriggerRange        = 1000,
        ActorX              = -36880,
        ActorZ              = 0,
        ActorY              = 186860,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11070,
        TriggerZ            = 0,
        TriggerY            = 155530,
        TriggerRange        = 1000,
        ActorX              = 11070,
        ActorZ              = 0,
        ActorY              = 154910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -7710,
        TriggerZ            = 0,
        TriggerY            = 158960,
        TriggerRange        = 1000,
        ActorX              = -7050,
        ActorZ              = 0,
        ActorY              = 158960,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -47400,
        TriggerZ            = -2000,
        TriggerY            = 190910,
        TriggerRange        = 1000,
        ActorX              = -47360,
        ActorZ              = -2000,
        ActorY              = 191570,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_392",          # 00, 0
        "Function_1_393",          # 01, 1
        "Function_2_537",          # 02, 2
        "Function_3_54D",          # 03, 3
        "Function_4_728",          # 04, 4
        "Function_5_86F",          # 05, 5
        "Function_6_9CB",          # 06, 6
        "Function_7_B18",          # 07, 7
        "Function_8_C55",          # 08, 8
        "Function_9_D98",          # 09, 9
        "Function_10_FEF",         # 0A, 10
        "Function_11_1214",        # 0B, 11
        "Function_12_1439",        # 0C, 12
        "Function_13_166D",        # 0D, 13
    )


    def Function_0_392(): pass

    label("Function_0_392")

    Return()

    # Function_0_392 end

    def Function_1_393(): pass

    label("Function_1_393")

    OP_22(0x1C7, 0x0, 0x64)
    OP_72(0x0, 0x28)
    OP_72(0x1, 0x28)
    OP_72(0x2, 0x28)
    OP_72(0x3, 0x28)
    OP_72(0x4, 0x28)
    OP_72(0x5, 0x28)
    OP_72(0x6, 0x28)
    OP_72(0x7, 0x28)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_END)), "loc_3D5")
    OP_6F(0x1, 120)
    OP_6F(0x6, 60)

    label("loc_3D5")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_END)), "loc_3EA")
    OP_6F(0x1, 120)
    OP_6F(0x6, 160)

    label("loc_3EA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_END)), "loc_3FF")
    OP_6F(0x3, 120)
    OP_6F(0x2, 60)

    label("loc_3FF")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_END)), "loc_414")
    OP_6F(0x3, 120)
    OP_6F(0x2, 160)

    label("loc_414")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_END)), "loc_429")
    OP_6F(0x4, 120)
    OP_6F(0x5, 60)

    label("loc_429")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_END)), "loc_43E")
    OP_6F(0x4, 120)
    OP_6F(0x5, 160)

    label("loc_43E")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 5)), scpexpr(EXPR_END)), "loc_453")
    OP_6F(0x7, 60)
    OP_6F(0x0, 260)

    label("loc_453")

    OP_4F(0x2A, (scpexpr(EXPR_PUSH_LONG, 0x6D6), scpexpr(EXPR_NEG), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_46F")
    OP_6F(0x8, 0)
    Jump("loc_476")

    label("loc_46F")

    OP_6F(0x8, 60)

    label("loc_476")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_488")
    OP_6F(0x9, 0)
    Jump("loc_48F")

    label("loc_488")

    OP_6F(0x9, 60)

    label("loc_48F")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4A1")
    OP_6F(0xA, 0)
    Jump("loc_4A8")

    label("loc_4A1")

    OP_6F(0xA, 60)

    label("loc_4A8")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4BA")
    OP_6F(0xB, 0)
    Jump("loc_4C1")

    label("loc_4BA")

    OP_6F(0xB, 60)

    label("loc_4C1")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4D3")
    OP_6F(0xC, 0)
    Jump("loc_4DA")

    label("loc_4D3")

    OP_6F(0xC, 60)

    label("loc_4DA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_4EC")
    OP_6F(0xD, 0)
    Jump("loc_4F3")

    label("loc_4EC")

    OP_6F(0xD, 60)

    label("loc_4F3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_505")
    OP_6F(0xE, 0)
    Jump("loc_50C")

    label("loc_505")

    OP_6F(0xE, 60)

    label("loc_50C")

    OP_E0(0x8, 0xDA, 0x67, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0xD2, 0xA8, 0x2, 0x0)
    OP_E0(0x9, 0x64, 0x5B, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0xD2, 0xA8, 0x2, 0x0)
    OP_E0(0xA, 0xF6, 0x73, 0xFF, 0xFF, 0x0, 0x0, 0x0, 0x0, 0xD2, 0xA8, 0x2, 0x0)
    Return()

    # Function_1_393 end

    def Function_2_537(): pass

    label("Function_2_537")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_54C")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_537")

    label("loc_54C")

    Return()

    # Function_2_537 end

    def Function_3_54D(): pass

    label("Function_3_54D")

    OP_EA(0x2, 0x87, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_625")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1E0, 1)"), scpexpr(EXPR_END)), "loc_5BE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "Found \x1F\xE0\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1110)
    Jump("loc_622")

    label("loc_5BE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "Found \x1F\xE0\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xE0\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_622")

    Jump("loc_699")

    label("loc_625")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        (
            "\x07\x05The empty chest opens with a groan. I guess it's\x01",
            "tired of being opened over and over.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_699")

    Sleep(30)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71F")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x14)"), scpexpr(EXPR_END)), "loc_6B8")
    Jump("loc_71F")

    label("loc_6B8")


    AnonymousTalk(    #3
        (
            "\x07\x00Found a scrap of paper with a [ #480i ]\x01",
            "recipe written on it.\x02",
        )
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #4
        "\x07\x00Learned [ #480i ] recipe.\x02",
    )

    CloseMessageWindow()

    label("loc_71F")

    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_54D end

    def Function_4_728(): pass

    label("Function_4_728")

    OP_EA(0x2, 0x88, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_81F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    AddSepith(0x0, 0xA)
    AddSepith(0x1, 0xA)
    AddSepith(0x2, 0xA)
    AddSepith(0x3, 0xA)
    AddSepith(0x4, 0xA)
    AddSepith(0x5, 0xA)
    AddSepith(0x6, 0xA)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "Found\x01",
            "#2C#56IEarth Sepith\x01",
            "#57IWater Sepith\x01",
            "#58IFire Sepith\x01",
            "#59IWind Sepith\x01",
            "#62ITime Sepith\x01",
            "#60ISpace Sepith\x01",
            "#61IMirage Sepith x 10#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1111)
    Jump("loc_85D")

    label("loc_81F")


    AnonymousTalk(    #6
        (
            "\x07\x05Can I help you?\x01",
            "Oh, wait. YOU ALREADY HELPED YOURSELF.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_85D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_728 end

    def Function_5_86F(): pass

    label("Function_5_86F")

    OP_EA(0x2, 0x89, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_947")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FC, 1)"), scpexpr(EXPR_END)), "loc_8E0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #7
        "Found \x1F\xFC\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1112)
    Jump("loc_944")

    label("loc_8E0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #8
        (
            "Found \x1F\xFC\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFC\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xA, 60)
    OP_70(0xA, 0x0)

    label("loc_944")

    Jump("loc_9BD")

    label("loc_947")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05You open the chest, realize you already looted it,\x01",
            "then angrily slam the lid back down.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_9BD")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_86F end

    def Function_6_9CB(): pass

    label("Function_6_9CB")

    OP_EA(0x2, 0x8A, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_AA3")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FE, 1)"), scpexpr(EXPR_END)), "loc_A3C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #10
        "Found \x1F\xFE\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1113)
    Jump("loc_AA0")

    label("loc_A3C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #11
        (
            "Found \x1F\xFE\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xFE\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_AA0")

    Jump("loc_B0A")

    label("loc_AA3")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05TREASURE CHEST ADVERTISING FOR THE LOW,\x01",
            "LOW PRICE OF 900 MIRA PER MONTH.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_B0A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_9CB end

    def Function_7_B18(): pass

    label("Function_7_B18")

    OP_EA(0x2, 0x8B, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_BF0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x25E, 1)"), scpexpr(EXPR_END)), "loc_B89")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #13
        "Found \x1F\x5E\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1114)
    Jump("loc_BED")

    label("loc_B89")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #14
        (
            "Found \x1F\x5E\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x5E\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xC, 60)
    OP_70(0xC, 0x0)

    label("loc_BED")

    Jump("loc_C47")

    label("loc_BF0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Dang, you REALLY like reading these messages,\x01",
            "don't you?\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_C47")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_B18 end

    def Function_8_C55(): pass

    label("Function_8_C55")

    OP_EA(0x2, 0x8C, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_D2D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x12D, 1)"), scpexpr(EXPR_END)), "loc_CC6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #16
        "Found \x1F\x2D\x01\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1115)
    Jump("loc_D2A")

    label("loc_CC6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #17
        (
            "Found \x1F\x2D\x01\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\x2D\x01\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_D2A")

    Jump("loc_D8A")

    label("loc_D2D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05You're... You're opening me again? Heeheehee...\x01",
            "How naughty...\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_D8A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_C55 end

    def Function_9_D98(): pass

    label("Function_9_D98")

    OP_EA(0x2, 0x8D, 0x1, 0x0)
    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_F33")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x222, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E82")
    OP_9F(0x8, 0xFF, 0xFF, 0xFF, 0x0, 0x0)
    TurnDirection(0x8, 0x0, 0)
    OP_91(0x8, 0x0, 0x3E8, 0x0, 0x0, 0x0)

    def lambda_DEF():
        OP_91(0xFE, 0x0, 0xFFFFFC18, 0x0, 0x258, 0x0)
        ExitThread()

    QueueWorkItem(0x8, 1, lambda_DEF)

    def lambda_E0A():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x258)
        ExitThread()

    QueueWorkItem(0x8, 2, lambda_E0A)
    ClearChrFlags(0x8, 0x80)

    AnonymousTalk(    #19
        "\x07\x05Monsters appeared!\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    Battle(0x391, 0x0, 0x0, 0x0, 0xFF)
    SetChrFlags(0x8, 0x80)
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0x3), scpexpr(EXPR_END)),
        (0, "loc_E5D"),
        (2, "loc_E6F"),
        (1, "loc_E7F"),
        (SWITCH_DEFAULT, "loc_E82"),
    )


    label("loc_E5D")

    OP_A2(0x1117)
    OP_6F(0xE, 60)
    Sleep(500)
    Jump("loc_E82")

    label("loc_E6F")

    OP_6F(0xE, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    label("loc_E7F")

    OP_B4(0x0)
    Return()

    label("loc_E82")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2C6, 1)"), scpexpr(EXPR_END)), "loc_ECE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #20
        "Found \x1F\xC6\x02\x07\x00.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x1116)
    Jump("loc_F30")

    label("loc_ECE")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #21
        (
            "Found \x1F\xC6\x02\x07\x00 in chest.\x01",
            "Inventory full so gave up \x1F\xC6\x02\x07\x00.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_F30")

    Jump("loc_FE1")

    label("loc_F33")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #22
        (
            "\x07\x05You open the chest and see riches beyond your\x01",
            "wildest imagination. As you take your first step\x01",
            "in your victory dance, you awaken. It was a dream.\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_FE1")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_D98 end

    def Function_10_FEF(): pass

    label("Function_10_FEF")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #23
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1145")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Flip Right\x01",      # 0
            "Flip Left\x01",       # 1
            "Stop\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_10D8")
    OP_6F(0x6, 0)
    OP_70(0x6, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x10A8)
    Sleep(500)
    OP_6D(3880, 0, 135860, 1400)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_113B")

    label("loc_10D8")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_113B")
    OP_6F(0x6, 100)
    OP_70(0x6, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A2(0x10A7)
    Sleep(500)
    OP_6D(3880, 0, 135860, 1400)
    OP_6F(0x1, 0)
    OP_70(0x1, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_113B")

    OP_69(0x0, 0x258)
    Jump("loc_120B")

    label("loc_1145")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1204")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 0)), scpexpr(EXPR_END)), "loc_11A7")
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A3(0x10A8)
    Jump("loc_11C7")

    label("loc_11A7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x214, 7)), scpexpr(EXPR_END)), "loc_11C7")
    OP_6F(0x6, 160)
    OP_70(0x6, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x6)
    OP_A3(0x10A7)

    label("loc_11C7")

    Sleep(500)
    OP_6D(3880, 0, 135860, 1200)
    OP_6F(0x1, 120)
    OP_70(0x1, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x1)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_1204")

    OP_69(0x0, 0x258)

    label("loc_120B")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_10_FEF end

    def Function_11_1214(): pass

    label("Function_11_1214")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_136A")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Flip Right\x01",      # 0
            "Flip Left\x01",       # 1
            "Stop\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_12FD")
    OP_6F(0x2, 0)
    OP_70(0x2, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10AA)
    Sleep(500)
    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_1360")

    label("loc_12FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1360")
    OP_6F(0x2, 100)
    OP_70(0x2, 0xA0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A2(0x10A9)
    Sleep(500)
    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x3, 0)
    OP_70(0x3, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_1360")

    OP_69(0x0, 0x258)
    Jump("loc_1430")

    label("loc_136A")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1429")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 2)), scpexpr(EXPR_END)), "loc_13CC")
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10AA)
    Jump("loc_13EC")

    label("loc_13CC")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 1)), scpexpr(EXPR_END)), "loc_13EC")
    OP_6F(0x2, 160)
    OP_70(0x2, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x2)
    OP_A3(0x10A9)

    label("loc_13EC")

    Sleep(500)
    OP_6D(-12270, 0, 174500, 1200)
    OP_6F(0x3, 120)
    OP_70(0x3, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x3)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_1429")

    OP_69(0x0, 0x258)

    label("loc_1430")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_11_1214 end

    def Function_12_1439(): pass

    label("Function_12_1439")

    TalkBegin(0xFF)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #25
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_1599")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Flip Right\x01",      # 0
            "Flip Left\x01",       # 1
            "Stop\x01",            # 2
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1527")
    OP_6F(0x5, 0)
    OP_70(0x5, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A2(0x10AC)
    Sleep(500)
    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)
    Jump("loc_158F")

    label("loc_1527")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_158F")
    OP_6F(0x5, 100)
    OP_22(0xFA, 0x0, 0x64)
    OP_70(0x5, 0xA0)
    OP_73(0x5)
    OP_A2(0x10AB)
    Sleep(500)
    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)
    OP_6F(0x4, 0)
    OP_70(0x4, 0x78)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_158F")

    OP_69(0x0, 0x258)
    Jump("loc_1664")

    label("loc_1599")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_165D")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 4)), scpexpr(EXPR_END)), "loc_15FB")
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x10AC)
    Jump("loc_161B")

    label("loc_15FB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 3)), scpexpr(EXPR_END)), "loc_161B")
    OP_6F(0x5, 160)
    OP_70(0x5, 0x64)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x5)
    OP_A3(0x10AB)

    label("loc_161B")

    Sleep(500)
    OP_6D(-8090, -60, 183030, 1200)
    Sleep(300)
    OP_6F(0x4, 120)
    OP_70(0x4, 0x0)
    OP_22(0xFB, 0x0, 0x64)
    OP_73(0x4)
    Sleep(1000)
    Fade(500)
    OP_69(0x0, 0x0)

    label("loc_165D")

    OP_69(0x0, 0x258)

    label("loc_1664")

    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_12_1439 end

    def Function_13_166D(): pass

    label("Function_13_166D")

    SetMapFlags(0x80)
    ClearMapFlags(0x1)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #26
        "\x07\x05There's a lever here that can be moved.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x215, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_172C")

    Menu(
        0,
        260,
        200,
        1,
        (
            "Drop Lever\x01",      # 0
            "Stop\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1729")
    EventBegin(0x0)
    OP_6F(0x7, 0)
    OP_70(0x7, 0x3C)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x7)
    OP_6F(0x0, 0)
    OP_70(0x0, 0xFA)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x0)
    OP_A2(0x10AD)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_1729")

    Jump("loc_17A4")

    label("loc_172C")


    Menu(
        0,
        260,
        200,
        1,
        (
            "Return To Original Position\x01",      # 0
            "Stop\x01",                             # 1
        )
    )

    MenuEnd(0x0)
    OP_5F(0x0)
    OP_56(0x0)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_17A4")
    EventBegin(0x0)
    OP_6F(0x7, 60)
    OP_70(0x7, 0x0)
    OP_22(0xFA, 0x0, 0x64)
    OP_73(0x7)
    OP_6F(0x0, 250)
    OP_70(0x0, 0x0)
    OP_22(0xFC, 0x0, 0x64)
    OP_73(0x0)
    OP_A3(0x10AD)
    SetMapFlags(0x1)
    EventEnd(0x3)
    Return()

    label("loc_17A4")

    OP_69(0x0, 0x258)
    ClearMapFlags(0x80)
    SetMapFlags(0x1)
    TalkEnd(0xFF)
    Return()

    # Function_13_166D end

    SaveToFile()

Try(main)
