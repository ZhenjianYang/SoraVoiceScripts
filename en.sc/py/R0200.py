from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'R0200   ._SN',
        MapName             = 'Rolent',
        Location            = 'R0200.x',
        MapIndex            = 22,
        MapDefaultBGM       = "ed60029",
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
        'Rolent',                               # 9
        'Verte Bridge',                         # 10
        '飛び猫',                               # 11
        'リリームーバー',                       # 12
        '混合',                                 # 13
        'マントラップ',                         # 14
        'リリームーバー',                       # 15
        '飛び猫',                               # 16
        '赤茶玉虫',                             # 17
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
        'ED6_DT09/CH10020 ._CH',             # 00
        'ED6_DT09/CH10021 ._CH',             # 01
        'ED6_DT09/CH10180 ._CH',             # 02
        'ED6_DT09/CH10181 ._CH',             # 03
        'ED6_DT09/CH10260 ._CH',             # 04
        'ED6_DT09/CH10261 ._CH',             # 05
        'ED6_DT09/CH10210 ._CH',             # 06
        'ED6_DT09/CH10211 ._CH',             # 07
        'ED6_DT29/CH12090 ._CH',             # 08
        'ED6_DT29/CH12091 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT09/CH10020P._CP',             # 00
        'ED6_DT09/CH10021P._CP',             # 01
        'ED6_DT09/CH10180P._CP',             # 02
        'ED6_DT09/CH10181P._CP',             # 03
        'ED6_DT09/CH10260P._CP',             # 04
        'ED6_DT09/CH10261P._CP',             # 05
        'ED6_DT09/CH10210P._CP',             # 06
        'ED6_DT09/CH10211P._CP',             # 07
        'ED6_DT29/CH12090P._CP',             # 08
        'ED6_DT29/CH12091P._CP',             # 09
    )

    DeclNpc(
        X                   = -48570,
        Z                   = 0,
        Y                   = -24070,
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
        X                   = -143230,
        Z                   = 0,
        Y                   = -17530,
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
        X                   = -78000,
        Z                   = 0,
        Y                   = -16000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -92600,
        Z                   = 0,
        Y                   = -13700,
        Unknown_0C          = 160,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -121000,
        Z                   = 0,
        Y                   = -31000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7E,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -108000,
        Z                   = 0,
        Y                   = 1800,
        Unknown_0C          = 228,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -103000,
        Z                   = 0,
        Y                   = -25600,
        Unknown_0C          = 10,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7A,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -118000,
        Z                   = 0,
        Y                   = -8000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x79,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -81000,
        Z                   = 0,
        Y                   = -36000,
        Unknown_0C          = 0,
        Unknown_0E          = 8,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x7B,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -105260,
        TriggerZ            = 0,
        TriggerY            = 14600,
        TriggerRange        = 1000,
        ActorX              = -104710,
        ActorZ              = 1500,
        ActorY              = 14910,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -74510,
        TriggerZ            = 0,
        TriggerY            = -19420,
        TriggerRange        = 1500,
        ActorX              = -74510,
        ActorZ              = 1500,
        ActorY              = -19420,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -118840,
        TriggerZ            = -90,
        TriggerY            = 3750,
        TriggerRange        = 1000,
        ActorX              = -116330,
        ActorZ              = -500,
        ActorY              = 6430,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_26A",          # 00, 0
        "Function_1_26B",          # 01, 1
        "Function_2_345",          # 02, 2
        "Function_3_43F",          # 03, 3
        "Function_4_613",          # 04, 4
    )


    def Function_0_26A(): pass

    label("Function_0_26A")

    Return()

    # Function_0_26A end

    def Function_1_26B(): pass

    label("Function_1_26B")

    OP_16(0x2, 0xFA0, 0xFFFC8D30, 0xFFFDBDE0, 0x23000B)
    OP_4F(0x3A, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_GE), scpexpr(EXPR_END)), "loc_298")
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x1)

    label("loc_298")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_2AA")
    OP_6F(0x0, 0)
    Jump("loc_2B1")

    label("loc_2AA")

    OP_6F(0x0, 60)

    label("loc_2B1")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F7")
    OP_C4(0x0, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x303, 4)), scpexpr(EXPR_END)), "loc_2E2")
    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0xEA60, 0x0)
    Jump("loc_2F7")

    label("loc_2E2")

    SetMapFlags(0x10)
    OP_11(0xE6, 0xF0, 0xFF, 0x0, 0x13880, 0x0)

    label("loc_2F7")

    OP_51(0xA, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xB, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xC, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xD, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xE, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0xF, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Return()

    # Function_1_26B end

    def Function_2_345(): pass

    label("Function_2_345")

    OP_EA(0x2, 0xC1, 0x1, 0x0)
    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x324, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_3D9")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    OP_73(0x0)
    OP_6F(0x0, 60)
    AddSepith(0x1, 0x64)
    AddSepith(0x3, 0x64)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #0
        (
            "Found\x01",
            "#2C#57IWater Sepith x100\x01",
            "#59IWind Sepith x100#0C.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x1920)
    Jump("loc_42D")

    label("loc_3D9")


    AnonymousTalk(    #1
        (
            "\x07\x05There's nothing in the chest but your failed\x01",
            "hopes and dreams for more loot.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_42D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_345 end

    def Function_3_43F(): pass

    label("Function_3_43F")

    EventBegin(0x1)

    ChrTalk(    #2
        0x101,
        "#1001FI bet I could fish here!\x02",
    )

    CloseMessageWindow()

    def lambda_46B():
        OP_6D(-117210, -110, 4810, 1500)
        ExitThread()

    QueueWorkItem(0x0, 1, lambda_46B)

    def lambda_483():
        OP_6B(2800, 1500)
        ExitThread()

    QueueWorkItem(0x1, 1, lambda_483)

    def lambda_493():
        OP_6C(270000, 1500)
        ExitThread()

    QueueWorkItem(0x1, 2, lambda_493)
    Sleep(1000)
    SetChrName("")

    AnonymousTalk(    #3
        "\x07\x05Try fishing?\x07\x00\x02",
    )

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        1,
        (
            "Hook, Line, and Sinker\x01",      # 0
            "Spare the Rod\x01",               # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    WaitChrThread(0x0, 0x1)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_603")
    RunExpression(0x2, (scpexpr(EXPR_GET_CHR_WORK, 0x101, 0x28), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NOT), scpexpr(EXPR_AND_SAVE), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_EXEC_OP, "OP_C0(0xE, 0x1, 0xFFFE2FC8, 0xFFFFFFA6, 0xEA6, 0x2D, 0xFFFE3996, 0xFFFFFE0C, 0x191E)"), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x101, 0x28, (scpexpr(EXPR_GET_RESULT, 0x2), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)), "loc_5FD")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x10)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x0, 0x40)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_5F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x73, 0x1, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5F4")
    OP_28(0x73, 0x1, 0x2)
    OP_28(0x73, 0x1, 0x8)
    Sleep(400)
    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #4
        "\x07\x05Recorded Milch Main Road fishing spot in Bracer Notebook.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)

    label("loc_5F4")

    Jump("loc_5FD")

    label("loc_5F7")

    OP_28(0x73, 0x1, 0x800)

    label("loc_5FD")

    OP_0D()
    EventEnd(0x1)
    Jump("loc_612")

    label("loc_603")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_612")
    EventEnd(0x1)

    label("loc_612")

    Return()

    # Function_3_43F end

    def Function_4_613(): pass

    label("Function_4_613")

    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #5
        (
            "\x07\x05East: City of Rolent\x01",
            "West: Verte Bridge - 172 selge\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_4_613 end

    SaveToFile()

Try(main)
