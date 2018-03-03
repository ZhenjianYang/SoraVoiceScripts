from ED63RDScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'M5406   ._SN',
        MapName             = 'Gaiden3',
        Location            = 'M5406.x',
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
        'Don',                                  # 9
        'Kyle',                                 # 10
        'Sky Bandit',                           # 11
        'Sky Bandit',                           # 12
        'Sky Bandit',                           # 13
        'Sky Bandit',                           # 14
        'Sky Bandit',                           # 15
        'Sky Bandit',                           # 16
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
        'ED6_DT07/CH02110 ._CH',             # 00
        'ED6_DT07/CH00290 ._CH',             # 01
        'ED6_DT07/CH00291 ._CH',             # 02
        'ED6_DT07/CH02120 ._CH',             # 03
        'ED6_DT07/CH00300 ._CH',             # 04
        'ED6_DT07/CH00301 ._CH',             # 05
        'ED6_DT07/CH00360 ._CH',             # 06
        'ED6_DT07/CH00361 ._CH',             # 07
        'ED6_DT07/CH00294 ._CH',             # 08
        'ED6_DT07/CH00304 ._CH',             # 09
    )

    AddCharChipPat(
        'ED6_DT07/CH02110P._CP',             # 00
        'ED6_DT07/CH00290P._CP',             # 01
        'ED6_DT07/CH00291P._CP',             # 02
        'ED6_DT07/CH02120P._CP',             # 03
        'ED6_DT07/CH00300P._CP',             # 04
        'ED6_DT07/CH00301P._CP',             # 05
        'ED6_DT07/CH00360P._CP',             # 06
        'ED6_DT07/CH00361P._CP',             # 07
        'ED6_DT07/CH00294P._CP',             # 08
        'ED6_DT07/CH00304P._CP',             # 09
    )

    DeclNpc(
        X                   = 0,
        Z                   = 0,
        Y                   = 0,
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 3,
        ChipIndex           = 0x3,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
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
        Direction           = 0,
        Unknown2            = 0,
        Unknown3            = 6,
        ChipIndex           = 0x6,
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )


    DeclEvent(
        X                   = -3720,
        Y                   = -2000,
        Z                   = -4000,
        Range               = 5440,
        Unknown_10          = 0xBB8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x0,
        Unknown_1C          = 2,
    )


    ScpFunction(
        "Function_0_21A",          # 00, 0
        "Function_1_237",          # 01, 1
        "Function_2_238",          # 02, 2
        "Function_3_249",          # 03, 3
        "Function_4_1F00",         # 04, 4
        "Function_5_1F4F",         # 05, 5
        "Function_6_1F9E",         # 06, 6
        "Function_7_1FED",         # 07, 7
        "Function_8_203C",         # 08, 8
        "Function_9_208B",         # 09, 9
        "Function_10_20DA",        # 0A, 10
        "Function_11_2869",        # 0B, 11
        "Function_12_3823",        # 0C, 12
    )


    def Function_0_21A(): pass

    label("Function_0_21A")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x4A0, 4)), scpexpr(EXPR_END)), "loc_236")
    OP_A3(0x2504)
    SetMapFlags(0x10000000)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xAD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Event(0, 11)

    label("loc_236")

    Return()

    # Function_0_21A end

    def Function_1_237(): pass

    label("Function_1_237")

    Return()

    # Function_1_237 end

    def Function_2_238(): pass

    label("Function_2_238")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x564, 7)), scpexpr(EXPR_END)), "loc_240")
    Return()

    label("loc_240")

    Call(0, 3)
    Call(0, 10)
    Return()

    # Function_2_238 end

    def Function_3_249(): pass

    label("Function_3_249")

    EventBegin(0x0)
    OP_20(0x7D0)
    LoadEffect(0x0, "map\\mp250_00.eff")
    LoadEffect(0x1, "map\\mp250_01.eff")
    LoadEffect(0x2, "monster\\msc1000.eff")
    OP_E0(238, 0x4A, 0x2)
    OP_E0(238, 0x4B, 0x3)
    OP_E0(239, 0x4C, 0x2)
    OP_E0(239, 0x4D, 0x3)
    OP_E0(240, 0x4E, 0x2)
    OP_E0(240, 0x4F, 0x3)
    OP_E0(241, 0x50, 0x2)
    OP_E0(241, 0x51, 0x3)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1600, -1000, 15930, 180)
    SetChrSubChip(0x10, 0)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30, -1000, 15930, 180)
    SetChrSubChip(0x11, 0)
    Sleep(500)

    NpcTalk(    #0
        0x10,
        "Man's Voice",
        "#4P#4SGahaha! Finally showed up, huh?\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_35F")
    OP_62(0xEE, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6")

    label("loc_35F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_387")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6")

    label("loc_387")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEE)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3AF")
    OP_62(0xEE, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_3C6")

    label("loc_3AF")

    OP_62(0xEE, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_3C6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3EE")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_455")

    label("loc_3EE")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_416")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_455")

    label("loc_416")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_43E")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_455")

    label("loc_43E")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_455")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_47D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E4")

    label("loc_47D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4A5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E4")

    label("loc_4A5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_4CD")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_4E4")

    label("loc_4CD")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_4E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_50C")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_573")

    label("loc_50C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_534")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_573")

    label("loc_534")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_55C")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_573")

    label("loc_55C")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_573")

    Sleep(1000)

    def lambda_57E():
        OP_6D(1840, -1000, 16610, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_57E)

    def lambda_596():
        OP_67(0, 6000, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_596)

    def lambda_5AE():
        OP_6B(3730, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_5AE)

    def lambda_5BE():
        OP_6C(45000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_5BE)

    def lambda_5CE():
        OP_6E(210, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 1, lambda_5CE)

    def lambda_5DE():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_5DE)

    def lambda_5EC():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_5EC)

    def lambda_5FA():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF0, 3, lambda_5FA)

    def lambda_608():
        OP_8C(0xFE, 0, 400)
        ExitThread()

    QueueWorkItem(0xF1, 3, lambda_608)
    WaitChrThread(0xEE, 0x0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_631")

    ChrTalk(    #1
        0x10B,
        "#216FOh!\x02",
    )

    CloseMessageWindow()

    label("loc_631")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_652")

    ChrTalk(    #2
        0x101,
        "#1004FHuh...?\x02",
    )

    CloseMessageWindow()

    label("loc_652")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_66F")

    ChrTalk(    #3
        0x103,
        "#1523FOh?\x02",
    )

    CloseMessageWindow()

    label("loc_66F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_695")

    ChrTalk(    #4
        0x106,
        "#055F...Seriously?\x02",
    )

    CloseMessageWindow()

    label("loc_695")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6B5")

    ChrTalk(    #5
        0x108,
        "#071FHaha...\x02",
    )

    CloseMessageWindow()

    label("loc_6B5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6D4")

    ChrTalk(    #6
        0x10C,
        "#113FOh...?\x02",
    )

    CloseMessageWindow()

    label("loc_6D4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_6F7")

    ChrTalk(    #7
        0x105,
        "#1164FOh, my...\x02",
    )

    CloseMessageWindow()

    label("loc_6F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_71B")

    ChrTalk(    #8
        0x10E,
        "#173FIs that...?\x02",
    )

    CloseMessageWindow()

    label("loc_71B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_74F")

    ChrTalk(    #9
        0x104,
        "#1541FWell, here's a surprise...\x02",
    )

    CloseMessageWindow()

    label("loc_74F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_76E")

    ChrTalk(    #10
        0x107,
        "#065FHmm...\x02",
    )

    CloseMessageWindow()

    label("loc_76E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_78F")

    ChrTalk(    #11
        0x10D,
        "#273FU-Umm...\x02",
    )

    CloseMessageWindow()

    label("loc_78F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B1")

    ChrTalk(    #12
        0x10A,
        "#1317FE-Erm...\x02",
    )

    CloseMessageWindow()

    label("loc_7B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7CF")

    ChrTalk(    #13
        0x110,
        "#1305FHmm?\x02",
    )

    CloseMessageWindow()

    label("loc_7CF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7ED")

    ChrTalk(    #14
        0x10F,
        "#1444FWho?\x02",
    )

    CloseMessageWindow()

    label("loc_7ED")


    ChrTalk(    #15
        0x102,
        "#1504FDon?! Kyle?!\x02",
    )

    CloseMessageWindow()
    Fade(1000)
    OP_6D(2180, -1000, 12120, 0)
    OP_67(0, 4890, -10000, 0)
    OP_6B(2900, 0)
    OP_6C(45000, 0)
    OP_6E(341, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C46")
    SetChrPos(0x109, 40, -1000, -2040, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8EB")
    SetChrPos(0xEF, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8B8")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_8E8")

    label("loc_8B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_8E8")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)

    label("loc_8E8")

    Jump("loc_9F2")

    label("loc_8EB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_970")
    SetChrPos(0xF0, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_93D")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_96D")

    label("loc_93D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_96D")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xEF, 1880, -1000, -2820, 0)

    label("loc_96D")

    Jump("loc_9F2")

    label("loc_970")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F2")
    SetChrPos(0xF1, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9C2")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)
    Jump("loc_9F2")

    label("loc_9C2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_9F2")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xEF, 1880, -1000, -2820, 0)

    label("loc_9F2")


    def lambda_9F8():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_9F8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC4")

    def lambda_A21():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_A21)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_A7D")

    def lambda_A4A():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_A4A)

    def lambda_A65():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A65)
    Jump("loc_AC1")

    label("loc_A7D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_AC1")

    def lambda_A91():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_A91)

    def lambda_AAC():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AAC)

    label("loc_AC1")

    Jump("loc_C2F")

    label("loc_AC4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B7B")

    def lambda_AD8():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_AD8)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B34")

    def lambda_B01():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B01)

    def lambda_B1C():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B1C)
    Jump("loc_B78")

    label("loc_B34")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_B78")

    def lambda_B48():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B48)

    def lambda_B63():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_B63)

    label("loc_B78")

    Jump("loc_C2F")

    label("loc_B7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2F")

    def lambda_B8F():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_B8F)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_BEB")

    def lambda_BB8():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_BB8)

    def lambda_BD3():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_BD3)
    Jump("loc_C2F")

    label("loc_BEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C2F")

    def lambda_BFF():
        OP_8F(0xFE, 0x64, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_BFF)

    def lambda_C1A():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_C1A)

    label("loc_C2F")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    Jump("loc_E5E")

    label("loc_C46")

    SetChrPos(0x109, 1620, -1000, -310, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_C9B")
    SetChrPos(0xEF, 340, -1000, 800, 0)
    SetChrPos(0xF0, 40, -1000, -2040, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_D20")

    label("loc_C9B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_CDF")
    SetChrPos(0xF0, 340, -1000, 800, 0)
    SetChrPos(0xEF, 40, -1000, -2040, 0)
    SetChrPos(0xF1, 1880, -1000, -2820, 0)
    Jump("loc_D20")

    label("loc_CDF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D20")
    SetChrPos(0xF1, 340, -1000, 800, 0)
    SetChrPos(0xEF, 40, -1000, -2040, 0)
    SetChrPos(0xF0, 1880, -1000, -2820, 0)

    label("loc_D20")


    def lambda_D26():
        OP_8F(0xFE, 0x64A, 0xFFFFFC18, 0x1E0A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0x109, 0, lambda_D26)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_D9D")

    def lambda_D4F():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_D4F)

    def lambda_D6A():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_D6A)

    def lambda_D85():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_D85)
    Jump("loc_E5E")

    label("loc_D9D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_DFF")

    def lambda_DB1():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_DB1)

    def lambda_DCC():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_DCC)

    def lambda_DE7():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_DE7)
    Jump("loc_E5E")

    label("loc_DFF")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_E5E")

    def lambda_E13():
        OP_8F(0xFE, 0x0, 0xFFFFFC18, 0x1EDC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_E13)

    def lambda_E2E():
        OP_8F(0xFE, 0xFFFFFF60, 0xFFFFFC18, 0x17FC, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_E2E)

    def lambda_E49():
        OP_8F(0xFE, 0x690, 0xFFFFFC18, 0x172A, 0x1388, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_E49)

    label("loc_E5E")

    WaitChrThread(0xEE, 0x0)
    WaitChrThread(0xEF, 0x0)
    WaitChrThread(0xF0, 0x0)
    WaitChrThread(0xF1, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_EF6")

    ChrTalk(    #16
        0x10B,
        "#415F#6PWh-What are you two doing here?!\x02",
    )

    CloseMessageWindow()
    OP_62(0x10B, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)

    ChrTalk(    #17
        0x10B,
        "#216F#6PWait. You couldn't be...\x02",
    )

    CloseMessageWindow()

    label("loc_EF6")


    ChrTalk(    #18
        0x109,
        "#1063F#12PEven you guys are being used, huh?\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x10,
        (
            "#198F#5PThat's how it looks.\x02\x03",

            "#490FThe whole situation's too much for my dumb\x01",
            "brain to get a handle on, to be honest... I just\x01",
            "know we've gotta do what we've gotta do.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x11,
        (
            "#204F#5PWhat he said. I don't think there's any point in\x01",
            "thinking too hard about it, anyway. Better to\x01",
            "just get it over with so you can move on.\x02\x03",

            "#200FMakes things easier for all parties involved,\x01",
            "yeah?\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_12C2")

    ChrTalk(    #21
        0x10B,
        "#216F#6PYou can't tell me you wanna fight!\x02",
    )

    CloseMessageWindow()
    Sleep(400)

    ChrTalk(    #22
        0x10B,
        (
            "#418F#6PI... I don't want to have to fight you!\x01",
            "You're my family!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #23
        0x10,
        (
            "#198F#5PWe're not the real Don and Kyle, though.\x02\x03",

            "#197FWe're just fakes made by that creeper in the\x01",
            "mask, the Lord of Phantasma.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #24
        0x11,
        (
            "#203F#5PIf I was the real Kyle, I'd be able to hold back\x01",
            "against you...but I can't. That's proof enough\x01",
            "I'm not real, I think.\x02\x03",

            "#206FSo, yeah. No holding back against us, either.\x01",
            "Come at us with all you've got!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #25
        0x10B,
        "#417F#6PDon't make me do this, you big dummies!\x02",
    )

    CloseMessageWindow()

    label("loc_12C2")


    ChrTalk(    #26
        0x102,
        "#1503F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #27
        0x11,
        (
            "#202F#5PGood to see you hangin' in there, Joshua.\x02\x03",

            "#200FHow's that whole trip been working out\x01",
            "for you?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #28
        0x102,
        (
            "#1513F#12PVery well, thanks.\x02\x03",

            "#1501FI hear your delivery company's been taking off,\x01",
            "too.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #29
        0x10,
        (
            "#198F#5PWell, we can't afford to be lazy when we've got\x01",
            "a debt to Her Majesty to repay.\x02\x03",

            "#490FAll the more reason you need to get everything\x01",
            "squared away here and get back out to the real\x01",
            "world. We can't do it without Josette!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #30
        0x11,
        (
            "#203F#5PYeah... She's the one who handles all our\x01",
            "accounts, you know.\x02\x03",

            "If we were forced to make do without her,\x01",
            "we'd flop within a month.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #31
        0x102,
        "#1509F#12PHaha. That sounds about right.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_15FF")

    ChrTalk(    #32
        0x10B,
        (
            "#413F#6PYou guys are so, SO dumb...\x02\x03",

            "#212FBut okay. I'll knock your blocks off!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #33
        0x11,
        (
            "#202F#5PThat's what we want to hear.\x02\x03",

            "#200FAll right, then! Bombs away, guys!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_162B")

    label("loc_15FF")


    ChrTalk(    #34
        0x10,
        "#191F#5PWe're ready to go on our side!\x02",
    )

    CloseMessageWindow()

    label("loc_162B")

    Sleep(300)
    Fade(250)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0x10, 1)
    SetChrSubChip(0x10, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x11, 4)
    SetChrSubChip(0x11, 0)
    OP_0D()
    Sleep(300)
    OP_22(0x233, 0x0, 0x64)
    PlayEffect(0x0, 0x1, 0xFF, -100, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x2, 0xFF, 1910, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x3, 0xFF, -2700, -900, 15870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x4, 0xFF, 4200, -900, 16059, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x5, 0xFF, -110, -900, 13340, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    PlayEffect(0x0, 0x6, 0xFF, 2000, -900, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    Sleep(1000)

    def lambda_17AC():
        OP_6D(1910, -1000, 12760, 3000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_17AC)

    def lambda_17C4():
        OP_67(0, 6230, -10000, 3000)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_17C4)

    def lambda_17DC():
        OP_6B(3170, 3000)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_17DC)

    def lambda_17EC():
        OP_6E(310, 3000)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_17EC)
    OP_0D()
    ClearChrFlags(0x12, 0x80)
    ClearChrFlags(0x13, 0x80)
    ClearChrFlags(0x14, 0x80)
    ClearChrFlags(0x15, 0x80)
    ClearChrFlags(0x16, 0x80)
    ClearChrFlags(0x17, 0x80)
    SetChrPos(0x12, -100, -4000, 18500, 180)
    SetChrPos(0x13, 1910, -4000, 18500, 180)
    SetChrPos(0x14, -2700, -4000, 15870, 180)
    SetChrPos(0x15, 4200, -4000, 16059, 180)
    SetChrPos(0x16, -110, -4000, 13340, 180)
    SetChrPos(0x17, 2000, -4000, 13110, 180)
    OP_22(0x85, 0x1, 0x64)

    def lambda_1886():

        label("loc_1886")

        OP_7C(0x14, 0x14, 0xBB8, 0x12C)
        OP_48()
        Jump("loc_1886")

    QueueWorkItem2(0x109, 3, lambda_1886)
    OP_43(0x12, 0x0, 0x0, 0x4)
    OP_43(0x13, 0x0, 0x0, 0x5)
    OP_43(0x14, 0x0, 0x0, 0x6)
    OP_43(0x15, 0x0, 0x0, 0x7)
    OP_43(0x16, 0x0, 0x0, 0x8)
    OP_43(0x17, 0x0, 0x0, 0x9)
    OP_62(0x109, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1909")
    OP_62(0xEF, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1970")

    label("loc_1909")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1931")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1970")

    label("loc_1931")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1959")
    OP_62(0xEF, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1970")

    label("loc_1959")

    OP_62(0xEF, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1970")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_199D")
    OP_62(0xF0, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A04")

    label("loc_199D")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19C5")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A04")

    label("loc_19C5")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_19ED")
    OP_62(0xF0, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A04")

    label("loc_19ED")

    OP_62(0xF0, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A04")

    Sleep(50)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x7), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A31")
    OP_62(0xF1, 0x0, 2300, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A98")

    label("loc_1A31")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A59")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A98")

    label("loc_1A59")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xF), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1A81")
    OP_62(0xF1, 0x0, 1700, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Jump("loc_1A98")

    label("loc_1A81")

    OP_62(0xF1, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)

    label("loc_1A98")

    Sleep(1000)
    Fade(250)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0x109, 10)
    SetChrSubChip(0x109, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xEF, 12)
    SetChrSubChip(0xEF, 0)
    Sleep(80)
    OP_22(0xD8, 0x0, 0x64)
    SetChrChipByIndex(0xF0, 14)
    SetChrSubChip(0xF0, 0)
    Sleep(50)
    OP_22(0xD5, 0x0, 0x64)
    SetChrChipByIndex(0xF1, 16)
    SetChrSubChip(0xF1, 0)
    OP_0D()
    Sleep(300)
    WaitChrThread(0x12, 0x0)
    WaitChrThread(0x13, 0x0)
    WaitChrThread(0x14, 0x0)
    WaitChrThread(0x15, 0x0)
    WaitChrThread(0x16, 0x0)
    WaitChrThread(0x17, 0x0)
    OP_44(0x109, 0x3)
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
    OP_82(0x6, 0x0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1B7B")

    ChrTalk(    #35
        0x10B,
        "#216F#6PWh-What the heck?!\x02",
    )

    CloseMessageWindow()

    label("loc_1B7B")


    ChrTalk(    #36
        0x109,
        "#1840F#12PThanks for being so cool about this.\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #37
        0x10,
        (
            "#196F#5PLet's get this over with so these guys\x01",
            "can move on!\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #38
        0x11,
        "#201F#5PGot'cha!\x02",
    )

    CloseMessageWindow()
    Sleep(500)
    SetMessageWindowPos(80, 120, -1, -1)
    SetChrName("Former Sky Bandits")

    AnonymousTalk(    #39
        "\x07\x00#4SGot it!\x02",
    )

    OP_7C(0x0, 0xC8, 0xBB8, 0x64)
    CloseMessageWindow()
    OP_56(0x0)
    Sleep(300)

    ChrTalk(    #40
        0x11,
        "#206FWe're not gonna be holding back against you...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #41
        0x10,
        (
            "#196F...so don't you even think about holding back\x01",
            "on us!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_1CFB")

    ChrTalk(    #42
        0x10B,
        "#214F#6PI wouldn't dream of it!\x02",
    )

    CloseMessageWindow()

    label("loc_1CFB")


    ChrTalk(    #43
        0x102,
        "#1506F#12PLet's go!\x02",
    )

    CloseMessageWindow()
    Sleep(150)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    def lambda_1D28():
        OP_6D(1840, -1000, 12320, 250)
        ExitThread()

    QueueWorkItem(0xEE, 1, lambda_1D28)

    def lambda_1D40():
        OP_67(0, 6580, -10000, 250)
        ExitThread()

    QueueWorkItem(0xEE, 2, lambda_1D40)

    def lambda_1D58():
        OP_6B(2900, 250)
        ExitThread()

    QueueWorkItem(0xEE, 3, lambda_1D58)

    def lambda_1D68():
        OP_6E(240, 250)
        ExitThread()

    QueueWorkItem(0xEF, 3, lambda_1D68)
    SetChrChipByIndex(0x10, 2)

    def lambda_1D7D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x10, 0, lambda_1D7D)
    SetChrChipByIndex(0x11, 5)

    def lambda_1D9D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x11, 0, lambda_1D9D)
    SetChrChipByIndex(0x12, 7)

    def lambda_1DBD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x12, 0, lambda_1DBD)
    SetChrChipByIndex(0x13, 7)

    def lambda_1DDD():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x13, 0, lambda_1DDD)
    SetChrChipByIndex(0x14, 7)

    def lambda_1DFD():
        OP_8E(0xFE, 0xF0, 0xFFFFFC18, 0x31E2, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x14, 0, lambda_1DFD)
    SetChrChipByIndex(0x15, 7)

    def lambda_1E1D():
        OP_8E(0xFE, 0x5BE, 0xFFFFFC18, 0x3174, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0x15, 0, lambda_1E1D)
    SetChrChipByIndex(0x16, 7)

    def lambda_1E3D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x16, 0, lambda_1E3D)
    SetChrChipByIndex(0x17, 7)

    def lambda_1E5D():
        OP_91(0xFE, 0x0, 0x0, 0xFFFFEC78, 0x1964, 0x0)
        ExitThread()

    QueueWorkItem(0x17, 0, lambda_1E5D)

    def lambda_1E78():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_1E78)

    def lambda_1E93():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xEF, 0, lambda_1E93)

    def lambda_1EAE():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF0, 0, lambda_1EAE)

    def lambda_1EC9():
        OP_91(0xFE, 0x0, 0x0, 0x1388, 0x1F40, 0x0)
        ExitThread()

    QueueWorkItem(0xF1, 0, lambda_1EC9)
    WaitChrThread(0xEE, 0x1)
    WaitChrThread(0xEE, 0x2)
    WaitChrThread(0xEE, 0x3)
    WaitChrThread(0xEF, 0x3)
    Battle(0x2AC, 0x0, 0x0, 0x0, 0xFF)
    Return()

    # Function_3_249 end

    def Function_4_1F00(): pass

    label("Function_4_1F00")

    PlayEffect(0x1, 0xFF, 0xFF, -100, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_4_1F00 end

    def Function_5_1F4F(): pass

    label("Function_5_1F4F")

    PlayEffect(0x1, 0xFF, 0xFF, 1910, -900, 18500, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_5_1F4F end

    def Function_6_1F9E(): pass

    label("Function_6_1F9E")

    PlayEffect(0x1, 0xFF, 0xFF, -2700, -900, 15870, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_6_1F9E end

    def Function_7_1FED(): pass

    label("Function_7_1FED")

    PlayEffect(0x1, 0xFF, 0xFF, 4200, -900, 16059, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_7_1FED end

    def Function_8_203C(): pass

    label("Function_8_203C")

    PlayEffect(0x1, 0xFF, 0xFF, -110, -900, 13340, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_8_203C end

    def Function_9_208B(): pass

    label("Function_9_208B")

    PlayEffect(0x1, 0xFF, 0xFF, 2000, -900, 13110, 0, 0, 0, 500, 500, 500, 0xFF, 0, 0, 0, 0)
    OP_91(0xFE, 0x0, 0xBB8, 0x0, 0x4B0, 0x0)
    ClearChrFlags(0xFE, 0x4)
    Return()

    # Function_9_208B end

    def Function_10_20DA(): pass

    label("Function_10_20DA")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    OP_20(0x0)
    Sleep(1000)
    OP_1D(0xAD)
    SetMapFlags(0x2000000)
    OP_44(0xEE, 0x0)
    OP_44(0xEF, 0x0)
    OP_44(0xF0, 0x0)
    OP_44(0xF1, 0x0)
    OP_44(0x10, 0x0)
    OP_44(0x11, 0x0)
    OP_44(0x12, 0x0)
    OP_44(0x13, 0x0)
    OP_44(0x14, 0x0)
    OP_44(0x15, 0x0)
    OP_44(0x16, 0x0)
    OP_44(0x17, 0x0)
    OP_4F(0x1C, (scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    SetChrFlags(0x12, 0x80)
    SetChrFlags(0x13, 0x80)
    SetChrFlags(0x14, 0x80)
    SetChrFlags(0x15, 0x80)
    SetChrFlags(0x16, 0x80)
    SetChrFlags(0x17, 0x80)
    ClearChrFlags(0x10, 0x80)
    SetChrPos(0x10, 1600, -1000, 15930, 180)
    SetChrChipByIndex(0x10, 8)
    SetChrSubChip(0x10, 3)
    SetChrFlags(0x10, 0x800)
    ClearChrFlags(0x11, 0x80)
    SetChrPos(0x11, -30, -1000, 15930, 180)
    SetChrChipByIndex(0x11, 9)
    SetChrSubChip(0x11, 3)
    SetChrFlags(0x11, 0x800)
    OP_43(0x10, 0x3, 0x0, 0xC)
    OP_43(0x11, 0x3, 0x0, 0xC)
    LoadEffect(0x0, "map\\mp259_02.eff")
    LoadEffect(0x1, "map\\mp256_00.eff")
    OP_22(0x146, 0x1, 0x3C)
    PlayEffect(0x0, 0x0, 0x10, 50, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    PlayEffect(0x0, 0x2, 0x11, 0, 600, 100, 0, 0, 0, 2200, 2400, 1000, 0xFF, 0, 0, 0, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_23EE")
    SetChrPos(0x109, -110, -1000, 11150, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E4")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22B1")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_22E1")

    label("loc_22B1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_22E1")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_22E1")

    Jump("loc_23EB")

    label("loc_22E4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2369")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2336")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2366")

    label("loc_2336")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2366")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1860, -1000, 11140, 0)

    label("loc_2366")

    Jump("loc_23EB")

    label("loc_2369")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EB")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23BB")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)
    Jump("loc_23EB")

    label("loc_23BB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_23EB")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1860, -1000, 11140, 0)

    label("loc_23EB")

    Jump("loc_24C8")

    label("loc_23EE")

    SetChrPos(0x109, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2443")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xF0, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_24C8")

    label("loc_2443")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2487")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_24C8")

    label("loc_2487")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_24C8")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_24C8")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2640, -1000, 15290, 0)
    OP_67(0, 5220, -10000, 0)
    OP_6B(3400, 0)
    OP_6C(45000, 0)
    OP_6E(229, 0)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)

    ChrTalk(    #44
        0x11,
        "#203F#5P#40WWhew... You guys are beasts...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #45
        0x10,
        "#490F#5P#40WHaha... And I'm happier for that.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_25C2")

    ChrTalk(    #46
        0x10B,
        "#418F#6PGuys...\x02",
    )

    CloseMessageWindow()

    label("loc_25C2")


    ChrTalk(    #47
        0x102,
        "#1503F#12P...\x02",
    )

    CloseMessageWindow()

    ChrTalk(    #48
        0x10,
        (
            "#198F#5P#40WWell...goes without saying, but we're just the\x01",
            "warmup act here...\x02\x03",

            "#490FYou've got some real monsters waitin' for you\x01",
            "ahead...so watch your backs...\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #49
        0x11,
        (
            "#200F#5P#40WOh, and while we'll disappear for now, it seems \x01",
            "like we'll be able to remain in this world for a\x01",
            "while longer...\x02\x03",

            "#202FWe should be able to help you out some, too.\x01",
            "Don't be afraid to call on us if you need us.\x02",
        )
    )

    CloseMessageWindow()
    Sleep(300)

    def lambda_276A():
        OP_6B(4500, 8000)
        ExitThread()

    QueueWorkItem(0xEE, 0, lambda_276A)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x1, 0x10, -100, -930, 0, 0, 0, 0, 2100, 2100, 2100, 0xFF, 0, 0, 0, 0)
    Sleep(100)
    OP_22(0x138, 0x0, 0x64)
    PlayEffect(0x1, 0x3, 0x11, -100, -930, 0, 0, 0, 0, 2000, 2000, 2000, 0xFF, 0, 0, 0, 0)
    Sleep(1000)
    OP_23(0x146)
    OP_22(0x99, 0x0, 0x64)
    OP_22(0xB8, 0x0, 0x64)
    OP_44(0x10, 0x3)
    OP_44(0x11, 0x3)

    def lambda_280D():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x10, 1, lambda_280D)

    def lambda_281F():
        OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x0, 0x3E8)
        ExitThread()

    QueueWorkItem(0x11, 1, lambda_281F)
    Sleep(800)
    Fade(1000)
    OP_82(0x0, 0x0)
    OP_82(0x1, 0x0)
    OP_82(0x2, 0x0)
    OP_82(0x3, 0x0)
    OP_0D()
    SetChrFlags(0x10, 0x80)
    SetChrFlags(0x11, 0x80)
    Sleep(1000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x2504)
    NewScene("ED6_DT21/M5408   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_10_20DA end

    def Function_11_2869(): pass

    label("Function_11_2869")

    EventBegin(0x0)
    FadeToDark(0, 0, -1)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2A23")
    SetChrPos(0x109, 310, -1000, 11150, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2919")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_28E6")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1660, -1000, 11140, 0)
    Jump("loc_2916")

    label("loc_28E6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2916")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1660, -1000, 11140, 0)

    label("loc_2916")

    Jump("loc_2A20")

    label("loc_2919")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299E")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_296B")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF1, 1660, -1000, 11140, 0)
    Jump("loc_299B")

    label("loc_296B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_299B")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1660, -1000, 11140, 0)

    label("loc_299B")

    Jump("loc_2A20")

    label("loc_299E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A20")
    SetChrPos(0x102, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_29F0")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xF0, 1660, -1000, 11140, 0)
    Jump("loc_2A20")

    label("loc_29F0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0xA), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A20")
    SetChrPos(0x10B, 250, -1000, 12840, 0)
    SetChrPos(0xEF, 1660, -1000, 11140, 0)

    label("loc_2A20")

    Jump("loc_2AFD")

    label("loc_2A23")

    SetChrPos(0x109, 1770, -1000, 12840, 0)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xEF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2A78")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xF0, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2AFD")

    label("loc_2A78")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2ABC")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF1, 1860, -1000, 11140, 0)
    Jump("loc_2AFD")

    label("loc_2ABC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_CB(0x0, 0xF1)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_2AFD")
    SetChrPos(0x102, 250, -1000, 12840, 0)
    SetChrPos(0xEF, -110, -1000, 11150, 0)
    SetChrPos(0xF0, 1860, -1000, 11140, 0)

    label("loc_2AFD")

    SetChrChipByIndex(0x0, 65535)
    SetChrChipByIndex(0x1, 65535)
    SetChrChipByIndex(0x2, 65535)
    SetChrChipByIndex(0x3, 65535)
    SetChrSubChip(0x0, 0)
    SetChrSubChip(0x1, 0)
    SetChrSubChip(0x2, 0)
    SetChrSubChip(0x3, 0)
    OP_6D(2310, -1000, 13300, 0)
    OP_67(0, 5950, -10000, 0)
    OP_6B(3260, 0)
    OP_6C(45000, 0)
    OP_6E(250, 0)
    Sleep(500)
    FadeToBright(1500, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_30BB")

    ChrTalk(    #50
        0x10B,
        (
            "#417F#5P...\x02\x03",

            "#415FAhaha... It's hard to believe they weren't the\x01",
            "real Don and Kyle.\x02\x03",

            "They were just like them in every way...\x02",
        )
    )

    CloseMessageWindow()
    OP_8C(0x102, 270, 400)
    Sleep(300)

    ChrTalk(    #51
        0x102,
        "#1503F#11PYeah... Your brothers are great.\x02",
    )

    CloseMessageWindow()
    OP_8C(0x10B, 90, 400)
    Sleep(300)

    ChrTalk(    #52
        0x10B,
        (
            "#413F#6PStill, seeing them like that's actually put me at\x01",
            "ease.\x02\x03",

            "#210FBecause there being copies of them here actually\x01",
            "points to the idea that the real Don and Kyle are\x01",
            "safe in the real world and not in this one.\x02\x03",

            "#211FRight! Time to put my back into it and help us\x01",
            "get back there, too!\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DA6")

    ChrTalk(    #53
        0x101,
        "#1006F#12PThat's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2DA6")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2DD9")

    ChrTalk(    #54
        0x10F,
        "#1442F#12PThat's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2DD9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E0E")

    ChrTalk(    #55
        0x107,
        "#560F#12PTh-That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2E0E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x9)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E40")

    ChrTalk(    #56
        0x10A,
        "#816F#12PThat's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2E40")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2E7B")

    ChrTalk(    #57
        0x105,
        "#1168F#12PHeehee. That's the spirit!\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2E7B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EB0")

    ChrTalk(    #58
        0x103,
        "#1521FHaha. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2EB0")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2EE4")

    ChrTalk(    #59
        0x106,
        "#051FHaha. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2EE4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F18")

    ChrTalk(    #60
        0x108,
        "#071FHaha. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2F18")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xD)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F4B")

    ChrTalk(    #61
        0x10E,
        "#171FHeh. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2F4B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F7F")

    ChrTalk(    #62
        0x104,
        "#1541FHeh. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2F7F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2F9F")

    ChrTalk(    #63
        0x10D,
        "#275FHeh.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2F9F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_2FD3")

    ChrTalk(    #64
        0x10C,
        "#111FHaha. That's the spirit.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3007")

    label("loc_2FD3")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3007")

    ChrTalk(    #65
        0x110,
        "#261FHeehee. Someone's fired up.\x02",
    )

    CloseMessageWindow()

    label("loc_3007")


    ChrTalk(    #66
        0x109,
        (
            "#1075F#6PEither way, we should be able to access the\x01",
            "forecastle area of the ship now.\x02\x03",

            "#1078FSo let's get going there.\x02",
        )
    )

    CloseMessageWindow()

    def lambda_3089():
        OP_8C(0xFE, 225, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_3089)
    Sleep(100)
    OP_8C(0x10B, 180, 400)
    Sleep(300)

    ChrTalk(    #67
        0x102,
        "#1500F#5PGot it.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3761")

    label("loc_30BB")


    ChrTalk(    #68
        0x102,
        (
            "#1503F#6P...\x02\x03",

            "#1513FHaha... They might not be the real Don and Kyle,\x01",
            "but they're just like them.\x02",
        )
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_OR), scpexpr(EXPR_END)), "loc_33F7")
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_31FC")

    ChrTalk(    #69
        0x110,
        (
            "#260F#12PThey seemed more like people who're too nice\x01",
            "for their own good.\x02\x03",

            "#261FThey'd probably give Estelle a run for her money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #70
        0x10F,
        "#1806F#12PHaha... Indeed.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3367")

    label("loc_31FC")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xF)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_32B8")

    ChrTalk(    #71
        0x110,
        (
            "#260F#12PThey seemed like more people who're too nice\x01",
            "for their own good.\x02\x03",

            "#261FThey'd probably give Estelle a run for her money.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #72
        0x109,
        "#1840F#5PHaha. Probably, yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3367")

    label("loc_32B8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xE)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3367")

    ChrTalk(    #73
        0x10F,
        (
            "#1447F#12PThey seemed like a couple more people who are\x01",
            "too nice for their own good...\x02\x03",

            "#1806FPossibly even more so than Estelle.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #74
        0x109,
        "#1840F#5PHaha. Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_3367")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_33F4")

    ChrTalk(    #75
        0x101,
        (
            "#1016F#12PI am here, you know...\x02\x03",

            "#1006FStill, at least Josette should be able to rest\x01",
            "easier now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #76
        0x102,
        "#1513F#6P...Yeah.\x02",
    )

    CloseMessageWindow()

    label("loc_33F4")

    Jump("loc_3622")

    label("loc_33F7")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x0)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34AD")

    ChrTalk(    #77
        0x101,
        (
            "#1016F#12PYou know, those two always were too nice\x01",
            "for their own good.\x02\x03",

            "#1006FStill, at least Josette should be able to rest\x01",
            "easier now.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #78
        0x102,
        "#1513F#6P...Yeah.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3622")

    label("loc_34AD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_34F8")

    ChrTalk(    #79
        0x104,
        "#1541F#12PHeh. Those two are as soft as ever, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3622")

    label("loc_34F8")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3546")

    ChrTalk(    #80
        0x103,
        "#1521F#12PHaha... Those two are as soft as ever, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3622")

    label("loc_3546")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3590")

    ChrTalk(    #81
        0x106,
        "#051F#12PHeh. Those two are as soft as ever, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3622")

    label("loc_3590")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_35DA")

    ChrTalk(    #82
        0x108,
        "#070F#12PHeh. Those two are as soft as ever, I see.\x02",
    )

    CloseMessageWindow()
    Jump("loc_3622")

    label("loc_35DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xB)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3622")

    ChrTalk(    #83
        0x10C,
        "#119F#12PHaha. Those two are as soft as ever, I see.\x02",
    )

    CloseMessageWindow()

    label("loc_3622")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_3667")

    ChrTalk(    #84
        0x107,
        "#066F#12PHeehee. They seem like such nice people.\x02",
    )

    CloseMessageWindow()

    label("loc_3667")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xC)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_36B5")

    ChrTalk(    #85
        0x10D,
        "#278F#12PHeh. They never were cut out for a life of crime.\x02",
    )

    CloseMessageWindow()

    label("loc_36B5")


    def lambda_36BB():
        OP_8C(0xFE, 90, 400)
        ExitThread()

    QueueWorkItem(0x102, 0, lambda_36BB)
    Sleep(100)
    OP_8C(0x109, 270, 400)
    Sleep(300)

    ChrTalk(    #86
        0x102,
        (
            "#1500F#6PEither way, we should be able to access the\x01",
            "forecastle area of the ship now.\x02\x03",

            "So let's head there next.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #87
        0x109,
        "#1078F#11PGot it.\x02",
    )

    CloseMessageWindow()

    label("loc_3761")

    OP_20(0x7D0)
    FadeToDark(1500, 0, -1)
    OP_0D()
    OP_A2(0x2B27)
    OP_28(0x3A, 0x1, 0x40)
    OP_28(0x3A, 0x1, 0x80)
    OP_6D(910, -1000, 10500, 0)
    OP_67(0, 9500, -10000, 0)
    OP_6B(4000, 0)
    OP_6C(45000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 910, -1000, 10500, 180)
    SetChrPos(0x1, 910, -1000, 10500, 180)
    SetChrPos(0x2, 910, -1000, 10500, 180)
    SetChrPos(0x3, 910, -1000, 10500, 180)
    OP_21()
    Sleep(500)
    FadeToBright(1000, 0)
    OP_1D(0xEA)
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0xEA), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    ClearMapFlags(0x2000000)
    EventEnd(0x0)
    Return()

    # Function_11_2869 end

    def Function_12_3823(): pass

    label("Function_12_3823")

    RunExpression(0x1, (scpexpr(EXPR_RAND), scpexpr(EXPR_PUSH_LONG, 0xE), scpexpr(EXPR_IMOD), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x0), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3844")
    Sleep(100)
    Jump("loc_38BF")

    label("loc_3844")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3859")
    Sleep(200)
    Jump("loc_38BF")

    label("loc_3859")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x2), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_386E")
    Sleep(300)
    Jump("loc_38BF")

    label("loc_386E")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x3), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3883")
    Sleep(400)
    Jump("loc_38BF")

    label("loc_3883")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x4), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_3898")
    Sleep(500)
    Jump("loc_38BF")

    label("loc_3898")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x5), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38AD")
    Sleep(600)
    Jump("loc_38BF")

    label("loc_38AD")

    Jc((scpexpr(EXPR_GET_RESULT, 0x1), scpexpr(EXPR_PUSH_LONG, 0x6), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_38BF")
    Sleep(700)

    label("loc_38BF")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_38E1")
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0x78, 0x5DC)
    OP_9F(0xFE, 0xFF, 0xFF, 0xFF, 0xFF, 0x5DC)
    Jump("loc_38BF")

    label("loc_38E1")

    Return()

    # Function_12_3823 end

    SaveToFile()

Try(main)
