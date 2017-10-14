from ED6SCScenarioHelper import *

def main():
    SetCodePage("ms932")

    CreateScenaFile(
        FileName            = 'C5100   ._SN',
        MapName             = 'Other',
        Location            = 'C5100.x',
        MapIndex            = 1,
        MapDefaultBGM       = "ed60062",
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
        'Riot Arms （黒）',                     # 9
        '地震制御用ダミーキャラ',               # 10
        'Axis Pillar - Entrance',               # 11
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
        'ED6_DT29/CH12520 ._CH',             # 00
        'ED6_DT29/CH12521 ._CH',             # 01
    )

    AddCharChipPat(
        'ED6_DT29/CH12520P._CP',             # 00
        'ED6_DT29/CH12521P._CP',             # 01
    )

    DeclNpc(
        X                   = -30,
        Z                   = 4000,
        Y                   = 47660,
        Direction           = 180,
        Unknown2            = 0,
        Unknown3            = 0,
        ChipIndex           = 0x0,
        NpcIndex            = 0x185,
        InitFunctionIndex   = 0,
        InitScenaIndex      = 2,
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
        NpcIndex            = 0x1C5,
        InitFunctionIndex   = -1,
        InitScenaIndex      = -1,
        TalkFunctionIndex   = -1,
        TalkScenaIndex      = -1,
    )

    DeclNpc(
        X                   = 310,
        Z                   = 4000,
        Y                   = 82310,
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


    DeclEvent(
        X                   = 0,
        Y                   = 6000,
        Z                   = -135000,
        Range               = 2000,
        Unknown_10          = 0x3E8,
        Unknown_14          = 0x0,
        Unknown_18          = 0x40,
        Unknown_1C          = 12,
    )

    DeclEvent(
        X                   = -7000,
        Y                   = 4000,
        Z                   = -59610,
        Range               = 7130,
        Unknown_10          = 0x1388,
        Unknown_14          = 0xFFFF0C54,
        Unknown_18          = 0x0,
        Unknown_1C          = 16,
    )


    DeclActor(
        TriggerX            = -27960,
        TriggerZ            = 4000,
        TriggerY            = -101880,
        TriggerRange        = 800,
        ActorX              = -27560,
        ActorZ              = 5000,
        ActorY              = -101880,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 10,
        Unknown_22          = 0,
    )

    DeclActor(
        TriggerX            = -26160,
        TriggerZ            = 4000,
        TriggerY            = -102500,
        TriggerRange        = 800,
        ActorX              = -26140,
        ActorZ              = 6000,
        ActorY              = -102180,
        Flags               = 0x7C,
        TalkScenaIndex      = 0,
        TalkFunctionIndex   = 11,
        Unknown_22          = 0,
    )


    ScpFunction(
        "Function_0_1A2",          # 00, 0
        "Function_1_1E2",          # 01, 1
        "Function_2_263",          # 02, 2
        "Function_3_279",          # 03, 3
        "Function_4_2A2",          # 04, 4
        "Function_5_5B6",          # 05, 5
        "Function_6_5E1",          # 06, 6
        "Function_7_627",          # 07, 7
        "Function_8_66D",          # 08, 8
        "Function_9_698",          # 09, 9
        "Function_10_11CC",        # 0A, 10
        "Function_11_1206",        # 0B, 11
        "Function_12_1348",        # 0C, 12
        "Function_13_145D",        # 0D, 13
        "Function_14_15D7",        # 0E, 14
        "Function_15_165D",        # 0F, 15
        "Function_16_16F0",        # 10, 16
    )


    def Function_0_1A2(): pass

    label("Function_0_1A2")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 0)), scpexpr(EXPR_END)), "loc_1B3")
    OP_A3(0x10F0)
    Event(0, 13)
    Jump("loc_1E1")

    label("loc_1B3")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x21E, 1)), scpexpr(EXPR_END)), "loc_1C4")
    OP_A3(0x10F1)
    Event(0, 9)
    Jump("loc_1E1")

    label("loc_1C4")

    Jc((scpexpr(EXPR_PUSH_VALUE_INDEX, 0x0), scpexpr(EXPR_PUSH_LONG, 0x65), scpexpr(EXPR_EQU), scpexpr(EXPR_END)), "loc_1E1")
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x446, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_1E1")
    SetMapFlags(0x10000000)
    Event(0, 4)

    label("loc_1E1")

    Return()

    # Function_0_1A2 end

    def Function_1_1E2(): pass

    label("Function_1_1E2")

    OP_16(0x2, 0xFA0, 0xFFFE0C00, 0xFFFD92E8, 0x230071)
    OP_72(0x0, 0x20)
    OP_72(0x0, 0x8)
    OP_6F(0x0, 0)
    OP_71(0x3, 0x4)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_255")
    OP_4F(0x1, (scpexpr(EXPR_PUSH_LONG, 0x42), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_10(0x2, 0x1)
    OP_64(0x0, 0x1)
    OP_71(0x4, 0x4)
    OP_72(0x1, 0x10)
    OP_72(0x1, 0x20)
    OP_72(0x1, 0x8)
    OP_6F(0x1, 30)
    OP_43(0x9, 0x3, 0x0, 0x3)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    OP_22(0x85, 0x1, 0x46)
    Jump("loc_262")

    label("loc_255")

    OP_10(0x2, 0x0)
    OP_71(0x1, 0x4)
    OP_22(0x1C7, 0x0, 0x64)

    label("loc_262")

    Return()

    # Function_1_1E2 end

    def Function_2_263(): pass

    label("Function_2_263")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_278")
    OP_99(0xFE, 0x0, 0x7, 0x5DC)
    Jump("Function_2_263")

    label("loc_278")

    Return()

    # Function_2_263 end

    def Function_3_279(): pass

    label("Function_3_279")

    OP_C4(0x0, 0x20)

    label("loc_27F")

    Jc((scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_END)), "loc_2A1")
    OP_7C(0x3C, 0x3C, 0x3E8, 0x384)
    Sleep(1000)
    Jump("loc_27F")

    label("loc_2A1")

    Return()

    # Function_3_279 end

    def Function_4_2A2(): pass

    label("Function_4_2A2")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_2B9")
    Call(0, 14)
    Call(0, 15)

    label("loc_2B9")

    SetChrFlags(0x0, 0x80)
    SetChrFlags(0x1, 0x80)
    SetChrFlags(0x2, 0x80)
    SetChrFlags(0x3, 0x80)
    SetChrFlags(0x8, 0x80)
    OP_6D(26370, 4000, -100180, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    FadeToBright(1000, 0)
    Sleep(500)
    OP_6F(0x2, 0)
    OP_70(0x2, 0x1E)
    OP_22(0x6D, 0x0, 0x64)
    OP_73(0x2)
    OP_43(0x101, 0x1, 0x0, 0x5)
    Sleep(800)
    LoadEffect(0x0, "map\\mp096_00.eff")
    PlayEffect(0x0, 0x0, 0xFF, 25500, 9000, -106000, -20, 0, 25, 800, 800, 800, 0xFF, 0, 0, 0, 0)
    OP_43(0x102, 0x1, 0x0, 0x6)
    Sleep(800)
    OP_43(0xF8, 0x1, 0x0, 0x7)
    Sleep(800)
    OP_43(0xF9, 0x1, 0x0, 0x8)

    def lambda_3AC():
        OP_6D(26630, 4000, -104390, 3000)
        ExitThread()

    QueueWorkItem(0x101, 0, lambda_3AC)

    def lambda_3C4():
        OP_67(0, 5830, -10000, 3000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_3C4)

    def lambda_3DC():
        OP_6B(3650, 3000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_3DC)
    WaitChrThread(0x102, 0x1)
    WaitChrThread(0x101, 0x0)
    OP_6F(0x2, 30)
    OP_70(0x2, 0x0)

    ChrTalk(    #0
        0x101,
        (
            "#1007F#5PMaaaan, it's bright.\x02\x03",

            "#1004FHey! This is...\x02",
        )
    )

    CloseMessageWindow()
    OP_62(0x102, 0x0, 2000, 0x2, 0x7, 0x50, 0x1)
    OP_22(0x27, 0x0, 0x64)
    Sleep(1000)
    OP_8C(0x102, 315, 400)

    ChrTalk(    #1
        0x102,
        "#1042F#6PEstelle, look!\x02",
    )

    CloseMessageWindow()
    OP_DB()
    Sleep(100)
    Fade(500)
    OP_6D(13060, 4000, -109970, 0)
    OP_67(0, 6220, -10000, 0)
    OP_6B(8560, 0)
    OP_6C(348000, 0)
    OP_6E(262, 0)
    OP_6D(11490, 4000, -99590, 0)
    OP_67(0, 6540, -10000, 0)
    OP_6B(7760, 0)
    OP_6C(314000, 0)
    OP_6E(262, 0)

    def lambda_503():
        OP_6D(50, 4000, 33050, 10000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_503)

    def lambda_51B():
        OP_67(0, 3780, -10000, 10000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_51B)

    def lambda_533():
        OP_6B(4190, 10000)
        ExitThread()

    QueueWorkItem(0x102, 2, lambda_533)

    def lambda_543():
        OP_6C(0, 10000)
        ExitThread()

    QueueWorkItem(0x102, 3, lambda_543)

    def lambda_553():
        OP_6E(412, 10000)
        ExitThread()

    QueueWorkItem(0xF8, 2, lambda_553)

    def lambda_563():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_563)
    Sleep(50)

    def lambda_576():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF8, 1, lambda_576)
    Sleep(50)

    def lambda_589():
        OP_8C(0xFE, 315, 400)
        ExitThread()

    QueueWorkItem(0xF9, 1, lambda_589)
    Sleep(9000)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_44(0x101, 0x2)
    OP_44(0x101, 0x3)
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C5101   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_4_2A2 end

    def Function_5_5B6(): pass

    label("Function_5_5B6")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE5F84, 0x7D0, 0x0)
    Return()

    # Function_5_5B6 end

    def Function_6_5E1(): pass

    label("Function_6_5E1")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE6F10, 0x7D0, 0x0)
    OP_8E(0xFE, 0x6766, 0xFA0, 0xFFFE64D4, 0x7D0, 0x0)
    OP_8C(0xFE, 180, 400)
    Return()

    # Function_6_5E1 end

    def Function_7_627(): pass

    label("Function_7_627")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6D38, 0xFA0, 0xFFFE6F10, 0x7D0, 0x0)
    OP_8E(0xFE, 0x724C, 0xFA0, 0xFFFE6268, 0x7D0, 0x0)
    OP_8C(0xFE, 135, 400)
    Return()

    # Function_7_627 end

    def Function_8_66D(): pass

    label("Function_8_66D")

    ClearChrFlags(0xFE, 0x80)
    SetChrPos(0xFE, 27960, 4000, -98520, 180)
    OP_8E(0xFE, 0x6BC6, 0xFA0, 0xFFFE686C, 0x7D0, 0x0)
    Return()

    # Function_8_66D end

    def Function_9_698(): pass

    label("Function_9_698")

    EventBegin(0x0)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 0)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x240, 1)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_NEQUZ_I64), scpexpr(EXPR_END)), "loc_6AF")
    Call(0, 14)
    Call(0, 15)

    label("loc_6AF")

    OP_6D(18100, 4000, -99210, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(3820, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x101, 17390, 4000, -98710, 0)
    SetChrPos(0x102, 18670, 4000, -98620, 0)
    SetChrPos(0xF8, 18060, 4000, -100190, 0)
    SetChrPos(0xF9, 19290, 4000, -100050, 0)
    FadeToBright(1000, 0)
    OP_0D()
    Sleep(500)
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_77B")

    ChrTalk(    #2
        0x108,
        "#072F#6PSo that is the Axis Pillar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_77B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7B9")

    ChrTalk(    #3
        0x106,
        "#057F#6PSo that's the Axis Pillar, huh?\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_7B9")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_7F4")

    ChrTalk(    #4
        0x109,
        "#1063F#6PThe Axis Pillar, I presume.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_7F4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_832")

    ChrTalk(    #5
        0x104,
        "#030F#6PHm. So this is the Axis Pillar.\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_832")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_870")

    ChrTalk(    #6
        0x103,
        "#022F#6PThat must be the Axis Pillar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_870")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8A2")

    ChrTalk(    #7
        0x105,
        "#1162F#6PThe Axis Pillar...\x02",
    )

    CloseMessageWindow()
    Jump("loc_8DA")

    label("loc_8A2")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_8DA")

    ChrTalk(    #8
        0x107,
        "#065F#6PWow, that's the Axis Pillar?\x02",
    )

    CloseMessageWindow()

    label("loc_8DA")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0xA)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_963")

    ChrTalk(    #9
        0x10B,
        (
            "#212F#6PI've seen that tower in the skyline\x01",
            "ever since we crashed...\x02\x03",

            "...but I didn't realize just how BIG it was.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_963")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_9DD")

    ChrTalk(    #10
        0x107,
        (
            "#065F#6PWaaaah, I knew it looked big when\x01",
            "we first saw it, but...\x02\x03",

            "But, up close, it's REALLY huge!\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_9DD")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_A65")

    ChrTalk(    #11
        0x105,
        (
            "#1162F#6PIt seemed large from a distance...\x02\x03",

            "...but you don't get a sense of the\x01",
            "scale of it until you get close.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_A65")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_AF4")

    ChrTalk(    #12
        0x103,
        (
            "#025F#6PI knew it was large from a distance,\x01",
            "but...\x02\x03",

            "#022FWhen you get close to it, the sheer\x01",
            "size of it overwhelms you.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_AF4")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_B81")

    ChrTalk(    #13
        0x104,
        (
            "#035F#6PMy goodness. At a distance,\x01",
            "it was imposing...\x02\x03",

            "#030F...but up close, the scale of it\x01",
            "takes one's breath away.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_B81")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C0A")

    ChrTalk(    #14
        0x109,
        (
            "#1065F#6PKnew it was big just seein' it\x01",
            "at a distance, but...\x02\x03",

            "#1063FMan. Bein' close to it kinda blows\x01",
            "your mind.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_C86")

    label("loc_C0A")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_C86")

    ChrTalk(    #15
        0x106,
        (
            "#052F#6PDang. It looked 'big' from a distance,\x01",
            "sure, but...\x02\x03",

            "#057FUp close, it's just... I got no words.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_C86")

    OP_62(0x101, 0x0, 2000, 0x18, 0x1B, 0xFA, 0x0)
    Sleep(1500)
    OP_63(0x101)
    Sleep(500)
    TurnDirection(0x101, 0x102, 400)
    Sleep(300)

    ChrTalk(    #16
        0x101,
        (
            "#1025F#6PHey, Joshua.\x02\x03",

            "The others are in there, aren't they?\x02",
        )
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)
    Sleep(300)

    ChrTalk(    #17
        0x102,
        (
            "#1043F#4PAlmost certainly.\x02\x03",

            "#1042FI would be willing to bet that this tower\x01",
            "originally served as, effectively, the\x01",
            "Ark's 'city hall.'\x02\x03",

            "I would imagine there's information\x01",
            "about the Aureole inside as well.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #18
        0x101,
        (
            "#1010F#6PI see...\x02\x03",

            "#1002FSo how do we do this, you think?\x01",
            "Go straight in?\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #19
        0x102,
        (
            "#1035F#4PHm... If the Enforcers are inside, we're in\x01",
            "for the hardest fights of our entire lives.\x02\x03",

            "We should probably return to the Arseille\x01",
            "first and make sure we are absolutely,\x01",
            "completely prepared.\x02\x03",

            "#1040FI'd also like to tell Julia what\x01",
            "we've discovered.\x02",
        )
    )

    CloseMessageWindow()

    ChrTalk(    #20
        0x101,
        "#1006F#6PYeah, good idea.\x02",
    )

    CloseMessageWindow()
    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x7)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_F8F")

    ChrTalk(    #21
        0x108,
        "#070F#6PLet's find the nearest rail station, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_F8F")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x5)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_FEB")

    ChrTalk(    #22
        0x106,
        (
            "#051F#6PAll right, then. Oughtta be a\x01",
            "rail-thing station around here.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_FEB")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x8)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_104C")

    ChrTalk(    #23
        0x109,
        (
            "#1060F#6POkay, should be one of those rail\x01",
            "stations around here somewhere.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_104C")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x3)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_109B")

    ChrTalk(    #24
        0x104,
        "#035F#6PLet us find the nearest halo rail station, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_109B")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x2)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_10E1")

    ChrTalk(    #25
        0x103,
        "#027F#6PTime to find a halo rail station, then.\x02",
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_10E1")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x4)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_114E")

    ChrTalk(    #26
        0x105,
        (
            "#1160F#6PLet's head back, then. I would imagine\x01",
            "a halo rail station is located nearby.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_11B0")

    label("loc_114E")

    Jc((scpexpr(EXPR_EXEC_OP, "OP_42(0x6)"), scpexpr(EXPR_PUSH_LONG, 0x1), scpexpr(EXPR_NEG), scpexpr(EXPR_NEQ), scpexpr(EXPR_END)), "loc_11B0")

    ChrTalk(    #27
        0x107,
        (
            "#061F#6POkay! Umm, there's probably a station\x01",
            "for the halo rail system nearby.\x02",
        )
    )

    CloseMessageWindow()

    label("loc_11B0")

    OP_A2(0x2230)
    OP_28(0x9E, 0x1, 0x800)
    OP_28(0x9E, 0x1, 0x1000)
    OP_28(0x9F, 0x4, 0x2)
    OP_28(0x9F, 0x4, 0x8)
    EventEnd(0x0)
    Return()

    # Function_9_698 end

    def Function_10_11CC(): pass

    label("Function_10_11CC")

    FadeToDark(300, 0, 100)

    AnonymousTalk(    #28
        "\x07\x05The door is tightly locked.\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    TalkEnd(0xFF)
    Return()

    # Function_10_11CC end

    def Function_11_1206(): pass

    label("Function_11_1206")

    FadeToDark(300, 0, 100)
    SetMessageWindowPos(-1, -1, -1, -1)

    AnonymousTalk(    #29
        "\x07\x05Emergency Evacuation Route: Axis Pillar ⇔ Calmare\x02",
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #30
        (
            "\x07\x05Automatically unlocks should any disruption occur in the\x01",
            "supply of orbal energy from the Axis Pillar.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)

    AnonymousTalk(    #31
        (
            "\x07\x05Be advised, any obstructions in the vicinity of this gate\x01",
            "that might interfere with evacuation is a crime.\x02",
        )
    )

    CloseMessageWindow()
    OP_56(0x0)
    FadeToBright(300, 0)
    SetMessageWindowPos(72, 320, 56, 3)
    TalkEnd(0xFF)
    Return()

    # Function_11_1206 end

    def Function_12_1348(): pass

    label("Function_12_1348")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_END)), "loc_1350")
    Return()

    label("loc_1350")

    EventBegin(0x0)
    Fade(1000)
    OP_6D(-290, 6000, -134740, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    OP_89(0x101, 0, 6000, -134000, 0)
    OP_89(0x102, -1000, 6000, -135000, 0)
    OP_89(0xF8, 1000, 6000, -135000, 0)
    OP_89(0xF9, 0, 6000, -136000, 0)
    OP_0D()
    Sleep(100)
    SetMapFlags(0x100000)
    OP_22(0xEB, 0x0, 0x64)
    OP_6F(0x0, 0)
    OP_70(0x0, 0x258)

    def lambda_13FC():
        OP_6D(-290, 55000, -134740, 8000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_13FC)

    def lambda_1414():
        OP_67(0, 10570, -10000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1414)

    def lambda_142C():
        OP_6C(320000, 8000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_142C)
    Sleep(2000)
    Sleep(1500)
    Sleep(1500)
    FadeToDark(1000, 0, -1)
    OP_0D()
    OP_A2(0x10F1)
    NewScene("ED6_DT21/C6003   ._SN", 100, 0, 0)
    IdleLoop()
    Return()

    # Function_12_1348 end

    def Function_13_145D(): pass

    label("Function_13_145D")

    EventBegin(0x0)
    OP_6D(-290, 45000, -134740, 0)
    OP_67(0, 10570, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(320000, 0)
    OP_6E(262, 0)
    OP_6F(0x0, 500)
    OP_48()
    OP_89(0x101, 0, 70000, -134000, 0)
    OP_89(0x102, -1000, 70000, -135000, 0)
    OP_89(0xF8, 1000, 70000, -135000, 0)
    OP_89(0xF9, 0, 70000, -136000, 0)
    OP_22(0xEB, 0x0, 0x64)
    FadeToBright(1000, 0)

    def lambda_14FC():
        OP_6D(-290, 6000, -134740, 9000)
        ExitThread()

    QueueWorkItem(0x101, 1, lambda_14FC)

    def lambda_1514():
        OP_67(0, 6500, -10000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 2, lambda_1514)

    def lambda_152C():
        OP_6C(315000, 9000)
        ExitThread()

    QueueWorkItem(0x101, 3, lambda_152C)
    OP_70(0x0, 0x0)
    OP_73(0x0)
    OP_23(0xEB)
    WaitChrThread(0x101, 0x1)
    Sleep(200)
    Fade(500)
    OP_6D(240, 6010, -133220, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    SetChrPos(0x0, 240, 6010, -133220, 0)
    SetChrPos(0x1, 240, 6010, -133220, 0)
    SetChrPos(0x2, 240, 6010, -133220, 0)
    SetChrPos(0x3, 240, 6010, -133220, 0)
    OP_0D()
    EventEnd(0x0)
    Return()

    # Function_13_145D end

    def Function_14_15D7(): pass

    label("Function_14_15D7")

    FadeToDark(0, 0, -1)
    OP_A3(0x1200)
    OP_A3(0x1201)
    RemoveParty(0x2, 0xFF)
    RemoveParty(0x5, 0xFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0x18), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))

    Menu(
        0,
        10,
        100,
        0,
        (
            "Set Scherazard as Partner\x01",      # 0
            "Set Agate as Partner\x01",           # 1
        )
    )

    MenuEnd(0x0)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    OP_5F(0x0)
    OP_56(0x0)
    Switch(
        (scpexpr(EXPR_GET_RESULT, 0x0), scpexpr(EXPR_END)),
        (0, "loc_1650"),
        (1, "loc_1656"),
        (SWITCH_DEFAULT, "loc_165C"),
    )


    label("loc_1650")

    OP_A2(0x1200)
    Jump("loc_165C")

    label("loc_1656")

    OP_A2(0x1201)
    Jump("loc_165C")

    label("loc_165C")

    Return()

    # Function_14_15D7 end

    def Function_15_165D(): pass

    label("Function_15_165D")

    FadeToDark(0, 0, -1)
    OP_6D(-78410, -8000, -230560, 0)
    OP_67(0, 6500, -10000, 0)
    OP_6B(4500, 0)
    OP_6C(315000, 0)
    OP_6E(262, 0)
    Sleep(200)
    FadeToBright(0, 0)
    OP_0D()
    OP_C9(0x0, 0x4, 0x0, 0x1, 0xFF, 0xFF, 0x5, 0x2, 0x4, 0x3, 0x6, 0x7, 0x8, 0xA, 0xFFFF)
    OP_4F(0x28, (scpexpr(EXPR_PUSH_LONG, 0xFFFF), scpexpr(EXPR_STUB), scpexpr(EXPR_END)))
    Sleep(100)
    FadeToDark(0, 0, -1)
    OP_69(0x0, 0x0)
    Return()

    # Function_15_165D end

    def Function_16_16F0(): pass

    label("Function_16_16F0")

    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x447, 6)), scpexpr(EXPR_EQUZ), scpexpr(EXPR_END)), "loc_16F9")
    Return()

    label("loc_16F9")

    EventBegin(0x2)
    Jc((scpexpr(EXPR_TEST_SCENA_FLAGS, MakeScenarioFlags(0x0, 0)), scpexpr(EXPR_END)), "loc_179D")
    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_1712"),
        (1, "loc_175A"),
        (SWITCH_DEFAULT, "loc_179A"),
    )


    label("loc_1712")


    ChrTalk(    #32
        0x101,
        (
            "#1002FThis way leads toward the Axis Pillar...\x01",
            "Let's head back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179A")

    label("loc_175A")


    ChrTalk(    #33
        0x102,
        (
            "#1042FThe Axis Pillar is this way.\x01",
            "We should turn back.\x02",
        )
    )

    CloseMessageWindow()
    Jump("loc_179A")

    label("loc_179A")

    Jump("loc_1889")

    label("loc_179D")

    Switch(
        (scpexpr(EXPR_PUSH_VALUE_INDEX, 0xA), scpexpr(EXPR_END)),
        (0, "loc_17AD"),
        (1, "loc_17EE"),
        (SWITCH_DEFAULT, "loc_1825"),
    )


    label("loc_17AD")

    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #34
        0x102,
        "#1042FEstelle! That's the way to the Axis Pillar!\x02",
    )

    CloseMessageWindow()
    Jump("loc_1825")

    label("loc_17EE")


    ChrTalk(    #35
        0x102,
        "#1042FStop! That's the way to the Axis Pillar.\x02",
    )

    CloseMessageWindow()
    Jump("loc_1825")

    label("loc_1825")

    TurnDirection(0x101, 0x102, 400)

    ChrTalk(    #36
        0x101,
        "#1002FThe escape route's straight ahead, right?\x02",
    )

    CloseMessageWindow()
    TurnDirection(0x102, 0x101, 400)

    ChrTalk(    #37
        0x102,
        "#1042FYeah, let's hurry.\x02",
    )

    CloseMessageWindow()
    OP_A2(0x0)

    label("loc_1889")

    OP_90(0x0, 0x0, 0x0, 0xFFFFFA24, 0xBB8, 0x0)
    Sleep(50)
    EventEnd(0x4)
    SetMapFlags(0x2000000)
    SetMapFlags(0x100000)
    Return()

    # Function_16_16F0 end

    SaveToFile()

Try(main)
