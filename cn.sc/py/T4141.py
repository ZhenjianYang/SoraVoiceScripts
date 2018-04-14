from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 格兰赛尔

    CreateScenaFile(
        FileName            = 'T4141   ._SN',
        MapName             = 'Grancel',
        Location            = 'T4141.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
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
            'ED6_DT21/SUB000  ._SN',
            ''
        ],
    )

    BuildStringList(
        '@FileName',                            # 8
        '莉莉',                                 # 9
        '丹顿',                                 # 10
        '蜜蒂',                                 # 11
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
        'ED6_DT07/CH01290 ._CH',             # 00
        'ED6_DT07/CH01540 ._CH',             # 01
        'ED6_DT07/CH01150 ._CH',             # 02
        'ED6_DT07/CH01020 ._CH',             # 03
        'ED6_DT07/CH01770 ._CH',             # 04
    )

    AddCharChipPat(
        'ED6_DT07/CH01290P._CP',             # 00
        'ED6_DT07/CH01540P._CP',             # 01
        'ED6_DT07/CH01150P._CP',             # 02
        'ED6_DT07/CH01020P._CP',             # 03
        'ED6_DT07/CH01770P._CP',             # 04
    )

    DeclNpc(
        X                   = 8790,
        Z                   = 0,
        Y                   = 10500,
        Direction           = 196,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )

    DeclNpc(
        X                   = 12170,
        Z                   = 0,
        Y                   = -4050,
        Direction           = 163,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 5,
    )

    DeclNpc(
        X                   = -4540,
        Z                   = 0,
        Y                   = 9850,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 4,
        ChipIndex           = 0x4,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 6,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 7,
    )


    DeclActor(
        TriggerX            = 8450,
        TriggerZ            = 0,
        TriggerY            = 8650,
        TriggerRange        = 800,
        ActorX              = 8790,
        ActorZ              = 1500,
        ActorY              = 10500,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 11970,
        TriggerZ            = 0,
        TriggerY            = -5950,
        TriggerRange        = 800,
        ActorX              = 12170,
        ActorZ              = 1500,
        ActorY              = -4050,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -6400,
        TriggerZ            = 0,
        TriggerY            = 9620,
        TriggerRange        = 800,
        ActorX              = -4540,
        ActorZ              = 1500,
        ActorY              = 9850,
        Flags               = 0x7E,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_19E",          # 00, 0
        "Function_1_19F",          # 01, 1
        "Function_2_1A0",          # 02, 2
        "Function_3_1A5",          # 03, 3
        "Function_4_200",          # 04, 4
        "Function_5_205",          # 05, 5
        "Function_6_243",          # 06, 6
        "Function_7_248",          # 07, 7
    )


    def Function_0_19E(): pass

    label("Function_0_19E")

    Return()

    # Function_0_19E end

    def Function_1_19F(): pass

    label("Function_1_19F")

    Return()

    # Function_1_19F end

    def Function_2_1A0(): pass

    label("Function_2_1A0")

    Call(0, 3)
    Return()

    # Function_2_1A0 end

    def Function_3_1A5(): pass

    label("Function_3_1A5")

    TalkBegin(0x8)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1DF")
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CA")
    OP_A9(0xD8)
    Jump("loc_1D8")

    label("loc_1CA")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x2C5, 5)), scpexpr(EXPR_END)), "loc_1D6")
    OP_A9(0xD7)
    Jump("loc_1D8")

    label("loc_1D6")

    OP_A9(0xD2)

    label("loc_1D8")

    TalkEnd(0x8)
    Return()

    label("loc_1DF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1F0")
    TalkEnd(0x8)
    Return()

    label("loc_1F0")


    ChrTalk(    #0
        0x8,
        "◆你好\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x8)
    Return()

    # Function_3_1A5 end

    def Function_4_200(): pass

    label("Function_4_200")

    Call(0, 5)
    Return()

    # Function_4_200 end

    def Function_5_205(): pass

    label("Function_5_205")

    TalkBegin(0x9)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_222")
    OP_A9(0xD3)
    TalkEnd(0x9)
    Return()

    label("loc_222")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_233")
    TalkEnd(0x9)
    Return()

    label("loc_233")


    ChrTalk(    #1
        0x9,
        "◆你好\x02",
    )

    CloseMessageWindow()
    TalkEnd(0x9)
    Return()

    # Function_5_205 end

    def Function_6_243(): pass

    label("Function_6_243")

    Call(0, 7)
    Return()

    # Function_6_243 end

    def Function_7_248(): pass

    label("Function_7_248")

    TalkBegin(0xA)
    Call(6, 4)
    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_265")
    OP_A9(0xD4)
    TalkEnd(0xA)
    Return()

    label("loc_265")

    Jc((scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_276")
    TalkEnd(0xA)
    Return()

    label("loc_276")


    ChrTalk(    #2
        0xA,
        "◆你好\x02",
    )

    CloseMessageWindow()
    TalkEnd(0xA)
    Return()

    # Function_7_248 end

    SaveToFile()

Try(main)
