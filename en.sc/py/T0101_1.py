from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    # 洛连特

    CreateScenaFile(
        FileName            = 'T0101_1 ._SN',
        MapName             = 'Rolent',
        Location            = 'C0403.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60010",
        Flags               = 0,
        EntryFunctionIndex  = 0xFFFF,
        Reserved            = 0,
        IncludedScenario    = [
            '',
            'ED6_DT21/T0101_1 ._SN',
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


    ScpFunction(
        "Function_0_AA",           # 00, 0
        "Function_1_106",          # 01, 1
        "Function_2_1AF",          # 02, 2
        "Function_3_501",          # 03, 3
        "Function_4_547",          # 04, 4
        "Function_5_58D",          # 05, 5
        "Function_6_5D3",          # 06, 6
    )


    def Function_0_AA(): pass

    label("Function_0_AA")

    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        32,
        0,
        (
            "Enter Sewers\x01",      # 0
            "Stop\x01",              # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_EE"),
        (1, "loc_FA"),
        (SWITCH_DEFAULT, "loc_100"),
    )


    label("loc_EE")

    NewScene("ED6_DT21/C0500   ._SN", 100, 0, 0)
    IdleLoop()
    Jump("loc_100")

    label("loc_FA")

    TalkEnd(0xFF)
    Jump("loc_100")

    label("loc_100")

    Sleep(30)
    Return()

    # Function_0_AA end

    def Function_1_106(): pass

    label("Function_1_106")

    FadeToDark(0, 0, -1)
    OP_0D()
    OP_6D(75350, 0, 18760, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2800, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 75350, 0, 18760, 270)
    SetChrPos(0x1, 75350, 0, 18760, 270)
    SetChrPos(0x2, 75350, 0, 18760, 270)
    SetChrPos(0x3, 75350, 0, 18760, 270)
    OP_30(0x0)
    SetMapFlags(0x1)
    OP_69(0x0, 0x0)
    FadeToBright(1000, 0)
    ClearMapFlags(0x80)
    Return()

    # Function_1_106 end

    def Function_2_1AF(): pass

    label("Function_2_1AF")

    EventBegin(0x0)
    SetChrFlags(0x101, 0x80)
    SetChrFlags(0x103, 0x80)
    SetChrFlags(0xF8, 0x80)
    SetChrFlags(0xF9, 0x80)
    OP_6F(0xD, 0)
    OP_6D(66130, 0, 55700, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(2650, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)

    def lambda_20F():
        OP_6D(66730, 0, 50970, 5500)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_20F)
    FadeToBright(1000, 0)
    Sleep(1000)
    OP_70(0xD, 0x3B)
    OP_73(0xD)
    Sleep(400)
    OP_43(0x101, 0x0, 0x1, 0x3)
    Sleep(1000)
    OP_43(0x103, 0x0, 0x1, 0x4)
    Sleep(1000)
    OP_43(0xF8, 0x0, 0x1, 0x5)
    Sleep(1000)
    OP_43(0xF9, 0x0, 0x1, 0x6)
    WaitChrThread(0xF9, 0x0)
    WaitChrThread(0x101, 0x1)

    ChrTalk(    #0
        0x101,
        (
            "#1006FOookay, that's one case\x01",
            "cleared up.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #1
        0x103,
        (
            "#022FNow we need to get back\x01",
            "to our real job.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_337")

    ChrTalk(    #2
        0x106,
        (
            "#050FInvestigating the comatose\x01",
            "people, right.\x02\x03",

            "Let's get right back to it.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477")

    label("loc_337")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3A6")

    ChrTalk(    #3
        0x108,
        (
            "#072FYes, we must investigate\x01",
            "these coma cases.\x02\x03",

            "Let's resume our investigation\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477")

    label("loc_3A6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_401")

    ChrTalk(    #4
        0x104,
        (
            "#030FIndeed, the sleeping require\x01",
            "our aid.\x02\x03",

            "May we go forth at once!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_477")

    label("loc_401")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_477")

    ChrTalk(    #5
        0x105,
        (
            "#042FYes, we were investigating\x01",
            "why everyone fell comatose...\x02\x03",

            "We should get back to that\x01",
            "at once.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_477")


    ChrTalk(    #6
        0x101,
        "#1002FLet's do it!\x02",
    )

    CloseMessageWindow()
    OP_28(0x74, 0x1, 0x400)
    OP_28(0x74, 0x1, 0x800)
    OP_28(0x74, 0x4, 0x10)
    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)
    SetChrName("")
    OP_22(0x17, 0x0, 0x64)

    AnonymousTalk(    #7
        "Quest #2C[Search for Lost Cat] #0Ccompleted!\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    EventEnd(0x0)
    Return()

    # Function_2_1AF end

    def Function_3_501(): pass

    label("Function_3_501")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x101D0, 0x0, 0xBF68, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    Return()

    # Function_3_501 end

    def Function_4_547(): pass

    label("Function_4_547")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0xFD51, 0x0, 0xC58A, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_4_547 end

    def Function_5_58D(): pass

    label("Function_5_58D")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    OP_8E(0xFE, 0x10662, 0x0, 0xC58A, 0x7D0, 0x0)
    OP_8C(0xFE, 225, 400)
    Return()

    # Function_5_58D end

    def Function_6_5D3(): pass

    label("Function_6_5D3")

    SetChrPos(0xFE, 66000, 500, 55500, 0)
    ClearChrFlags(0xFE, 0x80)
    OP_8E(0xFE, 0x101D0, 0x1F4, 0xD0AC, 0x7D0, 0x0)
    OP_8C(0xFE, 0, 400)
    OP_72(0xD, 0x800)
    OP_70(0xD, 0x0)
    OP_22(0x7, 0x0, 0x64)
    OP_73(0xD)
    OP_71(0xD, 0x800)
    Sleep(1000)
    OP_8C(0xFE, 180, 400)
    OP_8E(0xFE, 0x101D0, 0x0, 0xC8C8, 0x7D0, 0x0)
    Return()

    # Function_6_5D3 end

    SaveToFile()

Try(main)
