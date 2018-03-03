from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

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
        '',                                     # 14
        '',                                     # 15
        '',                                     # 16
        '',                                     # 17
        '',                                     # 18
        '',                                     # 19
        '',                                     # 20
        '',                                     # 21
        '',                                     # 22
        '',                                     # 23
        '',                                     # 24
        '',                                     # 25
        '',                                     # 26
        '',                                     # 27
        '',                                     # 28
        '',                                     # 29
        '',                                     # 30
        '',                                     # 31
        '',                                     # 32
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
        "Function_3_E58",          # 03, 3
        "Function_4_EF7",          # 04, 4
        "Function_5_1015",         # 05, 5
        "Function_6_1133",         # 06, 6
        "Function_7_1251",         # 07, 7
        "Function_8_136F",         # 08, 8
        "Function_9_148D",         # 09, 9
        "Function_10_15CF",        # 0A, 10
        "Function_11_16ED",        # 0B, 11
        "Function_12_182F",        # 0C, 12
        "Function_13_18CE",        # 0D, 13
        "Function_14_19EC",        # 0E, 14
        "Function_15_1AEF",        # 0F, 15
        "Function_16_1C0D",        # 10, 16
        "Function_17_1D2B",        # 11, 17
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
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_E13")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x0, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FD, 1)"), scpexpr(EXPR_END)), "loc_DA8")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05Found \x1F\xFD\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C70)
    Jump("loc_E10")

    label("loc_DA8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #1
        (
            "\x07\x05Found \x1F\xFD\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFD\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x0, 60)
    OP_70(0x0, 0x0)

    label("loc_E10")

    Jump("loc_E4A")

    label("loc_E13")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #2
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_E4A")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_2_D3A end

    def Function_3_E58(): pass

    label("Function_3_E58")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_EC5")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x1, 0x1E)
    OP_73(0x1)
    OP_6F(0x1, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #3
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C71)
    Jump("loc_EE0")

    label("loc_EC5")


    AnonymousTalk(    #4
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_EE0")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_3_E58 end

    def Function_4_EF7(): pass

    label("Function_4_EF7")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_FD0")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x2, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x188, 1)"), scpexpr(EXPR_END)), "loc_F65")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #5
        "\x07\x05Found \x1F\x88\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C72)
    Jump("loc_FCD")

    label("loc_F65")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #6
        (
            "\x07\x05Found \x1F\x88\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x88\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x2, 60)
    OP_70(0x2, 0x0)

    label("loc_FCD")

    Jump("loc_1007")

    label("loc_FD0")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #7
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1007")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_4_EF7 end

    def Function_5_1015(): pass

    label("Function_5_1015")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_10EE")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x3, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1F7, 1)"), scpexpr(EXPR_END)), "loc_1083")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #8
        "\x07\x05Found \x1F\xF7\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C73)
    Jump("loc_10EB")

    label("loc_1083")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #9
        (
            "\x07\x05Found \x1F\xF7\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xF7\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x3, 60)
    OP_70(0x3, 0x0)

    label("loc_10EB")

    Jump("loc_1125")

    label("loc_10EE")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #10
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1125")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_5_1015 end

    def Function_6_1133(): pass

    label("Function_6_1133")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_120C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x4, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x1FB, 1)"), scpexpr(EXPR_END)), "loc_11A1")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #11
        "\x07\x05Found \x1F\xFB\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C74)
    Jump("loc_1209")

    label("loc_11A1")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #12
        (
            "\x07\x05Found \x1F\xFB\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xFB\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x4, 60)
    OP_70(0x4, 0x0)

    label("loc_1209")

    Jump("loc_1243")

    label("loc_120C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #13
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1243")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_6_1133 end

    def Function_7_1251(): pass

    label("Function_7_1251")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_132A")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x5, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x2EA, 1)"), scpexpr(EXPR_END)), "loc_12BF")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #14
        "\x07\x05Found \x1F\xEA\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C75)
    Jump("loc_1327")

    label("loc_12BF")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #15
        (
            "\x07\x05Found \x1F\xEA\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\xEA\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x5, 60)
    OP_70(0x5, 0x0)

    label("loc_1327")

    Jump("loc_1361")

    label("loc_132A")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #16
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1361")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_7_1251 end

    def Function_8_136F(): pass

    label("Function_8_136F")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1448")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x6, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x201, 1)"), scpexpr(EXPR_END)), "loc_13DD")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #17
        "\x07\x05Found \x1F\x01\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C76)
    Jump("loc_1445")

    label("loc_13DD")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #18
        (
            "\x07\x05Found \x1F\x01\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x01\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x6, 60)
    OP_70(0x6, 0x0)

    label("loc_1445")

    Jump("loc_147F")

    label("loc_1448")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #19
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_147F")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_8_136F end

    def Function_9_148D(): pass

    label("Function_9_148D")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58E, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_159D")
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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x500\x01",
            "#57IWater Sepith x500\x01",
            "#58IFire Sepith x500\x01",
            "#59IWind Sepith x500\x01",
            "#62ITime Sepith x500\x01",
            "#60ISpace Sepith x500\x01",
            "#61IMirage Sepith x500.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C77)
    Jump("loc_15B8")

    label("loc_159D")


    AnonymousTalk(    #21
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_15B8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_9_148D end

    def Function_10_15CF(): pass

    label("Function_10_15CF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16A8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0x8, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x186, 1)"), scpexpr(EXPR_END)), "loc_163D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #22
        "\x07\x05Found \x1F\x86\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C78)
    Jump("loc_16A5")

    label("loc_163D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #23
        (
            "\x07\x05Found \x1F\x86\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x86\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0x8, 60)
    OP_70(0x8, 0x0)

    label("loc_16A5")

    Jump("loc_16DF")

    label("loc_16A8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #24
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_16DF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_10_15CF end

    def Function_11_16ED(): pass

    label("Function_11_16ED")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_17FD")
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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x500\x01",
            "#57IWater Sepith x500\x01",
            "#58IFire Sepith x500\x01",
            "#59IWind Sepith x500\x01",
            "#62ITime Sepith x500\x01",
            "#60ISpace Sepith x500\x01",
            "#61IMirage Sepith x500.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C79)
    Jump("loc_1818")

    label("loc_17FD")


    AnonymousTalk(    #26
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1818")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_11_16ED end

    def Function_12_182F(): pass

    label("Function_12_182F")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 2)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_189C")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xA, 0x1E)
    OP_73(0xA)
    OP_6F(0xA, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    AddMira(5000)

    AnonymousTalk(    #27
        "\x07\x05Received \x07\x025,000 mira\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7A)
    Jump("loc_18B7")

    label("loc_189C")


    AnonymousTalk(    #28
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_18B7")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_12_182F end

    def Function_13_18CE(): pass

    label("Function_13_18CE")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 3)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_19A7")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xB, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x204, 1)"), scpexpr(EXPR_END)), "loc_193C")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #29
        "\x07\x05Found \x1F\x04\x02\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7B)
    Jump("loc_19A4")

    label("loc_193C")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #30
        (
            "\x07\x05Found \x1F\x04\x02\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x04\x02\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xB, 60)
    OP_70(0xB, 0x0)

    label("loc_19A4")

    Jump("loc_19DE")

    label("loc_19A7")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #31
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_19DE")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_13_18CE end

    def Function_14_19EC(): pass

    label("Function_14_19EC")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 4)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1ABD")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xC, 0x1E)
    OP_73(0xC)
    OP_6F(0xC, 30)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_40(0x20D, 0x0)"), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1AAB")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_AC(0x7)"), scpexpr(EXPR_END)), "loc_1A41")
    Jump("loc_1A41")

    label("loc_1A41")


    AnonymousTalk(    #32
        "A recipe was written on a scrap of paper within.\x02",
    )

    CloseMessageWindow()
    OP_22(0x11, 0x0, 0x64)

    AnonymousTalk(    #33
        "\x06\x07\x05Learned the recipe for \x07\x02Master's Hotpot\x07\x05.\x02",
    )


    label("loc_1AAB")

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7C)
    Jump("loc_1AD8")

    label("loc_1ABD")


    AnonymousTalk(    #34
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1AD8")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_14_19EC end

    def Function_15_1AEF(): pass

    label("Function_15_1AEF")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 5)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1BC8")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xD, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x33D, 1)"), scpexpr(EXPR_END)), "loc_1B5D")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #35
        "\x07\x05Found \x1F\x3D\x03\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7D)
    Jump("loc_1BC5")

    label("loc_1B5D")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #36
        (
            "\x07\x05Found \x1F\x3D\x03\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x3D\x03\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xD, 60)
    OP_70(0xD, 0x0)

    label("loc_1BC5")

    Jump("loc_1BFF")

    label("loc_1BC8")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #37
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1BFF")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_15_1AEF end

    def Function_16_1C0D(): pass

    label("Function_16_1C0D")

    SetMapFlags(0x8000000)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1CE6")
    OP_22(0x2B, 0x0, 0x64)
    OP_70(0xE, 0x3C)
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_3E(0x17D, 1)"), scpexpr(EXPR_END)), "loc_1C7B")
    FadeToDark(300, 0, 100)
    OP_22(0x11, 0x0, 0x64)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")

    AnonymousTalk(    #38
        "\x07\x05Found \x1F\x7D\x01\x07\x05.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    FadeToBright(300, 0)
    OP_A2(0x2C7E)
    Jump("loc_1CE3")

    label("loc_1C7B")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #39
        (
            "\x07\x05Found \x1F\x7D\x01\x07\x05 in chest.\x01",
            "\x07\x05Inventory full so gave up \x1F\x7D\x01\x07\x05.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_22(0x2C, 0x0, 0x64)
    OP_6F(0xE, 60)
    OP_70(0xE, 0x0)

    label("loc_1CE3")

    Jump("loc_1D1D")

    label("loc_1CE6")

    FadeToDark(300, 0, 100)
    SetChrName("")

    AnonymousTalk(    #40
        "\x07\x05The chest is empty.\x07\x00\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    OP_F7(0x19, 0x0, 0x0)

    label("loc_1D1D")

    Sleep(30)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    Return()

    # Function_16_1C0D end

    def Function_17_1D2B(): pass

    label("Function_17_1D2B")

    SetMapFlags(0x8000000)
    FadeToDark(300, 0, 100)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x58F, 7)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E42")
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
            "\x07\x02Obtained:\x01",
            "#56IEarth Sepith x1000\x01",
            "#57IWater Sepith x1000\x01",
            "#58IFire Sepith x1000\x01",
            "#59IWind Sepith x1000\x01",
            "#62ITime Sepith x1000\x01",
            "#60ISpace Sepith x1000\x01",
            "#61IMirage Sepith x1000.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    SetMessageWindowPos(72, 320, 56, 3)
    OP_A2(0x2C7F)
    Jump("loc_1E5D")

    label("loc_1E42")


    AnonymousTalk(    #42
        "\x07\x05The chest is empty.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    label("loc_1E5D")

    FadeToBright(300, 0)
    TalkEnd(0xFF)
    ClearMapFlags(0x8000000)
    OP_F7(0x19, 0x0, 0x0)
    Return()

    # Function_17_1D2B end

    SaveToFile()

Try(main)
