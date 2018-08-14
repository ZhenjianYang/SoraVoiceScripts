from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    # 卢安

    CreateScenaFile(
        FileName            = 'T2200   ._SN',
        MapName             = 'Ruan',
        Location            = 'T2200.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60012",
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
        '目标用照相机',                         # 9
        '卢安市·南街区',                       # 10
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


    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x80,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 68010,
        Z                   = 0,
        Y                   = 21970,
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


    ScpFunction(
        "Function_0_EA",           # 00, 0
        "Function_1_100",          # 01, 1
        "Function_2_106",          # 02, 2
        "Function_3_1A8",          # 03, 3
        "Function_4_325",          # 04, 4
        "Function_5_3EA",          # 05, 5
    )


    def Function_0_EA(): pass

    label("Function_0_EA")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_FF")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_FF")

    Return()

    # Function_0_EA end

    def Function_1_100(): pass

    label("Function_1_100")

    OP_22(0x1C5, 0x1, 0x64)
    Return()

    # Function_1_100 end

    def Function_2_106(): pass

    label("Function_2_106")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_1A7")
    OP_8E(0xFE, 0x181E6, 0x0, 0x4A60, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x180C4, 0x0, 0x44C0, 0xBB8, 0x0)
    OP_8C(0xFE, 90, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17B10, 0x0, 0x42CC, 0xBB8, 0x0)
    OP_8C(0xFE, 180, 400)
    Sleep(1000)
    OP_8E(0xFE, 0x17A98, 0x0, 0x48C6, 0xBB8, 0x0)
    OP_8C(0xFE, 120, 400)
    OP_62(0xFE, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(3000)
    OP_63(0xFE)
    Jump("Function_2_106")

    label("loc_1A7")

    Return()

    # Function_2_106 end

    def Function_3_1A8(): pass

    label("Function_3_1A8")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1CD")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_30F")

    label("loc_1CD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E6")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_30F")

    label("loc_1E6")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1FF")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_30F")

    label("loc_1FF")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_218")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_30F")

    label("loc_218")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_231")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_30F")

    label("loc_231")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24A")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_30F")

    label("loc_24A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_263")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_30F")

    label("loc_263")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_27C")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_30F")

    label("loc_27C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_295")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_30F")

    label("loc_295")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AE")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_30F")

    label("loc_2AE")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_30F")

    label("loc_2C7")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2E0")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_30F")

    label("loc_2E0")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2F9")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_30F")

    label("loc_2F9")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_30F")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_30F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_324")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_30F")

    label("loc_324")

    Return()

    # Function_3_1A8 end

    def Function_4_325(): pass

    label("Function_4_325")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    SetChrPos(0x105, 90300, 0, 18000, 90)
    OP_6D(82160, 0, 21800, 0)
    OP_67(0, 4560, -10000, 0)
    OP_6B(2320, 0)
    OP_6C(90000, 0)
    OP_6E(406, 0)
    OP_43(0x105, 0x3, 0x0, 0x5)
    FadeToBright(2000, 0)
    OP_0D()

    def lambda_396():
        OP_6D(111300, 1000, 23740, 9500)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_396)

    def lambda_3AE():
        OP_67(0, 7320, -10000, 9500)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3AE)

    def lambda_3C6():
        OP_6C(45000, 9500)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_3C6)
    WaitChrThread(0x105, 0x3)
    FadeToDark(2000, 0, -1)
    OP_0D()
    NewScene("ED6_DT21/T2210   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_325 end

    def Function_5_3EA(): pass

    label("Function_5_3EA")


    def lambda_3F0():
        OP_8E(0xFE, 0x18178, 0x0, 0x4650, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_3F0)
    WaitChrThread(0x105, 0x1)

    def lambda_410():
        OP_8E(0xFE, 0x18178, 0x0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_410)
    WaitChrThread(0x105, 0x1)

    def lambda_430():
        OP_8E(0xFE, 0x1B2C4, 0x7D0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_430)
    WaitChrThread(0x105, 0x1)
    OP_72(0x1000, 0x0)
    ExitThread()
    OP_70(0x0, 0x1E)
    OP_73(0x0)

    def lambda_460():
        OP_8E(0xFE, 0x1BAF8, 0x7D0, 0x55F0, 0x7D0, 0x0)
        ExitThread()

    QueueWorkItem(0x105, 1, lambda_460)
    Return()

    # Function_5_3EA end

    SaveToFile()

Try(main)
