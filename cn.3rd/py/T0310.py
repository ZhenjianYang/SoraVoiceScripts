from ED63RDScenarioHelper import *

def main():
    SetCodePage("gbk")

    CreateScenaFile(
        FileName            = 'T0310   ._SN',
        MapName             = 'Rolent',
        Location            = 'T0310.x',
        MapIndex            = 15,
        MapDefaultBGM       = "ed60015",
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
        '约修亚',                               # 9
        '信',                                   # 10
        '目标用照相机',                         # 11
        '',                                     # 12
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
        'ED6_DT07/CH02220 ._CH',             # 00
        'ED6_DT07/CH02750 ._CH',             # 01
        'ED6_DT06/CH20021 ._CH',             # 02
    )

    AddCharChipPat(
        'ED6_DT07/CH02220P._CP',             # 00
        'ED6_DT07/CH02750P._CP',             # 01
        'ED6_DT06/CH20021P._CP',             # 02
    )

    DeclNpc(
        X                   = 44200,
        Z                   = 240,
        Y                   = 18540,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 1,
        ChipIndex           = 0x1,
        NpcIndex            = 0x1C1,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 3160,
        Z                   = 600,
        Y                   = 70700,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 2,
        ChipIndex           = 0x2,
        NpcIndex            = 0x1F6,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
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


    ScpFunction(
        "Function_0_122",          # 00, 0
        "Function_1_138",          # 01, 1
        "Function_2_14B",          # 02, 2
        "Function_3_2C8",          # 03, 3
    )


    def Function_0_122(): pass

    label("Function_0_122")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x42), scpexpr(EXPR_PUSH_LONG, 0x11), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_137")
    SetMapFlags(0x10000000)
    Event(0, 3)

    label("loc_137")

    Return()

    # Function_0_122 end

    def Function_1_138(): pass

    label("Function_1_138")

    OP_10(0x8, 0x1)
    OP_10(0x9, 0x1)
    OP_10(0xA, 0x0)
    OP_10(0xB, 0x0)
    OP_82(0x81, 0x0)
    OP_82(0x80, 0x0)
    Return()

    # Function_1_138 end

    def Function_2_14B(): pass

    label("Function_2_14B")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_170")
    OP_99(0xFE, 0x0, 0x7, 0x672)
    Jump("loc_2B2")

    label("loc_170")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_189")
    OP_99(0xFE, 0x1, 0x7, 0x640)
    Jump("loc_2B2")

    label("loc_189")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A2")
    OP_99(0xFE, 0x2, 0x7, 0x60E)
    Jump("loc_2B2")

    label("loc_1A2")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1BB")
    OP_99(0xFE, 0x3, 0x7, 0x5DC)
    Jump("loc_2B2")

    label("loc_1BB")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1D4")
    OP_99(0xFE, 0x4, 0x7, 0x5AA)
    Jump("loc_2B2")

    label("loc_1D4")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1ED")
    OP_99(0xFE, 0x5, 0x7, 0x578)
    Jump("loc_2B2")

    label("loc_1ED")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_206")
    OP_99(0xFE, 0x6, 0x7, 0x546)
    Jump("loc_2B2")

    label("loc_206")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_21F")
    OP_99(0xFE, 0x0, 0x7, 0x677)
    Jump("loc_2B2")

    label("loc_21F")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x8), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_238")
    OP_99(0xFE, 0x1, 0x7, 0x645)
    Jump("loc_2B2")

    label("loc_238")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x9), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_251")
    OP_99(0xFE, 0x2, 0x7, 0x613)
    Jump("loc_2B2")

    label("loc_251")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_26A")
    OP_99(0xFE, 0x3, 0x7, 0x5E1)
    Jump("loc_2B2")

    label("loc_26A")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xB), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_283")
    OP_99(0xFE, 0x4, 0x7, 0x5AF)
    Jump("loc_2B2")

    label("loc_283")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xC), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29C")
    OP_99(0xFE, 0x5, 0x7, 0x57D)
    Jump("loc_2B2")

    label("loc_29C")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0xD), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2B2")
    OP_99(0xFE, 0x6, 0x7, 0x54B)

    label("loc_2B2")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2C7")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("loc_2B2")

    label("loc_2C7")

    Return()

    # Function_2_14B end

    def Function_3_2C8(): pass

    label("Function_3_2C8")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_6D(4860, 0, 71900, 0)
    OP_67(0, 5600, -10000, 0)
    OP_6B(3000, 0)
    OP_6C(45000, 0)
    OP_6E(280, 0)
    SetChrPos(0x101, 4790, 0, 74900, 270)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 4850, 0, 71000, 270)
    SetChrSubChip(0x11, 17)
    FadeToBright(2000, 0)
    Sleep(1000)
    OP_62(0x10, 0x0, 1700, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x10)
    Sleep(300)

    def lambda_370():
        OP_8E(0xFE, 0x10CC, 0x0, 0x11558, 0x3E8, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_370)
    WaitChrThread(0x10, 0x1)
    Sleep(300)
    OP_22(0x8F, 0x0, 0x64)
    Fade(250)
    ClearChrFlags(0x11, 0x80)
    Sleep(1500)

    ChrTalk(    #0
        0x10,
        "#1675F#11P……承蒙照顾了。\x02",
    )

    CloseMessageWindow()
    OP_59()
    Sleep(500)
    OP_8C(0x10, 180, 400)
    Sleep(300)

    def lambda_3E2():
        OP_8E(0xFE, 0x10CC, 0x0, 0x107FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_3E2)
    WaitChrThread(0x10, 0x1)

    def lambda_402():
        OP_8E(0xFE, 0xBB8, 0x0, 0x1048C, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_402)
    WaitChrThread(0x10, 0x1)

    def lambda_422():
        OP_8E(0xFE, 0xBB8, 0x0, 0x102FC, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_422)
    WaitChrThread(0x10, 0x1)
    FadeToDark(2000, 0, -1)
    OP_22(0x6, 0x0, 0x64)
    Sleep(300)

    def lambda_456():
        OP_8E(0xFE, 0xBB8, 0x0, 0xFBF4, 0x5DC, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_456)

    def lambda_471():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 2, lambda_471)
    WaitChrThread(0x10, 0x1)
    OP_22(0x7, 0x0, 0x64)
    OP_0D()
    OP_A2(0x2506)
    NewScene("ED6_DT21/T0300   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_3_2C8 end

    SaveToFile()

Try(main)
