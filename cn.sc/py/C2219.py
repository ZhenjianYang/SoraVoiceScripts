from ED6SCScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'C2219   ._SN',
        MapName             = 'Ruan',
        Location            = 'C2219.x',
        MapIndex            = 84,
        MapDefaultBGM       = "ed60015",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            'ED6_DT21/C2219   ._SN',
            'ED6_DT21/C2219_1 ._SN',
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
        '弗科特老人',                           # 9
        '扎古',                                 # 10
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
        'ED6_DT07/CH01000 ._CH',             # 00
        'ED6_DT07/CH01460 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT07/CH01000P._CP',             # 00
        'ED6_DT07/CH01460P._CP',             # 01
    )

    DeclNpc(
        X                   = -2870,
        Z                   = 0,
        Y                   = 202000,
        Direction           = 270,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x101,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 1,
        TalkScenaIndex      = 0,
    )

    DeclNpc(
        X                   = 1430,
        Z                   = 0,
        Y                   = 200430,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x181,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
        TalkFunctionIndex   = 0,
        TalkScenaIndex      = 3,
    )


    DeclActor(
        TriggerX            = -6600,
        TriggerZ            = 0,
        TriggerY            = 204290,
        TriggerRange        = 800,
        ActorX              = -6600,
        ActorZ              = 1200,
        ActorY              = 204290,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 1,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 2000,
        TriggerZ            = 1000,
        TriggerY            = 192960,
        TriggerRange        = 600,
        ActorX              = 2000,
        ActorZ              = 1800,
        ActorY              = 192960,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 3030,
        TriggerZ            = 1000,
        TriggerY            = 192700,
        TriggerRange        = 600,
        ActorX              = 3230,
        ActorZ              = 1600,
        ActorY              = 192420,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 5240,
        TriggerZ            = 1000,
        TriggerY            = 194630,
        TriggerRange        = 600,
        ActorX              = 5350,
        ActorZ              = 1600,
        ActorY              = 194210,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 7110,
        TriggerZ            = 1000,
        TriggerY            = 196770,
        TriggerRange        = 800,
        ActorX              = 7110,
        ActorZ              = 2500,
        ActorY              = 196770,
        Flags               = 0x7C,
        TalkScenaIndex      = 1,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1AE",          # 00, 0
        "Function_1_1DF",          # 01, 1
        "Function_2_2C5",          # 02, 2
        "Function_3_442",          # 03, 3
        "Function_4_658",          # 04, 4
    )


    def Function_0_1AE(): pass

    label("Function_0_1AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_1CB")
    SetChrPos(0x8, 3410, 1000, 193340, 183)
    ClearChrFlags(0x9, 0x80)

    label("loc_1CB")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1DE")
    OP_A3(0x10F0)
    SetMapFlags(0x10000000)
    Event(1, 7)

    label("loc_1DE")

    Return()

    # Function_0_1AE end

    def Function_1_1DF(): pass

    label("Function_1_1DF")

    OP_B0(0x0, 0x78)
    OP_1C(0x0, 0x0, 0x4)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x40)"), scpexpr(EXPR_OR), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x10)"), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_218")
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    Jump("loc_23B")

    label("loc_218")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x0, 0x8)"), scpexpr(EXPR_EXEC_OP, "OP_29(0x6B, 0x1, 0x8000)"), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_23B")
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)

    label("loc_23B")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x4), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C4")
    OP_71(0x1, 0x4)
    OP_71(0x2, 0x4)
    OP_71(0x3, 0x4)
    OP_71(0x4, 0x4)
    OP_71(0x5, 0x4)
    OP_71(0x6, 0x4)
    OP_71(0x7, 0x4)
    OP_71(0x8, 0x4)
    OP_71(0x9, 0x4)
    OP_71(0xA, 0x4)
    OP_71(0xB, 0x4)
    OP_71(0xC, 0x4)
    OP_71(0xD, 0x4)
    OP_71(0xE, 0x4)
    OP_72(0xF, 0x4)
    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6C), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x6D), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_2AE")
    OP_78(0xC8, 0xC8, 0xC8)
    Jump("loc_2B2")

    label("loc_2AE")

    OP_78(0x96, 0x96, 0x96)

    label("loc_2B2")

    OP_79(0xFF, 0x2)
    OP_7A(0x1C, 0x2)
    OP_7B()
    OP_77(0xFF, 0xFF, 0xFF, 0x1, 0x0)

    label("loc_2C4")

    Return()

    # Function_1_1DF end

    def Function_2_2C5(): pass

    label("Function_2_2C5")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2EA")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_42C")

    label("loc_2EA")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_303")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_42C")

    label("loc_303")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_31C")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_42C")

    label("loc_31C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_335")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_42C")

    label("loc_335")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_34E")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_42C")

    label("loc_34E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_367")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_42C")

    label("loc_367")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_380")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_42C")

    label("loc_380")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_399")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_42C")

    label("loc_399")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3B2")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_42C")

    label("loc_3B2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3CB")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_42C")

    label("loc_3CB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3E4")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_42C")

    label("loc_3E4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3FD")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_42C")

    label("loc_3FD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_416")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_42C")

    label("loc_416")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_42C")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_42C")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_441")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_42C")

    label("loc_441")

    Return()

    # Function_2_2C5 end

    def Function_3_442(): pass

    label("Function_3_442")

    TalkBegin(0x9)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x405, 7)), scpexpr(EXPR_END)), "loc_55A")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_512")

    ChrTalk(    #0
        0xFE,
        (
            "爷爷似乎总算是能够\x01",
            "明白目前的状况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0xFE,
        (
            "其实我很希望他去村里避难的，\x01",
            "不过，看来这是不可能办到了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #2
        0xFE,
        (
            "唉，没办法\x01",
            "我就留在这里陪他吧。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #3
        0xFE,
        (
            "毕竟不能把爷爷一个人\x01",
            "丢在这里不管。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_557")

    label("loc_512")


    ChrTalk(    #4
        0xFE,
        (
            "爷爷似乎总算是能够\x01",
            "明白目前的状况了。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #5
        0xFE,
        "真是个倔强无比的人。\x02",
    )

    CloseMessageWindow()

    label("loc_557")

    Jump("loc_654")

    label("loc_55A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x400, 0)), scpexpr(EXPR_END)), "loc_654")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x1, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_5FC")

    ChrTalk(    #6
        0xFE,
        "唉，真伤脑筋……\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #7
        0xFE,
        (
            "关于导力器无法运行的事情\x01",
            "都已经说过好几次了……\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #8
        0xFE,
        (
            "爷爷他完全\x01",
            "都听不进去啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #9
        0xFE,
        (
            "这样的话，只好暂时\x01",
            "不管他了。\x02",
        )
    )

    CloseMessageWindow()
    OP_A2(0x9)
    Jump("loc_654")

    label("loc_5FC")


    ChrTalk(    #10
        0xFE,
        (
            "爷爷他根本就不相信\x01",
            "导力器无法运行的事实啊。\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #11
        0xFE,
        (
            "唉，这样的话，\x01",
            "只好暂时不管他了。\x02",
        )
    )

    CloseMessageWindow()

    label("loc_654")

    TalkEnd(0x9)
    Return()

    # Function_3_442 end

    def Function_4_658(): pass

    label("Function_4_658")

    TalkBegin(0xFF)
    TalkEnd(0xFF)
    Return()

    # Function_4_658 end

    SaveToFile()

Try(main)
