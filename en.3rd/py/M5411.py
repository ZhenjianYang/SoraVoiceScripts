from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5411   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5411.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60234",
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


    DeclEvent(
        X                   = 1130,
        Y                   = 3000,
        Z                   = -178880,
        Range               = 3000,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 3,
    )


    DeclActor(
        TriggerX            = 9910,
        TriggerZ            = 4000,
        TriggerY            = -184150,
        TriggerRange        = 1000,
        ActorX              = 9910,
        ActorZ              = 5000,
        ActorY              = -184150,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_EE",           # 00, 0
        "Function_1_EF",           # 01, 1
        "Function_2_F6",           # 02, 2
        "Function_3_11C",          # 03, 3
    )


    def Function_0_EE(): pass

    label("Function_0_EE")

    Return()

    # Function_0_EE end

    def Function_1_EF(): pass

    label("Function_1_EF")

    OP_71(0x405, 0x0)
    ExitThread()
    Return()

    # Function_1_EF end

    def Function_2_F6(): pass

    label("Function_2_F6")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_AD(0x24014D, 0x0, 0x0, 0x1F4)
    Sleep(500)
    OP_56(0x3)
    OP_AE(0x1F4)
    TalkEnd(0xFF)
    Return()

    # Function_2_F6 end

    def Function_3_11C(): pass

    label("Function_3_11C")

    OP_A3(0x2B6A)
    OP_A3(0x2B6B)
    OP_A3(0x2B6C)
    OP_A3(0x2B6D)
    OP_A3(0x2B6E)
    OP_A3(0x2B6F)
    OP_A3(0x2B70)
    OP_A2(0x2B71)
    Return()

    # Function_3_11C end

    SaveToFile()

Try(main)
