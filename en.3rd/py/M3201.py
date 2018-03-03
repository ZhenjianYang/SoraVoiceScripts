from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M3201   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M3201.x',
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
        'Kanone',                               # 9
        'Gun Special Ops Soldier',              # 10
        'Gun Special Ops Soldier',              # 11
        'Claw Special Ops Soldier',             # 12
        'Claw Special Ops Soldier',             # 13
        'Heavy-Armor Special Ops Soldier',      # 14
        '',                                     # 15
        '',                                     # 16
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
        'ED6_DT27/CH03120 ._CH',             # 00
        'ED6_DT27/CH04120 ._CH',             # 01
        'ED6_DT06/CH20027 ._CH',             # 02
        'ED6_DT27/CH04124 ._CH',             # 03
        'ED6_DT27/CH04125 ._CH',             # 04
        'ED6_DT27/CH04126 ._CH',             # 05
        'ED6_DT07/CH00340 ._CH',             # 06
        'ED6_DT07/CH00342 ._CH',             # 07
        'ED6_DT07/CH00440 ._CH',             # 08
        'ED6_DT07/CH00441 ._CH',             # 09
        'ED6_DT07/CH00500 ._CH',             # 0A
        'ED6_DT07/CH00508 ._CH',             # 0B
        'ED6_DT07/CH00320 ._CH',             # 0C
        'ED6_DT07/CH00321 ._CH',             # 0D
    )

    AddCharChipPat(
        'ED6_DT27/CH03120P._CP',             # 00
        'ED6_DT27/CH04120P._CP',             # 01
        'ED6_DT06/CH20027P._CP',             # 02
        'ED6_DT27/CH04124P._CP',             # 03
        'ED6_DT27/CH04125P._CP',             # 04
        'ED6_DT27/CH04126P._CP',             # 05
        'ED6_DT07/CH00340P._CP',             # 06
        'ED6_DT07/CH00342P._CP',             # 07
        'ED6_DT07/CH00440P._CP',             # 08
        'ED6_DT07/CH00441P._CP',             # 09
        'ED6_DT07/CH00500P._CP',             # 0A
        'ED6_DT07/CH00508P._CP',             # 0B
        'ED6_DT07/CH00320P._CP',             # 0C
        'ED6_DT07/CH00321P._CP',             # 0D
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 8,
        ChipIndex           = 0x8,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 10,
        ChipIndex           = 0xA,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclMonster(
        X                   = -15320,
        Z                   = 0,
        Y                   = 870,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28C,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 43940,
        Z                   = 0,
        Y                   = 35180,
        Unknown_0C          = 180,
        Unknown_0E          = 12,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x28D,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = -42100,
        TriggerZ            = 0,
        TriggerY            = 15050,
        TriggerRange        = 1000,
        ActorX              = -42100,
        ActorZ              = 800,
        ActorY              = 15050,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_236",          # 00, 0
        "Function_1_25C",          # 01, 1
        "Function_2_272",          # 02, 2
        "Function_3_36F",          # 03, 3
        "Function_4_378",          # 04, 4
        "Function_5_20C6",         # 05, 5
        "Function_6_2115",         # 06, 6
        "Function_7_2164",         # 07, 7
        "Function_8_21B3",         # 08, 8
        "Function_9_2202",         # 09, 9
        "Function_10_2251",        # 0A, 10
        "Function_11_2DDF",        # 0B, 11
    )


    def Function_0_236(): pass

    label("Function_0_236")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_25B")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 4)), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_25B")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 3)

    label("loc_25B")

    Return()

    # Function_0_236 end

    def Function_1_25C(): pass

    label("Function_1_25C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x563, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_26D")
    OP_72(0x1001, 0x0)
    ExitThread()
    Jump("loc_271")

    label("loc_26D")

    OP_64(0x0, 0x1)

    label("loc_271")

    Return()

    # Function_1_25C end

    def Function_2_272(): pass

    label("Function_2_272")

    TalkBegin(0xFF)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    OP_22(0x74, 0x0, 0x64)
    Sleep(300)
    FadeToDark(300, 0, 100)
    SetChrName("")
    SetMessageWindowPos(72, 320, 56, 3)

    AnonymousTalk(    #0
        "\x07\x05The door is locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_0D()
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x570, 0)), scpexpr(EXPR_END)), "loc_36B")
    FadeToDark(300, 0, 100)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    label("loc_2E7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B")

    Menu(
        1,
        -1,
        -1,
        1,
        (
            "Use B-01 Key\x01",      # 0
            "Cancel\x01",            # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_337"),
        (SWITCH_DEFAULT, "loc_35B"),
    )


    label("loc_337")

    OP_22(0x73, 0x0, 0x64)
    Sleep(500)
    OP_A2(0x2B1C)
    OP_71(0x1001, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_368")

    label("loc_35B")

    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0xFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jump("loc_368")

    label("loc_368")

    Jump("loc_2E7")

    label("loc_36B")

    TalkEnd(0xFF)
    Return()

    # Function_2_272 end

    def Function_3_36F(): pass

    label("Function_3_36F")

    Call(0, 4)
    Call(0, 10)
    Return()

    # Function_3_36F end

    def Function_4_378(): pass

    label("Function_4_378")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4E, 0x2)
    OP_E0(238, 0x4F, 0x3)
    OP_E0(239, 0x50, 0x2)
    OP_E0(239, 0x51, 0x3)
    OP_E0(240, 0x52, 0x2)
    OP_E0(240, 0x53, 0x3)
    OP_E0(241, 0x54, 0x2)
    OP_E0(241, 0x55, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 830, 0, 48770, 180)
    SetChrSubChip(0x10, 0)
    SetChrPos(0x109, 450, 0, 38370, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_458")
    SetChrPos(0xEF, 1770, 0, 38220, 0)
    SetChrPos(0xF0, 0, 0, 36840, 0)
    SetChrPos(0xF1, 1800, 0, 36800, 0)
    Jump("loc_4DD")

    label("loc_458")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_49C")
    SetChrPos(0xF0, 1770, 0, 38220, 0)
    SetChrPos(0xEF, 0, 0, 36840, 0)
    SetChrPos(0xF1, 1800, 0, 36800, 0)
    Jump("loc_4DD")

    label("loc_49C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4DD")
    SetChrPos(0xF1, 1770, 0, 38220, 0)
    SetChrPos(0xEF, 0, 0, 36840, 0)
    SetChrPos(0xF0, 1800, 0, 36800, 0)

    label("loc_4DD")

    OP_6D(1970, 0, 38740, 0)
    OP_67(0, 6350, -10000, 0)
    OP_6B(2750, 0)
    OP_6C(45000, 0)
    OP_6E(260, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    NpcTalk(    #1
        0x10,
        "Woman's Voice",
        "#4PI've been waiting for you, Your Excellency.\x02",
    )

    CloseMessageWindow()
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5AF")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_616")

    label("loc_5AF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5D7")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_616")

    label("loc_5D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_5FF")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_616")

    label("loc_5FF")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_616")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_643")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6AA")

    label("loc_643")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_66B")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6AA")

    label("loc_66B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_693")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_6AA")

    label("loc_693")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_6AA")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6D7")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_73E")

    label("loc_6D7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_6FF")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_73E")

    label("loc_6FF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_727")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_73E")

    label("loc_727")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_73E")

    Sleep(1000)
    Fade(500)
    OP_6D(2210, 0, 50140, 0)
    OP_67(0, 4660, -10000, 0)
    OP_6B(2790, 0)
    OP_6C(45000, 0)
    OP_6E(264, 0)
    OP_0D()
    Sleep(300)

    ChrTalk(    #2
        0x109,
        "#1064F#1PWha...?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0x10C,
        "#115F#1PSo our next opponent is you, Kanone.\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_7DE():
        OP_6D(2390, 0, 46240, 2000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_7DE)

    def lambda_7F6():
        OP_67(0, 5010, -10000, 2000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_7F6)

    def lambda_80E():
        OP_6B(2310, 2000)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_80E)

    def lambda_81E():
        OP_6E(367, 2000)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_81E)
    Sleep(1000)

    def lambda_833():
        OP_8F(0xFE, 0xD2, 0x0, 0xA69A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_833)
    Sleep(100)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B9")

    def lambda_861():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_861)
    Sleep(100)

    def lambda_881():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_881)
    Sleep(100)

    def lambda_8A1():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_8A1)
    Jump("loc_98E")

    label("loc_8B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_925")

    def lambda_8CD():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_8CD)
    Sleep(100)

    def lambda_8ED():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_8ED)
    Sleep(100)

    def lambda_90D():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_90D)
    Jump("loc_98E")

    label("loc_925")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_98E")

    def lambda_939():
        OP_8F(0xFE, 0x640, 0x0, 0xA668, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_939)
    Sleep(100)

    def lambda_959():
        OP_8F(0xFE, 0xFFFFFF1A, 0x0, 0x9FE2, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_959)
    Sleep(100)

    def lambda_979():
        OP_8F(0xFE, 0x622, 0x0, 0xA032, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_979)

    label("loc_98E")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    WaitChrThread(0xEE, 0x1)
    Sleep(500)

    ChrTalk(    #4
        0x10,
        (
            "#1321F#5PWhat a tragedy it is that we should be forced\x01",
            "to meet under these circumstances.\x02\x03",

            "What did I ever do to deserve turning my blade\x01",
            "against the man I've always duly served?\x02\x03",

            "#1185FBut please, never doubt even for a second that\x01",
            "I'm doing this against my will! I would never\x01",
            "even dream of fighting you if I had a choice!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0x10C,
        (
            "#119F#12PI understand perfectly well, Kanone.\x02\x03",

            "#111FBut if I may...I would rather you stopped calling\x01",
            "me Your Excellency.\x02\x03",

            "It was never a fitting title for a mere colonel to\x01",
            "begin with, and now I don't even have that.\x02\x03",

            "I would rather you simply called me 'sir' like you\x01",
            "usually do in the office. I've grown very fond of\x01",
            "it.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #6
        0x10,
        (
            "#1323F#5PY-Your Excellency...\x02\x03",

            "#1189F...I'm sorry. Just while we're here, please let me\x01",
            "call you the way I'd like to.\x02\x03",

            "The Kanone Amalthea who stands before you\x01",
            "is a symbol of my failure to truly move forward\x01",
            "from the past...\x02\x03",

            "#1185F...and something tells me that if this symbol were\x01",
            "defeated by you, then it will finally allow me to put\x01",
            "the past where it belongs and be born anew!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0x10C,
        (
            "#113F#12PKanone...\x02\x03",

            "#115FVery well. In that case, do as you will.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E8")
    Sleep(500)

    ChrTalk(    #8
        0x10,
        (
            "#1182F#5PIt makes my position all the more frustrating to\x01",
            "see YOU at His Excellency's side, too, Julia.\x02\x03",

            "Why could I not have been chosen to serve him\x01",
            "in your place?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0x10E,
        (
            "#176F#12PI can imagine how you must feel.\x02\x03",

            "#178FWhatever I may feel about being in this perilous\x01",
            "situation, I at least owe my thanks to Aidios for\x01",
            "letting me protect Her Highness with my own hands.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FD6")

    ChrTalk(    #10
        0x105,
        "#1382F#12PI'm touched you would say that, Julia.\x02",
    )

    CloseMessageWindow()

    label("loc_FD6")


    ChrTalk(    #11
        0x10,
        (
            "#1180F#5PHmph. Well, I can't change it now.\x02\x03",

            "#1183FI don't need to feel the slightest twinge of\x01",
            "guilt about fighting against you.\x02\x03",

            "#1181FSo go ahead and show me what you can do--\x01",
            "I doubt it'll be enough to match up to me.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #12
        0x10E,
        "#179F#4PHeh. I could say the same to you.\x02",
    )

    CloseMessageWindow()

    label("loc_10E8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")
    Sleep(500)

    ChrTalk(    #13
        0x10,
        (
            "#1180F#5PMeanwhile, we meet again Estelle Bright...\x01",
            "Yours isn't a name I'm likely to forget any\x01",
            "time soon.\x02\x03",

            "I've heard you're away from Liberl training\x01",
            "at the moment. I trust you're well?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #14
        0x101,
        (
            "#1016F#12PI'm doing all right, thanks.\x02\x03",

            "#1015FSo...like, you're running a research company\x01",
            "with Colonel Richard now, aren't you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #15
        0x10,
        (
            "#1183F#5PIndeed. In some ways, that makes us the Bracer\x01",
            "Guild's business rivals.\x02\x03",

            "#1181FI'm sure we'll get to know each other much better\x01",
            "over time because of that...but why not start now\x01",
            "through battle? Don't hold back--I won't be.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #16
        0x101,
        "#1016F#4PY-You can hold back a LITTLE...\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1386")

    ChrTalk(    #17
        0x102,
        "#1514F#12PHaha...\x02",
    )

    CloseMessageWindow()
    Jump("loc_13AD")

    label("loc_1386")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13AD")

    ChrTalk(    #18
        0x107,
        "#067F#12PA-Ahaha...\x02",
    )

    CloseMessageWindow()

    label("loc_13AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_13F1")

    ChrTalk(    #19
        0x106,
        "#051F#12PHeh. Wouldn't have it any other way.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1438")

    label("loc_13F1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1438")

    ChrTalk(    #20
        0x103,
        "#1527F#12PHaha... I wouldn't have it any other way.\x02",
    )

    CloseMessageWindow()

    label("loc_1438")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1642")
    Sleep(500)

    ChrTalk(    #21
        0x10,
        (
            "#1322F#5PS-Still...\x02\x03",

            "#1182F...just what are YOU doing here, child?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #22
        0x110,
        (
            "#261F#12PIt's good to see you again, too!\x02\x03",

            "#265FNot since I gave you that Gospel as a present,\x01",
            "I believe... I don't think I ever got the chance\x01",
            "to ask if you liked it, did I?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#1189F#5PY-You've got some nerve acting friendly with\x01",
            "me after all you put us through!\x02\x03",

            "#1187FI'm going to enjoy having this opportunity to\x01",
            "punish you for your insolence!\x02\x03",

            "I hope you're ready for this!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x110,
        "#1306F#12PHeehee. Go ahead and try. ♪\x02",
    )

    CloseMessageWindow()

    label("loc_1642")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_174D")

    ChrTalk(    #25
        0x109,
        (
            "#1066F#6PWell, I can respect the whole want-to-be-reborn\x01",
            "thing, but I see she hasn't ditched any of her old\x01",
            "highhanded ways.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_172C")

    ChrTalk(    #26
        0x108,
        "#071F#12PThat's her best quality, if you ask me.\x02",
    )

    CloseMessageWindow()

    label("loc_172C")


    ChrTalk(    #27
        0x10,
        "#1182F#5PS-Silence, you!\x02",
    )

    CloseMessageWindow()
    Jump("loc_182C")

    label("loc_174D")


    ChrTalk(    #28
        0x109,
        (
            "#1066F#6PWell, I'll be damned. Maybe she's actually got\x01",
            "a likable, respectable side after all.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_17F6")

    ChrTalk(    #29
        0x108,
        "#071F#12PHaha... I always thought so, personally.\x02",
    )

    CloseMessageWindow()

    label("loc_17F6")


    ChrTalk(    #30
        0x10,
        "#1185F#5PY-You don't have to sound so surprised!\x02",
    )

    CloseMessageWindow()

    label("loc_182C")

    Sleep(300)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    OP_0D()
    Sleep(300)
    SetChrChipByIndex(0x10, 4)

    def lambda_1856():

        label("loc_1856")

        OP_99(0xFE, 0x0, 0x3, 0x5DC)
        OP_48()
        Jump("loc_1856")

    QueueWorkItem2(0x10, 3, lambda_1856)
    PlayEffect(0x2, 0x0, 0x10, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -2009, 100, 47910, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 3190, 100, 48160, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -3530, 100, 43250, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 4900, 100, 43000, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, 810, 100, 46670, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19D8")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A3F")

    label("loc_19D8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A00")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A3F")

    label("loc_1A00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A28")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A3F")

    label("loc_1A28")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A3F")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A6C")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1AD3")

    label("loc_1A6C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A94")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1AD3")

    label("loc_1A94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ABC")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1AD3")

    label("loc_1ABC")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1AD3")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B00")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B67")

    label("loc_1B00")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B28")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B67")

    label("loc_1B28")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B50")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1B67")

    label("loc_1B50")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1B67")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1B94")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BFB")

    label("loc_1B94")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BBC")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BFB")

    label("loc_1BBC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BE4")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1BFB")

    label("loc_1BE4")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1BFB")

    Sleep(1000)

    def lambda_1C06():
        OP_6D(1930, 0, 46370, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1C06)

    def lambda_1C1E():
        OP_67(0, 5540, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1C1E)

    def lambda_1C36():
        OP_6B(2920, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1C36)

    def lambda_1C46():
        OP_6E(303, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1C46)

    def lambda_1C56():
        OP_6C(33000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1C56)
    ClearChrFlags(0x11, 0x80)
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    SetChrPos(0x11, -2009, -3000, 47910, 180)
    SetChrPos(0x12, 3190, -3000, 48160, 180)
    SetChrPos(0x13, -3530, -3000, 43250, 90)
    SetChrPos(0x14, 4900, -3000, 43000, 270)
    SetChrPos(0x15, 810, -3000, 46670, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1CD9():

        label("loc_1CD9")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1CD9")

    QueueWorkItem2(0x109, 3, lambda_1CD9)
    OP_43(0x11, 0x0, 0x0, 0x5)
    OP_43(0x12, 0x0, 0x0, 0x6)
    OP_43(0x13, 0x0, 0x0, 0x7)
    OP_43(0x14, 0x0, 0x0, 0x8)
    OP_43(0x15, 0x0, 0x0, 0x9)
    Sleep(300)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D6E")

    def lambda_1D2A():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1D2A)
    Sleep(50)

    def lambda_1D3D():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1D3D)
    Sleep(50)

    def lambda_1D50():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1D50)
    Sleep(50)

    def lambda_1D63():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1D63)
    Jump("loc_1E1B")

    label("loc_1D6E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DC6")

    def lambda_1D82():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1D82)
    Sleep(50)

    def lambda_1D95():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF0, 1, lambda_1D95)
    Sleep(50)

    def lambda_1DA8():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1DA8)
    Sleep(50)

    def lambda_1DBB():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1DBB)
    Jump("loc_1E1B")

    label("loc_1DC6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1B")

    def lambda_1DDA():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1DDA)
    Sleep(50)

    def lambda_1DED():
        OP_8C(0xFE, 0, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1DED)
    Sleep(50)

    def lambda_1E00():
        OP_8C(0xFE, 315, 600)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_1E00)
    Sleep(50)

    def lambda_1E13():
        OP_8C(0xFE, 45, 600)
        ExitThread()

    QueueWorkItem(0xF1, 1, lambda_1E13)

    label("loc_1E1B")

    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 14)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 16)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 18)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 20)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x11, 0x0)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    OP_44(0x109, 0x3)
    OP_44(0x10, 0x3)
    OP_23(0x85)
    OP_1D(0xC4)
    Fade(1000)
    OP_82(0x0, 0x0)
    LoadEffect(0x1, "map\\mp250_00.eff")
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_82(0x4, 0x0)
    OP_82(0x5, 0x0)
    OP_0D()
    WaitChrThread(0xEE, 0x0)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 5)
    SetChrSubChip(0x10, 1)
    OP_0D()
    Sleep(500)

    ChrTalk(    #31
        0x10,
        (
            "#1186F#5PWell, Your Excellency...I have no intention of\x01",
            "holding back.\x02\x03",

            "So, are you ready to begin?!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #32
        0x10C,
        "#112F#12PAt any time!\x02",
    )

    CloseMessageWindow()
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1F74():
        OP_6D(1600, 0, 44760, 280)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1F74)

    def lambda_1F8C():
        OP_67(0, 5830, -10000, 280)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1F8C)

    def lambda_1FA4():
        OP_6B(2200, 280)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1FA4)

    def lambda_1FB4():
        OP_6E(323, 280)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1FB4)
    Sleep(100)
    SetChrChipByIndex(0x11, 9)

    def lambda_1FCE():
        OP_8F(0xFE, 0xFFFFFDE4, 0x0, 0xA9B0, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1FCE)
    SetChrChipByIndex(0x12, 9)

    def lambda_1FEE():
        OP_8F(0xFE, 0x546, 0x0, 0xAB72, 0x2134, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1FEE)
    OP_7D(0x0, 0x13, 0x32, 0x1F4)
    SetChrFlags(0x13, 0x20)
    SetChrChipByIndex(0x13, 7)
    SetChrSubChip(0x13, 6)

    def lambda_2020():
        OP_8F(0xFE, 0xFFFFFCC2, 0x0, 0xA47E, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_2020)
    OP_7D(0x0, 0x14, 0x32, 0x1F4)
    SetChrFlags(0x14, 0x20)
    SetChrChipByIndex(0x14, 7)
    SetChrSubChip(0x14, 6)

    def lambda_2052():
        OP_8F(0xFE, 0x7D0, 0x0, 0xA4E2, 0x1B58, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_2052)
    SetChrChipByIndex(0x15, 11)
    SetChrSubChip(0x15, 0)

    def lambda_2077():
        OP_99(0xFE, 0x0, 0x3, 0x9C4)
        ExitThread()

    QueueWorkItem(0x15, 2, lambda_2077)
    OP_22(0xA3, 0x0, 0x64)

    def lambda_208C():
        OP_96(0xFE, 0x442, 0x0, 0xA604, 0x3E8, 0x1B58)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_208C)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2A8, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_4_378 end

    def Function_5_20C6(): pass

    label("Function_5_20C6")

    PlayEffect(0x1, 0xFF, 0xFF, -2009, 100, 47910, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_20C6 end

    def Function_6_2115(): pass

    label("Function_6_2115")

    PlayEffect(0x1, 0xFF, 0xFF, 3190, 100, 48160, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_2115 end

    def Function_7_2164(): pass

    label("Function_7_2164")

    PlayEffect(0x1, 0xFF, 0xFF, -3530, 100, 43250, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_2164 end

    def Function_8_21B3(): pass

    label("Function_8_21B3")

    PlayEffect(0x1, 0xFF, 0xFF, 4900, 100, 43000, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_21B3 end

    def Function_9_2202(): pass

    label("Function_9_2202")

    PlayEffect(0x1, 0xFF, 0xFF, 810, 100, 46670, 0, 0, 0, 400, 400, 400, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_2202 end

    def Function_10_2251(): pass

    label("Function_10_2251")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrFlags(0x10, 0x800)
    SetChrPos(0x10, 740, 0, 47860, 180)
    SetChrChipByIndex(0x10, 3)
    SetChrSubChip(0x10, 3)
    OP_43(0x10, 0x3, 0x0, 0xB)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    LoadEffect(0x2, "map\\mp257_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    SetChrPos(0x109, -500, 0, 43300, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2387")
    SetChrPos(0xEF, 780, 0, 44800, 0)
    SetChrPos(0xF0, 1600, 0, 43500, 0)
    SetChrPos(0xF1, 320, 0, 42300, 0)
    Jump("loc_240C")

    label("loc_2387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23CB")
    SetChrPos(0xF0, 780, 0, 44800, 0)
    SetChrPos(0xEF, 1600, 0, 43500, 1)
    SetChrPos(0xF1, 320, 0, 42300, 0)
    Jump("loc_240C")

    label("loc_23CB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_240C")
    SetChrPos(0xF1, 780, 0, 44800, 0)
    SetChrPos(0xEF, 1600, 0, 43500, 1)
    SetChrPos(0xF0, 320, 0, 42300, 0)

    label("loc_240C")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(1810, 0, 46710, 0)
    OP_67(0, 5700, -10000, 0)
    OP_6B(2680, 0)
    OP_6C(45000, 0)
    OP_6E(292, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #33
        0x10,
        (
            "#1183F#5PHaha... I knew I wouldn't stand a chance\x01",
            "against you, Your Excellency...\x02\x03",

            "#1180F...The rest of you fought passably as well,\x01",
            "I suppose.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #34
        0x109,
        "#1066F#6PHaha. Thanks.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2561")

    ChrTalk(    #35
        0x10E,
        "#171F#12PHeh. As did you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2623")

    label("loc_2561")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25A0")

    ChrTalk(    #36
        0x106,
        "#051F#12PHeh. Could say the same to you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2623")

    label("loc_25A0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25E3")

    ChrTalk(    #37
        0x103,
        "#1536F#12PHaha. I could say the same to you.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2623")

    label("loc_25E3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2623")

    ChrTalk(    #38
        0x102,
        "#1513F#12PYou put up quite a fight yourself.\x02",
    )

    CloseMessageWindow()

    label("loc_2623")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2678")

    ChrTalk(    #39
        0x101,
        (
            "#1017F#12PAhaha... You gave us a real run for our money\x01",
            "yourself.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_2678")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26B1")

    ChrTalk(    #40
        0x110,
        "#261F#12PHeehee. That was fun enough.\x02",
    )

    CloseMessageWindow()

    label("loc_26B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_26ED")

    ChrTalk(    #41
        0x108,
        "#071F#12PHaha. You fought well yourself.\x02",
    )

    CloseMessageWindow()

    label("loc_26ED")


    ChrTalk(    #42
        0x10,
        (
            "#1322F#5PHmph...\x02\x03",

            "#1182FAll of you should make sure you don't get in\x01",
            "His Excellency's way in the battles ahead.\x02\x03",

            "You'll be facing the strongest warriors in Liberl.\x01",
            "He doesn't need you stopping him from fighting\x01",
            "at his best.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2800")

    ChrTalk(    #43
        0x10F,
        "#1447F#12P...Of course.\x02",
    )

    CloseMessageWindow()
    Jump("loc_2820")

    label("loc_2800")


    ChrTalk(    #44
        0x109,
        "#1075F#6PWay ahead of you.\x02",
    )

    CloseMessageWindow()

    label("loc_2820")


    ChrTalk(    #45
        0x10C,
        (
            "#115F#12PKanone...\x02\x03",

            "It seems there's still something important left\x01",
            "for me to do after all.\x02\x03",

            "#116FHowever, I believe that by clearing the trials\x01",
            "ahead, I will finally be able to do it.\x02\x03",

            "#111FIt's thanks to you that I feel ready enough to\x01",
            "face those trials head on. So, thank you.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #46
        0x10,
        (
            "#1323F#5PY-You don't have to thank me...\x02\x03",

            "#1183FI don't think there's anything more I could\x01",
            "say for you right now.\x02\x03",

            "#1320FAll I'll do is pray that you safely overcome\x01",
            "the trials before you and return to the real\x01",
            "world unharmed.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #47
        0x10C,
        "#119F#12PThank you. I will.\x02",
    )

    CloseMessageWindow()
    Sleep(300)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -600, 0, 0, 0, 0, 1750, 1750, 1750, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)

    def lambda_2AA2():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_2AA2)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_0D()
    PlayEffect(0x2, 0x0, 0xFF, 740, 300, 47860, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(1500)
    SetChrFlags(0x10, 0x80)

    ChrTalk(    #48
        0x10C,
        "#116F#12P...\x02",
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_2B1B():
        OP_6D(2000, 0, 47710, 1500)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_2B1B)
    OP_8F(0x10C, 0x302, 0x0, 0xB798, 0x7D0, 0x0)
    Sleep(500)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10C, 2)
    SetChrSubChip(0x10C, 0)
    OP_0D()
    Sleep(500)
    OP_82(0x0, 0x2)
    Sleep(500)
    OP_22(0x11, 0x0, 0x64)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #49
        "\x07\x05Received \x1F\x34\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_3E(0x334, 1)
    CloseMessageWindow()
    Sleep(300)
    Fade(250)
    OP_22(0x8F, 0x0, 0x64)
    SetChrChipByIndex(0x10C, 65535)
    SetChrSubChip(0x10C, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #50
        0x109,
        (
            "#1075F#12PAnyway, let's shuffle on to the heart of\x01",
            "the fortress.\x02\x03",

            "#1060FThat's the key to the command center,\x01",
            "right?\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x10C, 180, 400)
    Sleep(300)

    ChrTalk(    #51
        0x10C,
        (
            "#115F#5PThat's correct. It's the building directly in front\x01",
            "of you when you enter the main courtyard from\x01",
            "the entrance.\x02\x03",

            "#110FThis key should allow us to gain access to it.\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x2B1D)
    OP_28(0x39, 0x1, 0x40)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_6D(760, 0, 43590, 0)
    OP_67(0, 6000, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x0, 760, 0, 43590, 180)
    SetChrPos(0x1, 760, 0, 43590, 180)
    SetChrPos(0x2, 760, 0, 43590, 180)
    SetChrPos(0x3, 760, 0, 43590, 180)
    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_69(0x0, 0x0)
    Sleep(500)
    OP_1D(0xE8)
    FadeToBright(1000, 0)
    EventEnd(0x0)
    Return()

    # Function_10_2251 end

    def Function_11_2DDF(): pass

    label("Function_11_2DDF")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E00")
    Sleep(100)
    Jump("loc_2E7B")

    label("loc_2E00")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E15")
    Sleep(200)
    Jump("loc_2E7B")

    label("loc_2E15")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E2A")
    Sleep(300)
    Jump("loc_2E7B")

    label("loc_2E2A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E3F")
    Sleep(400)
    Jump("loc_2E7B")

    label("loc_2E3F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E54")
    Sleep(500)
    Jump("loc_2E7B")

    label("loc_2E54")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E69")
    Sleep(600)
    Jump("loc_2E7B")

    label("loc_2E69")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E7B")
    Sleep(700)

    label("loc_2E7B")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2E9D")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_2E7B")

    label("loc_2E9D")

    Return()

    # Function_11_2DDF end

    SaveToFile()

Try(main)
