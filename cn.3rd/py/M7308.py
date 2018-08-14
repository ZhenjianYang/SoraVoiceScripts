from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'M7308   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M7308.x',
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


    DeclActor(
        TriggerX            = -5900,
        TriggerZ            = 7120,
        TriggerY            = 26100,
        TriggerRange        = 1000,
        ActorX              = -5900,
        ActorZ              = 8100,
        ActorY              = 26100,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 2,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_CE",           # 00, 0
        "Function_1_CF",           # 01, 1
        "Function_2_EC",           # 02, 2
    )


    def Function_0_CE(): pass

    label("Function_0_CE")

    Return()

    # Function_0_CE end

    def Function_1_CF(): pass

    label("Function_1_CF")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFE8130, 0x23009B)
    OP_22(0x17B, 0x1, 0x64)
    SetMapFlags(0x100000)
    Return()

    # Function_1_CF end

    def Function_2_EC(): pass

    label("Function_2_EC")

    TalkBegin(0xFF)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(72, 320, 56, 3)
    SetChrName("")

    AnonymousTalk(    #0
        "\x07\x05有一股不可思议的力量涌出。\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    RunExpression(0x0, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        1,
        -1,
        150,
        1,
        (
            "在这里休息\x01",      # 0
            "离开\x01",            # 1
        )
    )

    Jump("loc_15A")

    label("loc_15A")

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x1)
    FadeToBright(300, 0)
    OP_0D()
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_184"),
        (1, "loc_222"),
        (SWITCH_DEFAULT, "loc_222"),
    )


    label("loc_184")

    PlayEffect(0x86, 0xFF, 0xFFFF, 0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 0xFF, 0, 0, 0, 0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFFFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(300)
    OP_20(0x3E8)
    OP_22(0xC, 0x0, 0x64)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_22(0xD, 0x0, 0x64)
    OP_C0(0x15, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0, 0x0)
    OP_30(0x1)
    Sleep(3500)
    OP_82(0x86, 0x0)
    OP_1D(0xE0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    FadeToBright(1000, 0)
    OP_0D()

    label("loc_222")

    TalkEnd(0xFF)
    SetMapFlags(0x100000)
    Return()

    # Function_2_EC end

    SaveToFile()

Try(main)
