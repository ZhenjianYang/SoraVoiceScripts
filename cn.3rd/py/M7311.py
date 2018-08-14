from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7311   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7311.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60224",
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


    DeclMonster(
        X                   = 15580,
        Z                   = 11740,
        Y                   = 34500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22130,
        Z                   = 4720,
        Y                   = -3290,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11800,
        Z                   = -640,
        Y                   = -37380,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27740,
        Z                   = -7380,
        Y                   = -26600,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2DA,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32700,
        Z                   = -8550,
        Y                   = -460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18390,
        Z                   = -15250,
        Y                   = 22810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15580,
        Z                   = 11740,
        Y                   = 34500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22130,
        Z                   = 4720,
        Y                   = -3290,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11800,
        Z                   = -640,
        Y                   = -37380,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27740,
        Z                   = -7380,
        Y                   = -26600,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D9,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32700,
        Z                   = -8550,
        Y                   = -460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18390,
        Z                   = -15250,
        Y                   = 22810,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15580,
        Z                   = 11740,
        Y                   = 34500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22130,
        Z                   = 4720,
        Y                   = -3290,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11800,
        Z                   = -640,
        Y                   = -37380,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D8,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27740,
        Z                   = -7380,
        Y                   = -26600,
        Unknown_0C          = 180,
        Unknown_0E          = 6,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32700,
        Z                   = -8550,
        Y                   = -460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18390,
        Z                   = -15250,
        Y                   = 22810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 15580,
        Z                   = 11740,
        Y                   = 34500,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 22130,
        Z                   = 4720,
        Y                   = -3290,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D6,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = 11800,
        Z                   = -640,
        Y                   = -37380,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -27740,
        Z                   = -7380,
        Y                   = -26600,
        Unknown_0C          = 180,
        Unknown_0E          = 4,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D5,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -32700,
        Z                   = -8550,
        Y                   = -460,
        Unknown_0C          = 180,
        Unknown_0E          = 2,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D7,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )

    DeclMonster(
        X                   = -18390,
        Z                   = -15250,
        Y                   = 22810,
        Unknown_0C          = 180,
        Unknown_0E          = 0,
        Unknown_10          = 65,
        Unknown_11          = 1,
        Unknown_12          = 0xFFFFFFFF,
        BattleIndex         = 0x2D4,
        Unknown_18          = 0,
        Unknown_1A          = 0,
    )


    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 3,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25140,
        TriggerZ            = 11750,
        TriggerY            = 29950,
        TriggerRange        = 1000,
        ActorX              = 25140,
        ActorZ              = 12750,
        ActorY              = 29950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 4,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 5,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25140,
        TriggerZ            = 11750,
        TriggerY            = 29950,
        TriggerRange        = 1000,
        ActorX              = 25140,
        ActorZ              = 12750,
        ActorY              = 29950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 6,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 7,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 8,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 9,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 12,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25140,
        TriggerZ            = 11750,
        TriggerY            = 29950,
        TriggerRange        = 1000,
        ActorX              = 25140,
        ActorZ              = 12750,
        ActorY              = 29950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 13,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -36600,
        TriggerZ            = -5550,
        TriggerY            = -19780,
        TriggerRange        = 1000,
        ActorX              = -36600,
        ActorZ              = -4550,
        ActorY              = -19780,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 14,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 15,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 25140,
        TriggerZ            = 11750,
        TriggerY            = 29950,
        TriggerRange        = 1000,
        ActorX              = 25140,
        ActorZ              = 12750,
        ActorY              = 29950,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 16,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = 15800,
        TriggerZ            = -700,
        TriggerY            = -26820,
        TriggerRange        = 1000,
        ActorX              = 15800,
        ActorZ              = 300,
        ActorY              = -26820,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 17,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_58A",          # 00, 0
        "Function_1_5DC",          # 01, 1
        "Function_2_D3A",          # 02, 2
        "Function_3_E60",          # 03, 3
        "Function_4_F00",          # 04, 4
        "Function_5_1026",         # 05, 5
        "Function_6_114C",         # 06, 6
        "Function_7_1272",         # 07, 7
        "Function_8_1398",         # 08, 8
        "Function_9_14BE",         # 09, 9
        "Function_10_1615",        # 0A, 10
        "Function_11_173B",        # 0B, 11
        "Function_12_1892",        # 0C, 12
        "Function_13_1932",        # 0D, 13
        "Function_14_1A58",        # 0E, 14
        "Function_15_1B54",        # 0F, 15
        "Function_16_1C7A",        # 10, 16
        "Function_17_1DA0",        # 11, 17
    )


    def Function_0_58A(): pass

    label("Function_0_58A")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x64), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x67), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x69), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5B4")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_ADD_SAVE), scpexpr(EXPR_END)))
    Jump("loc_5DB")

    label("loc_5B4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x66), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x68), scpexpr(EXPR_EQU), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_5DB")
    OP_CE(0x5, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_SUB_SAVE), scpexpr(EXPR_END)))

    label("loc_5DB")

    Return()

    # Function_0_58A end

    def Function_1_5DC(): pass

    label("Function_1_5DC")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE0C00, 0x23009E)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    OP_10(0x0, 0x0)
    OP_10(0x3, 0x0)
    OP_10(0x5, 0x0)
    OP_10(0x1, 0x0)
    OP_10(0x2, 0x0)
    OP_10(0x4, 0x0)
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (1, "loc_632"),
        (6, "loc_63B"),
        (11, "loc_63B"),
        (16, "loc_63B"),
        (4, "loc_644"),
        (9, "loc_644"),
        (14, "loc_644"),
        (19, "loc_64D"),
        (SWITCH_DEFAULT, "loc_656"),
    )


    label("loc_632")

    OP_10(0x0, 0x1)
    OP_10(0x4, 0x1)
    Jump("loc_65F")

    label("loc_63B")

    OP_10(0x5, 0x1)
    OP_10(0x4, 0x1)
    Jump("loc_65F")

    label("loc_644")

    OP_10(0x3, 0x1)
    OP_10(0x1, 0x1)
    Jump("loc_65F")

    label("loc_64D")

    OP_10(0x3, 0x1)
    OP_10(0x2, 0x1)
    Jump("loc_65F")

    label("loc_656")

    OP_10(0x3, 0x1)
    OP_10(0x4, 0x1)
    Jump("loc_65F")

    label("loc_65F")

    OP_71(0x400, 0x0)
    ExitThread()
    OP_71(0x401, 0x0)
    ExitThread()
    OP_71(0x402, 0x0)
    ExitThread()
    OP_71(0x403, 0x0)
    ExitThread()
    OP_71(0x404, 0x0)
    ExitThread()
    OP_71(0x405, 0x0)
    ExitThread()
    OP_71(0x406, 0x0)
    ExitThread()
    OP_71(0x407, 0x0)
    ExitThread()
    OP_71(0x408, 0x0)
    ExitThread()
    OP_71(0x409, 0x0)
    ExitThread()
    OP_71(0x40A, 0x0)
    ExitThread()
    OP_71(0x40B, 0x0)
    ExitThread()
    OP_71(0x40C, 0x0)
    ExitThread()
    OP_71(0x40D, 0x0)
    ExitThread()
    OP_71(0x40E, 0x0)
    ExitThread()
    OP_71(0x40F, 0x0)
    ExitThread()
    OP_64(0x0, 0x1)
    OP_64(0x1, 0x1)
    OP_64(0x2, 0x1)
    OP_64(0x3, 0x1)
    OP_64(0x4, 0x1)
    OP_64(0x5, 0x1)
    OP_64(0x6, 0x1)
    OP_64(0x7, 0x1)
    OP_64(0x8, 0x1)
    OP_64(0x9, 0x1)
    OP_64(0xA, 0x1)
    OP_64(0xB, 0x1)
    OP_64(0xC, 0x1)
    OP_64(0xD, 0x1)
    OP_64(0xE, 0x1)
    OP_64(0xF, 0x1)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_711")
    OP_6F(0x0, 0)
    Jump("loc_718")

    label("loc_711")

    OP_6F(0x0, 60)

    label("loc_718")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_72A")
    OP_6F(0x1, 0)
    Jump("loc_731")

    label("loc_72A")

    OP_6F(0x1, 60)

    label("loc_731")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_743")
    OP_6F(0x2, 0)
    Jump("loc_74A")

    label("loc_743")

    OP_6F(0x2, 60)

    label("loc_74A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_75C")
    OP_6F(0x3, 0)
    Jump("loc_763")

    label("loc_75C")

    OP_6F(0x3, 60)

    label("loc_763")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_775")
    OP_6F(0x4, 0)
    Jump("loc_77C")

    label("loc_775")

    OP_6F(0x4, 60)

    label("loc_77C")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_78E")
    OP_6F(0x5, 0)
    Jump("loc_795")

    label("loc_78E")

    OP_6F(0x5, 60)

    label("loc_795")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7A7")
    OP_6F(0x6, 0)
    Jump("loc_7AE")

    label("loc_7A7")

    OP_6F(0x6, 60)

    label("loc_7AE")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7C0")
    OP_6F(0x7, 0)
    Jump("loc_7C7")

    label("loc_7C0")

    OP_6F(0x7, 60)

    label("loc_7C7")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7D9")
    OP_6F(0x8, 0)
    Jump("loc_7E0")

    label("loc_7D9")

    OP_6F(0x8, 60)

    label("loc_7E0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_7F2")
    OP_6F(0x9, 0)
    Jump("loc_7F9")

    label("loc_7F2")

    OP_6F(0x9, 60)

    label("loc_7F9")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_80B")
    OP_6F(0xA, 0)
    Jump("loc_812")

    label("loc_80B")

    OP_6F(0xA, 60)

    label("loc_812")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_824")
    OP_6F(0xB, 0)
    Jump("loc_82B")

    label("loc_824")

    OP_6F(0xB, 60)

    label("loc_82B")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_83D")
    OP_6F(0xC, 0)
    Jump("loc_844")

    label("loc_83D")

    OP_6F(0xC, 60)

    label("loc_844")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_856")
    OP_6F(0xD, 0)
    Jump("loc_85D")

    label("loc_856")

    OP_6F(0xD, 60)

    label("loc_85D")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_86F")
    OP_6F(0xE, 0)
    Jump("loc_876")

    label("loc_86F")

    OP_6F(0xE, 60)

    label("loc_876")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_888")
    OP_6F(0xF, 0)
    Jump("loc_88F")

    label("loc_888")

    OP_6F(0xF, 60)

    label("loc_88F")

    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (1, "loc_8D7"),
        (2, "loc_8E4"),
        (3, "loc_8F1"),
        (4, "loc_8FE"),
        (6, "loc_90B"),
        (7, "loc_918"),
        (8, "loc_925"),
        (9, "loc_932"),
        (11, "loc_93F"),
        (12, "loc_94C"),
        (13, "loc_959"),
        (14, "loc_966"),
        (16, "loc_973"),
        (17, "loc_980"),
        (18, "loc_98D"),
        (19, "loc_99A"),
        (SWITCH_DEFAULT, "loc_9A7"),
    )


    label("loc_8D7")

    OP_72(0x400, 0x0)
    ExitThread()
    OP_65(0x0, 0x1)
    Jump("loc_9A7")

    label("loc_8E4")

    OP_72(0x401, 0x0)
    ExitThread()
    OP_65(0x1, 0x1)
    Jump("loc_9A7")

    label("loc_8F1")

    OP_72(0x402, 0x0)
    ExitThread()
    OP_65(0x2, 0x1)
    Jump("loc_9A7")

    label("loc_8FE")

    OP_72(0x403, 0x0)
    ExitThread()
    OP_65(0x3, 0x1)
    Jump("loc_9A7")

    label("loc_90B")

    OP_72(0x404, 0x0)
    ExitThread()
    OP_65(0x4, 0x1)
    Jump("loc_9A7")

    label("loc_918")

    OP_72(0x405, 0x0)
    ExitThread()
    OP_65(0x5, 0x1)
    Jump("loc_9A7")

    label("loc_925")

    OP_72(0x406, 0x0)
    ExitThread()
    OP_65(0x6, 0x1)
    Jump("loc_9A7")

    label("loc_932")

    OP_72(0x407, 0x0)
    ExitThread()
    OP_65(0x7, 0x1)
    Jump("loc_9A7")

    label("loc_93F")

    OP_72(0x408, 0x0)
    ExitThread()
    OP_65(0x8, 0x1)
    Jump("loc_9A7")

    label("loc_94C")

    OP_72(0x409, 0x0)
    ExitThread()
    OP_65(0x9, 0x1)
    Jump("loc_9A7")

    label("loc_959")

    OP_72(0x40A, 0x0)
    ExitThread()
    OP_65(0xA, 0x1)
    Jump("loc_9A7")

    label("loc_966")

    OP_72(0x40B, 0x0)
    ExitThread()
    OP_65(0xB, 0x1)
    Jump("loc_9A7")

    label("loc_973")

    OP_72(0x40C, 0x0)
    ExitThread()
    OP_65(0xC, 0x1)
    Jump("loc_9A7")

    label("loc_980")

    OP_72(0x40D, 0x0)
    ExitThread()
    OP_65(0xD, 0x1)
    Jump("loc_9A7")

    label("loc_98D")

    OP_72(0x40E, 0x0)
    ExitThread()
    OP_65(0xE, 0x1)
    Jump("loc_9A7")

    label("loc_99A")

    OP_72(0x40F, 0x0)
    ExitThread()
    OP_65(0xF, 0x1)
    Jump("loc_9A7")

    label("loc_9A7")

    OP_51(0x10, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x12, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x13, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x15, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x18, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1B, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1C, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1E, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xDF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x1F, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x21, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x22, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x24, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x25, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_51(0x27, 0x24, (scpexpr(EXPR_PUSH_LONG, 0xEF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Switch(
        (scpexpr(EXPR_23, 0x5), scpexpr(EXPR_END)),
        (1, "loc_A89"),
        (2, "loc_A89"),
        (3, "loc_A89"),
        (4, "loc_A89"),
        (6, "loc_B2B"),
        (7, "loc_B2B"),
        (8, "loc_B2B"),
        (9, "loc_B2B"),
        (11, "loc_BE1"),
        (12, "loc_BE1"),
        (13, "loc_BE1"),
        (14, "loc_BE1"),
        (16, "loc_C97"),
        (17, "loc_C97"),
        (18, "loc_C97"),
        (19, "loc_C97"),
        (SWITCH_DEFAULT, "loc_D39"),
    )


    label("loc_A89")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x199), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x290751, 0x290755, 0x0)
    OP_D2(0x290752, 0x290756, 0x1)
    OP_D2(0x29043C, 0x290440, 0x2)
    OP_D2(0x29043C, 0x290440, 0x3)
    OP_D2(0x2904AA, 0x2904AE, 0x4)
    OP_D2(0x2904AA, 0x2904AE, 0x5)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jump("loc_D39")

    label("loc_B2B")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x19A), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x290586, 0x29058A, 0x0)
    OP_D2(0x290586, 0x29058A, 0x1)
    OP_D2(0x29043C, 0x290440, 0x2)
    OP_D2(0x29043C, 0x290440, 0x3)
    OP_D2(0x2905B8, 0x2905BC, 0x4)
    OP_D2(0x2905B8, 0x2905BC, 0x5)
    OP_D2(0x290751, 0x290755, 0x6)
    OP_D2(0x290752, 0x290756, 0x7)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jump("loc_D39")

    label("loc_BE1")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x19B), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x2905B8, 0x2905BC, 0x0)
    OP_D2(0x2905B8, 0x2905BC, 0x1)
    OP_D2(0x29043C, 0x290440, 0x2)
    OP_D2(0x29043C, 0x290440, 0x3)
    OP_D2(0x290751, 0x290755, 0x4)
    OP_D2(0x290752, 0x290756, 0x5)
    OP_D2(0x29048C, 0x290490, 0x6)
    OP_D2(0x29048C, 0x290490, 0x7)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x22, 0x80)
    SetChrFlags(0x23, 0x80)
    SetChrFlags(0x24, 0x80)
    SetChrFlags(0x25, 0x80)
    SetChrFlags(0x26, 0x80)
    SetChrFlags(0x27, 0x80)
    Jump("loc_D39")

    label("loc_C97")

    OP_4F(0x31, (scpexpr(EXPR_PUSH_LONG, 0x19C), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_D2(0x29048C, 0x290490, 0x0)
    OP_D2(0x29048C, 0x290490, 0x1)
    OP_D2(0x29043C, 0x290440, 0x2)
    OP_D2(0x29043C, 0x290440, 0x3)
    OP_D2(0x2905B8, 0x2905BC, 0x4)
    OP_D2(0x2905B8, 0x2905BC, 0x5)
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    SetChrFlags(0x18, 0x80)
    SetChrFlags(0x19, 0x80)
    SetChrFlags(0x1A, 0x80)
    SetChrFlags(0x1B, 0x80)
    SetChrFlags(0x1C, 0x80)
    SetChrFlags(0x1D, 0x80)
    SetChrFlags(0x1E, 0x80)
    SetChrFlags(0x1F, 0x80)
    SetChrFlags(0x20, 0x80)
    SetChrFlags(0x21, 0x80)
    Jump("loc_D39")

    label("loc_D39")

    Return()

    # Function_1_5DC end

    def Function_2_D3A(): pass

    label("Function_2_D3A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E1F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_DAE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x00得到了\x1F\xFD\x01\x07\x00。\x02",
    )

    Jump("loc_D93")

    label("loc_D93")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C70)
    Jump("loc_E1C")

    label("loc_DAE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "宝箱里装有\x1F\xFD\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFD\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_DFD")

    label("loc_DFD")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_E1C")

    Jump("loc_E52")

    label("loc_E1F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_E52")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_D3A end

    def Function_3_E60(): pass

    label("Function_3_E60")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_ED2")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #3
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_EC0")

    label("loc_EC0")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C71)
    Jump("loc_EEE")

    label("loc_ED2")


    AnonymousTalk(    #4
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_EEE")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_3_E60 end

    def Function_4_F00(): pass

    label("Function_4_F00")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FE5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x188, 1)"), scpexpr(EXPR_END)), "loc_F74")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x00得到了\x1F\x88\x01\x07\x00。\x02",
    )

    Jump("loc_F59")

    label("loc_F59")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C72)
    Jump("loc_FE2")

    label("loc_F74")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "宝箱里装有\x1F\x88\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x88\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_FC3")

    label("loc_FC3")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_FE2")

    Jump("loc_1018")

    label("loc_FE5")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1018")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_F00 end

    def Function_5_1026(): pass

    label("Function_5_1026")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_110B")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_109A")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x00得到了\x1F\xF7\x01\x07\x00。\x02",
    )

    Jump("loc_107F")

    label("loc_107F")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C73)
    Jump("loc_1108")

    label("loc_109A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "宝箱里装有\x1F\xF7\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xF7\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_10E9")

    label("loc_10E9")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_1108")

    Jump("loc_113E")

    label("loc_110B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_113E")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1026 end

    def Function_6_114C(): pass

    label("Function_6_114C")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1231")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_11C0")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x00得到了\x1F\xFB\x01\x07\x00。\x02",
    )

    Jump("loc_11A5")

    label("loc_11A5")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C74)
    Jump("loc_122E")

    label("loc_11C0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "宝箱里装有\x1F\xFB\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xFB\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_120F")

    label("loc_120F")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_122E")

    Jump("loc_1264")

    label("loc_1231")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1264")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_114C end

    def Function_7_1272(): pass

    label("Function_7_1272")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1357")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2EA, 1)"), scpexpr(EXPR_END)), "loc_12E6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x00得到了\x1F\xEA\x02\x07\x00。\x02",
    )

    Jump("loc_12CB")

    label("loc_12CB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C75)
    Jump("loc_1354")

    label("loc_12E6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "宝箱里装有\x1F\xEA\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\xEA\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1335")

    label("loc_1335")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1354")

    Jump("loc_138A")

    label("loc_1357")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_138A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1272 end

    def Function_8_1398(): pass

    label("Function_8_1398")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_147D")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_140C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x00得到了\x1F\x01\x02\x07\x00。\x02",
    )

    Jump("loc_13F1")

    label("loc_13F1")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C76)
    Jump("loc_147A")

    label("loc_140C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "宝箱里装有\x1F\x01\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x01\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_145B")

    label("loc_145B")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_147A")

    Jump("loc_14B0")

    label("loc_147D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_14B0")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_1398 end

    def Function_9_14BE(): pass

    label("Function_9_14BE")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_15E7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x7, 0x1E)
    OP_73(0x7)
    OP_6F(0x7, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x1F4)
    AddSepith(0x1, 0x1F4)
    AddSepith(0x2, 0x1F4)
    AddSepith(0x3, 0x1F4)
    AddSepith(0x4, 0x1F4)
    AddSepith(0x5, 0x1F4)
    AddSepith(0x6, 0x1F4)

    AnonymousTalk(    #20
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×５００\x01",
            "\x07\x02#57I水之耀晶片×５００\x01",
            "\x07\x02#58I火之耀晶片×５００\x01",
            "\x07\x02#59I风之耀晶片×５００\x01",
            "\x07\x02#62I时之耀晶片×５００\x01",
            "\x07\x02#60I空之耀晶片×５００\x01",
            "\x07\x02#61I幻之耀晶片×５００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C77)
    Jump("loc_1603")

    label("loc_15E7")


    AnonymousTalk(    #21
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1603")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_9_14BE end

    def Function_10_1615(): pass

    label("Function_10_1615")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16FA")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x186, 1)"), scpexpr(EXPR_END)), "loc_1689")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x00得到了\x1F\x86\x01\x07\x00。\x02",
    )

    Jump("loc_166E")

    label("loc_166E")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C78)
    Jump("loc_16F7")

    label("loc_1689")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "宝箱里装有\x1F\x86\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x86\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_16D8")

    label("loc_16D8")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_16F7")

    Jump("loc_172D")

    label("loc_16FA")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_172D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_1615 end

    def Function_11_173B(): pass

    label("Function_11_173B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1864")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x9, 0x1E)
    OP_73(0x9)
    OP_6F(0x9, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x1F4)
    AddSepith(0x1, 0x1F4)
    AddSepith(0x2, 0x1F4)
    AddSepith(0x3, 0x1F4)
    AddSepith(0x4, 0x1F4)
    AddSepith(0x5, 0x1F4)
    AddSepith(0x6, 0x1F4)

    AnonymousTalk(    #25
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×５００\x01",
            "\x07\x02#57I水之耀晶片×５００\x01",
            "\x07\x02#58I火之耀晶片×５００\x01",
            "\x07\x02#59I风之耀晶片×５００\x01",
            "\x07\x02#62I时之耀晶片×５００\x01",
            "\x07\x02#60I空之耀晶片×５００\x01",
            "\x07\x02#61I幻之耀晶片×５００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C79)
    Jump("loc_1880")

    label("loc_1864")


    AnonymousTalk(    #26
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1880")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_11_173B end

    def Function_12_1892(): pass

    label("Function_12_1892")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1904")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x1E)
    OP_73(0xA)
    OP_6F(0xA, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #27
        "\x07\x00得到了\x07\x02５０００米拉\x07\x00。\x02",
    )

    Jump("loc_18F2")

    label("loc_18F2")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7A)
    Jump("loc_1920")

    label("loc_1904")


    AnonymousTalk(    #28
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1920")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_12_1892 end

    def Function_13_1932(): pass

    label("Function_13_1932")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1A17")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_19A6")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x00得到了\x1F\x04\x02\x07\x00。\x02",
    )

    Jump("loc_198B")

    label("loc_198B")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7B)
    Jump("loc_1A14")

    label("loc_19A6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "宝箱里装有\x1F\x04\x02\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x04\x02\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_19F5")

    label("loc_19F5")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_1A14")

    Jump("loc_1A4A")

    label("loc_1A17")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1A4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_1932 end

    def Function_14_1A58(): pass

    label("Function_14_1A58")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1B26")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_6F(0xC, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B14")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_1AAD")
    Jump("loc_1AAD")

    label("loc_1AAD")


    AnonymousTalk(    #32
        "\x07\x00得到了\x07\x02达人火锅『极』\x07\x00的食谱。\x02",
    )

    Jump("loc_1AE0")

    label("loc_1AE0")

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #33
        "\x06\x07\x02达人火锅『极』\x07\x00的制作方法已经记下了。\x02",
    )


    label("loc_1B14")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7C)
    Jump("loc_1B42")

    label("loc_1B26")


    AnonymousTalk(    #34
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1B42")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_14_1A58 end

    def Function_15_1B54(): pass

    label("Function_15_1B54")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1C39")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33D, 1)"), scpexpr(EXPR_END)), "loc_1BC8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x00得到了\x1F\x3D\x03\x07\x00。\x02",
    )

    Jump("loc_1BAD")

    label("loc_1BAD")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7D)
    Jump("loc_1C36")

    label("loc_1BC8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "宝箱里装有\x1F\x3D\x03\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x3D\x03\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1C17")

    label("loc_1C17")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1C36")

    Jump("loc_1C6C")

    label("loc_1C39")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1C6C")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1B54 end

    def Function_16_1C7A(): pass

    label("Function_16_1C7A")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1D5F")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_1CEE")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x00得到了\x1F\x7D\x01\x07\x00。\x02",
    )

    Jump("loc_1CD3")

    label("loc_1CD3")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7E)
    Jump("loc_1D5C")

    label("loc_1CEE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "宝箱里装有\x1F\x7D\x01\x07\x00。\x01",
            "不过现有的数量太多，\x1F\x7D\x01\x07\x00不能再拿更多了。\x02",
        )
    )

    Jump("loc_1D3D")

    label("loc_1D3D")

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_1D5C")

    Jump("loc_1D92")

    label("loc_1D5F")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05宝箱中什么都没有。\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)

    label("loc_1D92")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1C7A end

    def Function_17_1DA0(): pass

    label("Function_17_1DA0")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ED7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xF, 0x1E)
    OP_73(0xF)
    OP_6F(0xF, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddSepith(0x0, 0x3E8)
    AddSepith(0x1, 0x3E8)
    AddSepith(0x2, 0x3E8)
    AddSepith(0x3, 0x3E8)
    AddSepith(0x4, 0x3E8)
    AddSepith(0x5, 0x3E8)
    AddSepith(0x6, 0x3E8)

    AnonymousTalk(    #41
        (
            "\x07\x00得到了：\x01",
            "\x07\x02#56I地之耀晶片×１０００\x01",
            "\x07\x02#57I水之耀晶片×１０００\x01",
            "\x07\x02#58I火之耀晶片×１０００\x01",
            "\x07\x02#59I风之耀晶片×１０００\x01",
            "\x07\x02#62I时之耀晶片×１０００\x01",
            "\x07\x02#60I空之耀晶片×１０００\x01",
            "\x07\x02#61I幻之耀晶片×１０００\x07\x00\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7F)
    Jump("loc_1EF1")

    label("loc_1ED7")


    AnonymousTalk(    #42
        "\x07\x05宝箱中什么都没有。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1EF1")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_17_1DA0 end

    SaveToFile()

Try(main)
